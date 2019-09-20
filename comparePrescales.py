import os
import argparse
import re
import commands

parser = argparse.ArgumentParser(description='compare prescales in two menus')
parser.add_argument('menuA',help='menu A')
parser.add_argument('menuB',help='menu B')
parser.add_argument('maxCol',help='max column')
args = parser.parse_args()

def processCmd(cmd, quite = 0):
    status, output = commands.getstatusoutput(cmd)
    return output

os.system('/nfshome0/hltpro/scripts/hltConfigFromDB --v2 --gdr --configName '+str(args.menuA)+' > hlt_menuA.py')
os.system('/nfshome0/hltpro/scripts/hltConfigFromDB --v2 --gdr --configName '+str(args.menuB)+' > hlt_menuB.py')

from hlt_menuA import *

prescalesA = open('prescales_menuA.txt', 'w')
for service in process._Process__services.values():
    if hasattr(service,"prescaleTable"):
        
        for PSet in service.prescaleTable:
            pathname = re.sub('_v[0-9]*','_v',PSet.pathName.value())
            prescalesA.write(pathname+' '+str([PSet.prescales[i] for i in range(0,len(PSet.prescales))])+' \n')
prescalesA.close()

from hlt_menuB import *

prescalesB = open('prescales_menuB.txt', 'w')
for service in process._Process__services.values():
    if hasattr(service,"prescaleTable"):
        
        for PSet in service.prescaleTable:
            pathname = re.sub('_v[0-9]*','_v',PSet.pathName.value())
            prescalesB.write(pathname+' '+str([PSet.prescales[i] for i in range(0,len(PSet.prescales))])+' \n')
prescalesB.close()

with open('prescales_menuA.txt','r') as fA:
  with open ('prescales_menuB.txt','r') as fB:
    for lineA in fA:
      pathA = lineA.split('[')[0]      
      psA = lineA.split('[')[1].replace('\n','')
      psAmax = psA.split(',')
      psA=''
      c=0      
      for ps in psAmax:
        if c>args.maxCol: break
        psA+=psAmax[c]+', '
        c+=1
      psA+=']'
      output = processCmd('grep '+pathA+' prescales_menuB.txt')
      if (output==''):
          print pathA,'prescales have changed' 
          print 'menuA: ['+psA         
          print 'menuB: []'
          print ''         
      for lineB in fB: 
        pathB = lineB.split('[')[0]
        psB = lineB.split('[')[1].replace('\n','')        
        psBmax = psB.split(',')
        psB=''
        c=0      
        for ps in psBmax:
          if c>args.maxCol: break
          psB+=psBmax[c]+', '
          c+=1
        psB+=']'
        if (pathA==pathB and psA!=psB):
          print pathA,'prescales have changed' 
          print 'menuA: ['+psA         
          print 'menuB: ['+psB
          print ''
      fB.seek(0)
    for lineB in fB:  
      pathB = lineB.split('[')[0]
      psB = lineB.split('[')[1].replace('\n','')
      psBmax = psB.split(',')
      psB=''
      c=0      
      for ps in psBmax:
        if c>args.maxCol: break
        psB+=psBmax[c]+', '
        c+=1
      psB+=']'
      output = processCmd('grep '+pathB+' prescales_menuA.txt')
      if (output==''):
        print pathB,'prescales have changed' 
        print 'menuA: []'         
        print 'menuB: ['+psB
        print ''   
      
#os.system('diff prescales_menuA.txt prescales_menuB.txt')

#os.system('rm hlt_menuA.py')
#os.system('rm hlt_menuB.py')
#os.system('rm prescales_menuA.txt')
#os.system('rm prescales_menuB.txt')
