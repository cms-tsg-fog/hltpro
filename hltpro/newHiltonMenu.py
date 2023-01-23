#!/usr/bin/env python3
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
"""
 Usage: This script takes an HLT menu in ORCOFF as argument and changes the menu on the Hilton.
        It assumes that the HLT browser is currently not broken
        (if you get a menu without the name in the heading, check the browser).
"""
import argparse
import subprocess
import os

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

def gt_override(tagname):
    """ Returns a string of the python necessary to override the GT."""
    gt_str="process.GlobalTag.globaltag = '%s'\n" % tagname
    gt_str+="\n"
    return gt_str

def main(args):

    if os.getenv("CMSSW_VERSION") == None:
        print("You need to do cmsenv first")
        raise SystemExit(1)

    scripts_dir = '.'

    print(("Dumping",args.menu,"from ConfDB..."))
    hlt_cfg_cmd = [scripts_dir+'/hltConfigFromDB', '--online', '--configName', args.menu]
#    hlt_cfg_cmd += ['--services', '-PrescaleService'] # why? defies the purposes of args.unprescale
    if args.unprescale:
        print("Removing HLT prescales...")
        hlt_cfg_cmd.extend(["--services", "-PrescaleService"])
    if args.converter!="daq":
        print(f"Running a non standard ConfDB converter {args.converter}")
    hlt_cfg_cmd.append(f"--{args.converter}")

    out,err = subprocess.Popen(hlt_cfg_cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True).communicate()
    if err:
        print("error dumping menu:")
        print(err)

    with open("hlt.py", "w") as f:
        f.write(out)

    if args.unprescale:
        subprocess.Popen(['sed','-i','s~+ process.hltPSColumnMonitor~~g','hlt.py'],universal_newlines=True).communicate() 

    # check for errors in the menu
    print("Checking dump consistency")
    try:
        from hlt import process
        print(("   Found HLT version: \t%s" % process.HLTConfigVersion.tableName.value()))
    except:
        print("   HLT menu (dump is in hlt.py) is corrupted, most of the time this is a typo in menu name")
        raise SystemExit(1)

    # convert the hlt menu for online use in the Hilton
    # run the menu checker script
    print("\nRunning MenuChecker.py")
    subprocess.Popen(["python3","MenuChecker.py",args.menu],universal_newlines=True).communicate()

    # check to make sure no empty event content in any of the streams
    print("\nchecking event content output commands...")
    for output_module_name in list(process.outputModules.keys()):
        output_commands = process.outputModules[output_module_name].outputCommands.value()
        if len(output_commands) == 0:
            print(("\tWARNING: OutputModule %s has no event content!" % output_module_name))
        elif output_commands[0].find('drop *') < 0:
            print(("\tWARNING: OutputModule %s missing drop * command!" % output_module_name))

    globaltag = process.GlobalTag.globaltag.value()
    print(" ")
    print(("Checking L1 seeds in HLT menu against L1 XML in Global Tag",globaltag))
    subprocess.Popen([scripts_dir+"/L1MenuCheck_FromGT.sh", "hlt.py",globaltag],universal_newlines=True).communicate()

    print("\nChecking for Global Tag overrides:")

    reqGToverrides_ = ["cms.PSet(record = cms.string('BeamSpotOnlineLegacyObjectsRcd'), refreshTime = cms.uint64(2))",
                       "cms.PSet(record = cms.string('BeamSpotOnlineHLTObjectsRcd'),    refreshTime = cms.uint64(2))"]
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

    print("\nOverriding menu with the DAQ patch:")
    with open(scripts_dir+"/hltDAQPatch.py") as f:
        menu_overrides = f.read()

    if args.GT is not None:
        print(("Overriding GT for Hilton config with GT:", args.GT))
        menu_overrides += '\n'+gt_override(args.GT)

    if args.l1XML is not None:
        print(("Overriding L1 menu for Hilton config with XML:", args.l1XML))
        menu_overrides += '\n'+l1xml_override(args.l1XML)
        # disable consistency check between L1 menus in GT and .xml file (if the two are not different, no need to use the .xml file)
        menu_overrides += 'process.hltGtStage2ObjectMap.RequireMenuToMatchAlgoBlkInput = False\n'
        print("Rechecking HLT menu for missing seeds in XML")
        # hlt.py is just used to check the list of seeds, so it does not matter that we have not rewritten the XML override to it yet
        subprocess.Popen([scripts_dir+"/L1MenuCheck.sh", "hlt.py", args.l1XML],universal_newlines=True).communicate()

    if args.l1GT is not None:
        print(("Overriding L1 menu for Hilton config with GT record:", args.l1GT))
        menu_overrides += '\n'+l1gt_override(args.l1GT)

    if args.l1_emulator is not None:
        # Ref: https://github.com/cms-sw/cmssw/blob/CMSSW_12_0_0_pre4/HLTrigger/Configuration/python/Tools/confdb.py#L457-L465
        menu_overrides += '\n'.join(['',
          '# run the Full L1T emulator, then repack the data into a new RAW collection, to be used by the HLT',
          'from HLTrigger.Configuration.CustomConfigs import L1REPACK',
          'process = L1REPACK(process, "{:}")'.format(args.l1_emulator),
          ''])
        subprocess.Popen(['sed','-i','s|process = cms.Process( "HLT" )|from Configuration.Eras.Era_Run3_cff import Run3\\nprocess = cms.Process( "HLT", Run3 )|g','hlt.py'], universal_newlines=True).communicate()

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
    print((open("/tmp/hltpro/hlt/fffParameters.jsn").read()))

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='takes a HLT menu in ORCOFF and changes the menu on the Hilton')
    parser.add_argument('menu',help='HLT menu location in ORCOFF')
    parser.add_argument('--GT',help='Overrides the Global Tag in the resulting Hilton menu with this GT')
    parser.add_argument('--l1XML',help='Overrides the L1 menu in the resulting Hilton menu via an XML file ')
    parser.add_argument('--l1GT',help='Override the L1 menu in the resulting Hilton menu via a GlobalTag record')
                        # example would be "--l1GT L1Menu_Collisions2018_v2_1_0_xml" (see https://twiki.cern.ch/twiki/bin/viewauth/CMS/SWGuideL1TriggerMenu)
    parser.add_argument('--l1-emulator', dest = 'l1_emulator', action = 'store', metavar = 'EMULATOR', nargs = '?',
                        choices = ['Full', 'FullMC', 'Full2015Data', 'uGT'], default = None, const = 'Full',
                        help = 'Run the Full stage-2 L1T emulator.')
    parser.add_argument('--unprescale',action='store_true',help='Remove HLT prescales')
    parser.add_argument('--converter',default="daq",help='Converter to  use (daq, v2, v3, v3-dev, v3-test)')
    args = parser.parse_args()
    main(args)
