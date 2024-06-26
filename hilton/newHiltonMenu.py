#!/usr/bin/env python3
"""
 Usage: This script takes an HLT menu in ORCOFF as argument and changes the menu on the Hilton.
        It assumes that the HLT browser is currently not broken
        (if you get a menu without the name in the heading, check the browser).
"""
import argparse
import subprocess
import os

def conddb_db():
    return 'oracle+frontier://@frontier%3A%2F%2F%28proxyurl%3Dhttp%3A%2F%2Flocalhost%3A3128%29%28serverurl%3Dhttp%3A%2F%2Flocalhost%3A8000%2FFrontierOnProd%29/CMS_CONDITIONS'

def l1xml_override(l1xml_filename):
    """ Returns a string of the python module necessary to override the L1 menu using an XML."""
    # because the L1TUtmTriggerMenuESProducer has the path hardcoded to a specific directory,
    # specifically L1Trigger/L1TGlobal/data/Luminosity/startup/ 
    # we need to escape that back up to the root of the filesystem,
    # and this is done with a hack based on using "../" a large number of times (50)
    # Note-1: if the path-finding logic of L1TUtmTriggerMenuESProducer changes in CMSSW, this function will need updating
    # Note-2: if the path of the CMSSW area is more than 50 levels deep in the filesystem,
    #         you should reconsider the location of the CMSSW area (or in extreme cases, increase the number in this function)
    l1xml_str= 'process.TriggerMenu = cms.ESProducer("L1TUtmTriggerMenuESProducer",\n'
    l1xml_str+='    L1TriggerMenuFile = cms.string("'+'../'*50+'{:}")\n'.format(os.path.abspath(l1xml_filename))
    l1xml_str+=')\n'
    return l1xml_str

def l1gt_override(tagname):
    """ Returns a string of the python necessary to override the L1 menu using an GT record."""
    l1gt_str= "process.GlobalTag.toGet = cms.VPSet(\n"
    l1gt_str+="   cms.PSet(\n"
    l1gt_str+="       connect = cms.string('frontier://(proxyurl=http://localhost:3128)(serverurl=http://localhost:8000/FrontierOnProd)(serverurl=http://localhost:8000/FrontierOnProd)(retrieve-ziplevel=0)/CMS_CONDITIONS'),\n"
    l1gt_str+="       record = cms.string('L1TUtmTriggerMenuRcd'),\n"
    l1gt_str+="       snapshotTime = cms.string('9999-03-21 17:00:00.000'),\n"
    l1gt_str+="       tag = cms.string('%s')\n" % tagname
    l1gt_str+="   )\n"
    l1gt_str+=")\n"
    return l1gt_str

def append_customisation_function(custom_func):
    append_failed = False
    try:
        custom_func_split = custom_func.split('.')
        try:
            foo = custom_func_split[2]
            append_failed = True
        except:
            custom_func_file = custom_func_split[0].replace('/', '.')
            custom_func_name = custom_func_split[1]
    except:
        append_failed = True

    if append_failed:
        warning_msg = 'WARNING: failed to append customisation function "{custom_func}"'
        print('\n>>> {warning_msg}')
        return f'# {warning_msg}'

    customFunc_str=f'from {custom_func_file} import {custom_func_name}\n'
    customFunc_str+=f'process = {custom_func_name}(process)\n'
    return customFunc_str

def customise_outputModules_selectNoEvents():
    """ Customise all the OutputModules of the HLT configuration in order to store no events in the output files of the cmsRun jobs."""
    # The Path "HLTriggerFirstPath" is guaranteed to be in every TSG menu supported by TSG, and to always reject every event
    outMod_str="for out_mod_label, out_mod in process.outputModules_().items():\n"
    outMod_str+="    try:\n"
    outMod_str+="        out_mod.SelectEvents.SelectEvents = ['HLTriggerFirstPath']\n"
    outMod_str+="    except:\n"
    outMod_str+="        pass\n"
    return outMod_str

def psColumn_override(colname):
    """ Returns the string needed to customise the HLT python configuration in order to choose a PS column."""
    pscol_str=f"process.PrescaleService.lvl1DefaultLabel = '{colname}'\n"
    pscol_str+="process.PrescaleService.forceDefault = True\n"
    return pscol_str

def gt_override(tagname):
    """ Returns a string of the python necessary to override the GT."""
    return f"process.GlobalTag.globaltag = '{tagname}'\n"

def main(args):

    if os.getenv("CMSSW_VERSION") == None:
        print("You need to do cmsenv first")
        raise SystemExit(1)

    if args.l1_menu_xml == None and args.run_number == None:
        raise RuntimeError('failed to specify run number [-r] (necessary to choose IOV of L1T-menu tag, see --help)')

    scripts_dir = '.'

    print("Dumping",args.menu,"from ConfDB ...")
    hlt_cfg_cmd = [scripts_dir+'/hltConfigFromDB', '--online', '--configName', args.menu]

    # remove PrescaleService if running unprescaled
    if args.prescale == 'none':
        print("Removing HLT prescales...")
        hlt_cfg_cmd.extend(["--services", "-PrescaleService"])

    if args.converter!="daq":
        print(f"Running a non standard ConfDB converter {args.converter}")
    hlt_cfg_cmd.append(f"--{args.converter}")

    print(" ".join(hlt_cfg_cmd))
    out,err = subprocess.Popen(hlt_cfg_cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True).communicate()
    if err:
        print("error dumping menu:")
        print(err)

    with open("hlt.py", "w") as f:
        f.write(out)

    if args.prescale == 'none':
        subprocess.Popen(['sed','-i','s~+ process.hltPSColumnMonitor~~g','hlt.py'],universal_newlines=True).communicate() 

    # check for errors in the menu
    print("Checking dump consistency")
    try:
        from hlt import process
        print("   Found HLT version: \t%s" % process.HLTConfigVersion.tableName.value())
    except:
        print("   HLT menu (dump is in hlt.py) is corrupted, most of the time this is a typo in menu name")
        raise SystemExit(1)

    # convert the hlt menu for online use in the Hilton
    # run the menu checker script
    print("\nRunning MenuChecker.py")
    if args.menuType:
        subprocess.Popen(["python3","MenuChecker.py", args.menu, "--menuType", args.menuType], universal_newlines=True).communicate()
    else:
        subprocess.Popen(["python3","MenuChecker.py", args.menu], universal_newlines=True).communicate()
    # check to make sure no empty event content in any of the streams
    print("\nchecking event content output commands...")
    for output_module_name in list(process.outputModules.keys()):
        output_commands = process.outputModules[output_module_name].outputCommands.value()
        if len(output_commands) == 0:
            print("\tWARNING: OutputModule %s has no event content!" % output_module_name)
        elif output_commands[0].find('drop *') < 0:
            print("\tWARNING: OutputModule %s missing drop * command!" % output_module_name)

    print("\nChecking for Global Tag overrides:")

    reqGToverrides_ = ["cms.PSet(record = cms.string('BeamSpotOnlineLegacyObjectsRcd'), refreshTime = cms.uint64(2))",
                       "cms.PSet(record = cms.string('BeamSpotOnlineHLTObjectsRcd'),    refreshTime = cms.uint64(2))",
                       "cms.PSet(record = cms.string('LHCInfoPerLSRcd'),                refreshTime = cms.uint64(40))",
                       "cms.PSet(record = cms.string('LHCInfoPerFillRcd'),              refreshTime = cms.uint64(40))"]
    
    reqGToverrides = []

    for reqPset in reqGToverrides_: 
        reqPset = ''.join(reqPset.split()) # strip of whitespace and newline
        reqGToverrides.append(reqPset)  

    if process.GlobalTag.toGet.value()!=[]:
        print("\033[93mWARNING:\033[0m Found the following overriding records in Global Tag:")
        print(process.GlobalTag.toGet.value())
        for pset in process.GlobalTag.toGet.value():
            pset_ = ''.join(pset.dumpPython().split()) # strip of whitespace and newline
            if pset_ not in reqGToverrides:
                print("\nChecking for Global Tag overrides: \033[31mFAIL\033[0m")
                print("\033[31mERROR:\033[0m Found unexpected overriding records in the Global Tag,\033[31m This must be removed from the menu!\033[0m")
                print(pset.dumpPython())
            else:
                print("\nChecking for Global Tag overrides: \033[32mSUCCEEDED\033[0m")
                print("\nThis listed as a required Global Tag override (related to the new BeamSpot workflow)")
                print("\033[93mWARNING:\033[0m Overriding records in the Global Tag,\033[93m Please make sure that this is what you want in the menu!\033[0m")
                print(pset.dumpPython())
    else:
        print("\033[93mWARNING:\033[0m Found no overriding records in Global Tag!")
        print("\nChecking for Global Tag overrides: \033[31mFAIL\033[0m")
        print("Please add the following required Global Tag overrides (related to the new BeamSpot workflow):")
        for reqPset in reqGToverrides_:
            print(reqPset)

    print("\nOverriding menu with the DAQ patch")
    with open(scripts_dir+"/hltDAQPatch.py") as f:
        menu_overrides = f.read()

    if args.globaltag != None:
        print(f'Overriding GT for Hilton config with GT: "{args.globaltag}"')
        menu_overrides += '\n'+gt_override(args.globaltag)

    # change L1T menu (name of L1TMenu tag in conditions database)
    if args.l1_menu_tag != None:
        print(f'Overriding L1T menu for Hilton config with conditions-db tag: "{args.l1_menu_tag}"')
        menu_overrides += '\n'+l1gt_override(args.l1_menu_tag)
        print("Checking HLT menu for missing L1T seeds in conditions-db tag")
        checkCompL1T_cmd = f'{scripts_dir}/hltCheckCompatibilityWithL1TMenu.py hlt.py -t {args.l1_menu_tag} -r {args.run_number} --db "{conddb_db()}"'

    # change L1T menu (path to .xml file)
    elif args.l1_menu_xml != None:
        print(f'Overriding L1T menu for Hilton config with XML: "{args.l1_menu_xml}"')
        menu_overrides += '\n'+l1xml_override(args.l1_menu_xml)
        print("Checking HLT menu for missing L1T seeds in XML")
        # hlt.py is just used to check the list of seeds, so it does not matter that we have not rewritten the XML override to it yet
        checkCompL1T_cmd = f'{scripts_dir}/hltCheckCompatibilityWithL1TMenu.py hlt.py -x {args.l1_menu_xml}'

    # if no customisation of L1T menu, the L1T menu is taken from the GT, so the L1T seeds are checked based on the GT
    else:
        globaltag = args.globaltag if args.globaltag != None else process.GlobalTag.globaltag.value()
        print(f'\nChecking L1T seeds in HLT menu against algos of L1T menu in the Global Tag: "{globaltag}"')
        checkCompL1T_cmd = f'{scripts_dir}/hltCheckCompatibilityWithL1TMenu.py hlt.py -g {globaltag} -r {args.run_number} --db "{conddb_db()}"'

    checkCompL1T_prc = subprocess.Popen(checkCompL1T_cmd.split(), universal_newlines = True)
    checkCompL1T_prc.communicate()
    if checkCompL1T_prc.returncode != 0:
        raise RuntimeError(f'L1T and HLT menus are not compatible: cmd="{checkCompL1T_cmd}"')

    if args.l1_emulator != None:
        # Ref: https://github.com/cms-sw/cmssw/blob/CMSSW_12_0_0_pre4/HLTrigger/Configuration/python/Tools/confdb.py#L457-L465
        menu_overrides += '\n'.join(['',
          '# run the L1T emulator, then repack the data into a new RAW collection, to be used by the HLT',
          'from HLTrigger.Configuration.CustomConfigs import L1REPACK',
          'process = L1REPACK(process, "{:}")'.format(args.l1_emulator),
          ''])
        subprocess.Popen(['sed','-i','s|process = cms.Process( "HLT" )|from Configuration.Eras.Era_Run3_cff import Run3\\nprocess = cms.Process( "HLT", Run3 )|g','hlt.py'], universal_newlines=True).communicate()

    if args.prescale != 'none':

        if not hasattr(process, 'PrescaleService'):
            print('\n>>> WARNING: the HLT configuration does not contain a PrescalService --> "--prescale {args.prescale}" will be ignored\n')

        elif args.prescale not in process.PrescaleService.lvl1Labels:
            print(f'\n>>> ERROR: the selected PS column does not exist in the HLT configuration: "{args.prescale}"\n')
            raise SystemExit(1)

        else:
            print(f'Overriding Hilton config to use PS column: "{args.prescale}"')
            menu_overrides += '\n'+psColumn_override(args.prescale)

    for custom_func in args.customisation_functions:
        menu_overrides += '\n'+append_customisation_function(custom_func)

    if args.empty_output_files:
        menu_overrides += '\n'+customise_outputModules_selectNoEvents()

    if args.customisation_commands:
        menu_overrides += '\n'
        for custom_cmd in args.customisation_commands.split('\\n'):
            menu_overrides += f'{custom_cmd}\n'

    with open("hlt.py", "a") as f:
        f.write(menu_overrides)

    # HLT configuration and fffParameters.jsn copied to tmp directory to be picked up by the HLTD  
    subprocess.Popen(["sudo","mkdir","-p","/tmp/hltpro/hlt"],universal_newlines=True).communicate()
    subprocess.Popen(["sudo","cp","hlt.py","/tmp/hltpro/hlt/HltConfig.py"],universal_newlines=True).communicate()
    subprocess.Popen(["sudo","cp","fffParameters.jsn","/tmp/hltpro/hlt"],universal_newlines=True).communicate()
    os.remove("hlt.py")
    try: os.remove("hlt.pyc")
    except: pass

    print("\nHLT Configuration:")
    print("(heading of /tmp/hltpro/hlt/HltConfig.py)")
    subprocess.Popen(["head","-1","/tmp/hltpro/hlt/HltConfig.py"],universal_newlines=True).communicate()

    print("\nfff Parameters:")
    print("(from /tmp/hltpro/hlt/fffParameters.jsn)")
    print(open("/tmp/hltpro/hlt/fffParameters.jsn").read())

###
### main
###
if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Takes a HLT menu in ORCOFF and changes the menu on the Hilton')

    # HLT menu (name of ConfDB configuration)
    parser.add_argument('menu', help = 'HLT menu location in ORCOFF')

    # HLT menu type
    parser.add_argument("--menuType", dest = "menuType", type = str, default = None,
                        help = "Set a specific menu type", choices = ["collisions", "collisionsHI", "circulating", "cosmics"])

    # ConfDB converter
    parser.add_argument('-c', '--converter', default = "daq", help = 'Converter to  use (daq, v2, v3, v3-dev, v3-test)')

    # GlobalTag [optional]
    parser.add_argument('-g', '--globaltag', help = 'Overrides the Global Tag in the resulting Hilton menu with this GT')

    # Choice of HLT-prescale column, if any [optional]
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--prescale', dest = 'prescale', action = 'store', default = 'none',
                       help = 'Run in prescale column named PRESCALE (use "--prescale none" to run without any HLT prescales)' )
    group.add_argument('--no-prescale', dest = 'prescale', action = 'store_const', const = 'none', help = 'Same as "--prescale none"' )
    group.add_argument('--unprescale', dest = 'prescale', action = 'store_const', const = 'none', help = 'Same as "--prescale none"' )

    # L1T emulator [optional]
    parser.add_argument('--l1-emulator', dest = 'l1_emulator', action = 'store', metavar = 'L1T_EMULATOR', nargs = '?',
                        choices = ['Full', 'FullMC', 'uGT'], default = None, const = 'Full',
                        help = 'Re-emulate the L1-Trigger results')

    # L1T menu (tag of conditions database, or .xml file) [optional]
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--l1', dest = 'l1_menu_tag', action = 'store', metavar = 'L1T_MENU', default = None,
                       help = 'Override the L1 menu in the resulting Hilton menu by overriding the tag of the record L1TUtmTriggerMenuRcd via the GlobalTag ESSource module')
    group.add_argument('--l1Xml', dest = 'l1_menu_xml', action = 'store', metavar = 'L1T_MENU', default = None,
                       help = 'Overrides the L1 menu in the resulting Hilton menu via an XML file')

    # Run number [optional]
    parser.add_argument('-r', '--run-number', dest = 'run_number', type = int, default = None,
                        help='Run number (necessary to choose IOV of the L1T-menu tag, unless the "--l1Xml" option is used)')

    # Additional customisation functions
    parser.add_argument('--customise', dest = 'customisation_functions', action = 'append', default = [],
                        help = 'List of customisation functions to be applied to the HLT configuration')

    parser.add_argument('--customise_commands', dest = 'customisation_commands', action = 'store', default = '',
                        help = 'String to be appended at the bottom of the HLT configuration')

    # Empty output files
    parser.add_argument('--empty-output-files', dest = 'empty_output_files', default = False, action = 'store_true',
                        help = 'Customise output modules in order to store no events in the HLT output files')

    # Parse arguments
    args = parser.parse_args()

    main(args)
