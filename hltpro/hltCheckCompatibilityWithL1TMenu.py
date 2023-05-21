#!/usr/bin/env python3
import subprocess
import tempfile

from HLTrigger.Configuration.common import filters_by_type

_db_str = "oracle+frontier://@frontier%3A%2F%2F%28proxyurl%3Dhttp%3A%2F%2Flocalhost%3A3128%29%28serverurl%3Dhttp%3A%2F%2Flocalhost%3A8000%2FFrontierOnProd%29/CMS_CONDITIONS"

def get_output(cmd, permissive=False):
    prc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    out, err = prc.communicate()
    if (not permissive) and prc.returncode:
       raise RuntimeError('get_output -- shell command failed (execute command to reproduce the error):\n'+' '*14+'> '+cmd)
    return (out, err)

def command_output_lines(cmd, stdout=True, stderr=False, permissive=False):
    if not (stdout or stderr):
       print('command_output_lines -- options "stdout" and "stderr" both set to FALSE, returning empty list')
       return []

    _tmp_out, _tmp_out_ls = get_output(cmd, permissive=permissive), []
    if stdout: _tmp_out_ls += _tmp_out[0].split('\n')
    if stderr: _tmp_out_ls += _tmp_out[1].split('\n')

    return _tmp_out_ls

def getXMLFileFromL1TMenuTag(tag_name):
    conddb_cmd = f'conddb --db "{_db_str}" list {tag_name} | grep L1TUtmTriggerMenu | tail -1'
    out_lines = [foo for foo in command_output_lines(conddb_cmd) if len(foo) > 0]
    if len(out_lines) != 1:
        raise RuntimeError('failed parsing output of conddb (more than one output line selected): cmd="{conddb_cmd}"\n{out_lines}')
    out_entries = out_lines[0].split()

    if out_entries[4] != 'L1TUtmTriggerMenu':
        raise RuntimeError('failed parsing output of conddb (record type != "L1TUtmTriggerMenu"): cmd="{conddb_cmd}"\n{out_lines}')

    xml_outfile_path = None
    with tempfile.NamedTemporaryFile() as tmp:
        xml_outfile_path = tmp.name

    get_output(f'conddb --db "{_db_str}" dump {out_entries[3]} > {xml_outfile_path}')
    return xml_outfile_path

def getL1TMenuTagFromGlobalTag(globaltag):
    conddb_cmd = f'conddb --db "{_db_str}" list {globaltag} | grep L1TUtmTriggerMenuRcd | sed "s/ *$//g" | sed "s/^.* //g"'
    out_lines = [foo for foo in command_output_lines(conddb_cmd) if len(foo) > 0]

    if len(out_lines) != 1:
        raise RuntimeError('failed parsing output of conddb (failed to find tag of L1T menu in GlobalTag): cmd="{conddb_cmd}"\n{out_lines}')

    return out_lines[0]

def getL1TSeedsFromXMLFile(xml_file_path, xmlFromDB = False):
    if xmlFromDB:
        l1tAlgosFromXML = f"grep '<first>' {xml_file_path} | sed 's/^.*<first>\(.*\)<\/first>*$/\\1/g' | sed '/--/d'"
    else:
        l1tAlgosFromXML = f"grep '<algorithm>' -A 1 {xml_file_path} | grep -v '<algorithm>' | sed 's/^.*<name>\(.*\)<\/name>*$/\\1/g' | sed '/--/d'"
    return [foo for foo in command_output_lines(l1tAlgosFromXML) if len(foo) > 0 and foo.startswith('L1_')]

def getL1TSeedsFromGlobalTag(globaltag):
    l1tMenu_tag = getL1TMenuTagFromGlobalTag(globaltag)
    return getL1TSeedsFromL1TMenuTag(l1tMenu_tag)

def getL1TSeedsFromL1TMenuTag(tag_name):
    xml_file_path = getXMLFileFromL1TMenuTag(tag_name)
    return getL1TSeedsFromXMLFile(xml_file_path, xmlFromDB = True)

def getL1TSeedUsedInHLTMenu(hltMenu_file_path):    
    try:
        foo = {'process': None}
        exec(open(hltMenu_file_path).read(), foo)
        process = foo['process']
    except:
        raise RuntimeError(f'failed to parse HLT configuration: {hltMenu_file_path}')

    ret = []
    for mod in filters_by_type(process, 'HLTL1TSeed'):
        tmplist = [foo.replace('(','').replace(')','') for foo in mod.L1SeedsLogicalExpression.value().split()]
        ret += [foo for foo in tmplist if foo.startswith('L1_')]
    for mod in filters_by_type(process, 'TriggerResultsFilter'):
        tmplist = [bar.replace('(','').replace(')','') for foo in mod.triggerConditions for bar in foo.split()]
        ret += [foo for foo in tmplist if foo.startswith('L1_') and (('*' not in foo) and ('?' not in foo))]

    return sorted(list(set(ret)))

###
### main
###
def main():
    hltMenu_file_path = '/tmp/hltpro/hlt/HltConfig.py'
    globaltag = '130X_dataRun3_HLT_v2'
    tag_name = 'L1Menu_Collisions2023_v1_1_0-v2_xml'
    xml_file_path = None

    l1tMenuAlgos = []
    if globaltag != None:
        l1tMenuAlgos = getL1TSeedsFromGlobalTag(globaltag)
    elif tag_name != None:
        l1tMenuAlgos = getL1TSeedsFromL1TMenuTag(tag_name)
    elif xml_file_path != None:
        l1tMenuAlgos = getL1TSeedsFromXMLFile(xml_file_path)

    hltMenuSeeds = getL1TSeedUsedInHLTMenu(hltMenu_file_path)
    print('='*30)
    print(f'L1T Seeds in HLT menu = {len(hltMenuSeeds)}')
    print(f'L1T Algos in L1T menu = {len(l1tMenuAlgos)}')
    print('='*30)

    l1tAlgosMissing = []
    for hltSeed in hltMenuSeeds:
        if hltSeed not in l1tMenuAlgos:
            l1tAlgosMissing += [hltSeed]
    l1tAlgosMissing = sorted(list(set(l1tAlgosMissing)))
    if l1tAlgosMissing:
        print(f'ERROR -- The following {len(l1tAlgosMissing)} L1T algos are required in the HLT menu, but missing in the L1T menu.')
        for l1tAlgo in l1tAlgosMissing:
            print(' ', l1tAlgo)
        raise SystemExit(1)
    
    raise SystemExit(0)

if __name__ == '__main__':
    main()
