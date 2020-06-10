#!/usr/bin/env python
"""
description:
 script to print number of events accepted by selected HLT paths in a given set of luminosity blocks
"""
import argparse
import sys
import cx_Oracle
import os
import json

if __name__ == '__main__':
   parser = argparse.ArgumentParser(
     prog='./'+os.path.basename(__file__),
     formatter_class=argparse.RawDescriptionHelpFormatter,
     description=__doc__)

   parser.add_argument('-t', '--trigger', dest='trigger', required=True, action='store', default=None,
                       help='pattern to match name of trigger path(s) [example: "HLT_ZeroBias_v"]')

   parser.add_argument('-l', '--lumi-json', dest='lumi_json', required=True, action='store', default=None,
                       help='path to .json file with luminosity blocks')

   parser.add_argument('-c', '--connect-str', dest='connect_str', action='store',
#                      default='cms_runinfo_r/mickey2mouse@cms_orcon_adg',
#                      default='cms_runinfo_r/mickey2mouse@cms_omds_adg',
                       default='cms_hlt_gdr_r/convertMe!@cms_omds_adg',
                       help='connection string to the Oracle Database')

   parser.add_argument('-v', '--verbosity', dest='verbosity', action='store', type=int, default=0,
                       help='verbosity of stdout')

   args, args_unknown = parser.parse_known_args()

   triggerNameMatch = '\''+args.trigger.replace('\'','').replace('"','')+'\''
   lumiJson = args.lumi_json

   if not os.path.isfile(lumiJson):
      raise RuntimeError('invalid path to .json file with luminosity blocks [-l]: '+lumiJson)

   if args.verbosity >= 0:
      print '-'*50
      print '\033[1m{:<10}\033[0m : {:}'.format('trigger(s)', triggerNameMatch)
      print '\033[1m{:<10}\033[0m : {:}'.format('run/lumis', lumiJson)
      print '-'*50

   # DB
   conn = cx_Oracle.connect(args.connect_str)
   curs = conn.cursor()
   curs.arraysize = 50

   counts = {}
   lumiJsonDict = json.load(open(lumiJson))

   for runnumber in sorted(lumiJsonDict.keys()):
      lumiBlocks = lumiJsonDict[runnumber]
      if args.verbosity > 10:
         print '  > run={:<7} lumiBlocks={:}'.format(runnumber, lumiBlocks)
      for rangeLS in lumiBlocks:
          for lsnumber in range(rangeLS[0], rangeLS[1]+1):
              query = 'select  a.paccept,c.name as path,a.runnumber,a.lsnumber'
              query += ' from cms_runinfo.HLT_SUPERVISOR_TRIGGERPATHS a, cms_hlt_gdr.u_pathids b, cms_hlt_gdr.u_paths c'
              query += ' where runnumber='+runnumber+' and lsnumber='+str(lsnumber)+' and b.pathid=a.pathid and c.id=b.id_path and instr(c.name,'+triggerNameMatch+')>0'
              curs.execute(query)
              for rows in curs:
                  path = rows[1]
                  if args.verbosity > 20:
                     print '    > path={:<70} run={:<7} lumiBlock={:<7} counts={:<7}'.format(path, rows[2], rows[3], rows[0])
                  if path in counts:
                     counts[path] += rows[0]
                  else:
                     counts[path] = 0

   if args.verbosity > 10:
      print '-'*50

   for triggerPath in sorted(counts.keys()):
       print '{:>12} \033[1m{:<100}\033[0m'.format(counts[triggerPath], triggerPath)
