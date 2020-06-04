#!/usr/bin/python

import sys
import cx_Oracle
import string
import os 

def help() :
    print " usage: " + sys.argv[0] + " Pathname json"
    sys.exit(1)
#print len(sys.argv)
if len(sys.argv)<3 or len(sys.argv)>=5 :
    help()
elif len(sys.argv)==4:
    DEBUG=True
else:
    DEBUG=False

#print DEBUG

pathname="'"+sys.argv[1]+"'"
jsonFILE=sys.argv[2]
debug=0


#DB
#connstr='cms_runinfo_r/mickey2mouse@cms_orcon_adg'
#connstr='cms_runinfo_r/mickey2mouse@cms_omds_adg'
connstr='cms_hlt_gdr_r/convertMe!@cms_omds_adg'
conn = cx_Oracle.connect(connstr)
curs = conn.cursor()
curs.arraysize=50

#json_DCS = "/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/DCSOnly/json_DCSONLY.txt" #2016
json_DCS = "/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/DCSOnly/json_DCSONLY.txt" # 2017

if DEBUG:
    print jsonFILE
    import json
    data = json.load(open(jsonFILE))
    from pprint import pprint
#pprint(data)
#print data["294936"]
    for j in data:
        print j, data[j]
    

#### FOR TESTING QUERIES
#    count = {}
#    paths = []
#    runnumber = 295606
#    pathname = 'HLT_ZeroBias_v'
#    for lsnumber in range(10,20):
#        print lsnumber,runnumber,pathname,
#        query="select a.paccept,c.name as path,a.runnumber,a.lsnumber from cms_runinfo.HLT_SUPERVISOR_TRIGGERPATHS a,cms_hlt_gdr.u_pathids b, cms_hlt_gdr.u_paths c where a.runnumber="+str(runnumber)+" and a.lsnumber="+str(lsnumber)+" and b.pathid=a.pathid and c.id=b.id_path and instr(c.name,'" + pathname+ "')>0"
#    #    print query
#        curs.execute(query)
#        
#        ii=0
#        curs_copy=curs
#        
#        for rows in curs_copy:
#            #        print rows
#            path  = rows[1]
#            paths.append(path)
#            run   = rows[2]
#            ls    = rows[3]
#            if path in count.keys():
#                count[path]+= rows[0]
#                print '-->',count[path]
#            else:
#                count[path] = 0
#                ii=ii+1
#        print ""
#    print count
#    exit()

count = {}
paths = []
import json
json_raw = json.load(open(jsonFILE))
#print json_raw
for runnumber in json_raw:
    for rangeLS in json_raw[runnumber]:
#        print rangeLS[0],rangeLS[1]
        for lsnumber in range(rangeLS[0],rangeLS[1]+1):
#            print lsnumber,runnumber,pathname
            query='select  a.paccept,c.name as path,a.runnumber,a.lsnumber from cms_runinfo.HLT_SUPERVISOR_TRIGGERPATHS a, cms_hlt_gdr.u_pathids b, cms_hlt_gdr.u_paths c where runnumber='+runnumber+' and lsnumber= '+str(lsnumber)+'and b.pathid=a.pathid and c.id=b.id_path and instr(c.name,'+pathname+')>0'
            curs.execute(query)

            ii=0
            curs_copy=curs

            for rows in curs_copy:
#                print rows
                path  = rows[1]
                paths.append(path)
                run   = rows[2]
                ls    = rows[3]
                if path in count.keys():
                    count[path]+= rows[0]
                else:
                    count[path] = 0
                ii=ii+1

for key, value in count.items():
    print key, value
