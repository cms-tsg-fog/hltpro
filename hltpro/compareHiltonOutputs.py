#!/usr/bin/env python

def fillPathData(content,data,prescaledPaths,index):
    active=False
    for line in content:
        line=line.rstrip()
        
        if len(line.split())<4: continue
        pathName=line.split()[0]
        
#        print pathName
        if pathName.find("HLTriggerFirstPath")!=-1: active=True
#        print pathName,active
        if active==False:continue #first line

 #       print pathName,line.split()[1]
        l1Counts=int(line.split()[1])
        psCounts=int(line.split()[2])
        hltCounts=int(line.split()[3])
    
        if psCounts!=l1Counts: prescaledPaths.append(pathName)

        if pathName not in data:
            data[pathName]=[]
            
        for i in range(len(data[pathName]),index+1):
            data[pathName].append([-1,-1])
        data[pathName][index]=hltCounts




import argparse

parser = argparse.ArgumentParser(description='compares hilton test outputs')
parser.add_argument('file1',help='input file1')
parser.add_argument('file2',help='input file2')
args = parser.parse_args()



compareData={}
preScaledPaths=[]
with open(args.file1) as f:
    content1 =f.readlines()
with open(args.file2) as f:
    content2 =f.readlines()

fillPathData(content1,compareData,preScaledPaths,0)
fillPathData(content2,compareData,preScaledPaths,1)


for pathName in compareData.keys():
  #  print pathName,compareData[pathName]
    if pathName not in preScaledPaths:
        pathData = compareData[pathName]
        
        if len(pathData)==1:
            print "path %s is in %s but not %s", (pathName,args.file1,args.file2)
        
        rate1=pathData[0]
        rate2=pathData[1]
        
        if rate1!=rate2:
            print "path %s has rate miss-match %i vs %i" % (pathName,rate1,rate2)
