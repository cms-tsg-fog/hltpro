

def printEPValues(process,pathName,printThres=9999999):
    valuesAllHigher=True
    outputStr=pathName
    hasEPFilter=False
    path = getattr(process,pathName)
    for filterName in path.moduleNames():
        filt = getattr(process,filterName)
        if type(filt).__name__=="EDFilter":
            if filt.type_()=="HLTElectronOneOEMinusOneOPFilterRegional":
               # print "old school tracking detected in %s" % pathName
                barrelCut = filt.getParameter("barrelcut").value()
                endcapCut = filt.getParameter("endcapcut").value()
                if barrelCut<printThres or endcapCut <printThres:
                    print "%s in %s : 1/E - 1/p cuts < %s (barrel) < %s (endcap) " % (filterName,pathName,barrelCut,endcapCut)
                    valuesAllHigher=False
            if filt.type_()=="HLTEgammaGenericFilter":
                if filt.getParameter("nonIsoTag").getModuleLabel()!="": print "mis configured E/gamma filter %s in %s" % (filterName,pathName)
                if filt.getParameter("isoTag").getProductInstanceLabel()=="OneOESuperMinusOneOP":
                   # print "e/p filter detected"
                    barrelCut = filt.getParameter("thrRegularEB").value()
                    endcapCut = filt.getParameter("thrRegularEE").value()
                    if barrelCut<printThres or endcapCut < printThres:
                        print "%s in %s : 1/E - 1/p cuts < %s (barrel) < %s (endcap) " % (filterName,pathName,barrelCut,endcapCut)
                        valuesAllHigher=False
    return valuesAllHigher

def compareFilter(filt):
    if filt.type_()=="HLTElectronOneOEMinusOneOPFilterRegional": return True
    if filt.type_()=="HLTEgammaGenericFilter" and filt.getParameter("isoTag").getProductInstanceLabel()=="OneOESuperMinusOneOP": return True
    return False

def getParaNamesToIgnore(filt):
    namesToIgnore=[]
    if filt.type_()=="HLTElectronOneOEMinusOneOPFilterRegional":
        namesToIgnore.append("barrelcut")
        namesToIgnore.append("endcapcut")
    if filt.type_()=="HLTEgammaGenericFilter" and filt.getParameter("isoTag").getProductInstanceLabel()=="OneOESuperMinusOneOP":
        namesToIgnore.append("thrRegularEB")
        namesToIgnore.append("thrRegularEE")
    return namesToIgnore
  
def validateChanges(fullTelsaProcess,zeroTeslaProcess):

    addedModules=["hltSingleEGL1SingleEG20","hltPreDiSC3018EIsoANDHEMass70","hltSingleEGL1SingleEG20Filter",
                  "hltEG30EtL1SingleEG20EtFilter","hltEG30HE30HEFilter","hltEG30EIso15HE30EcalIsoLastFilter",
                  "hltDiEG18HE30eHEUnseededFilter","hltEG18EIso15HE30EcalIsoUnseededFilter","hltDiEG18EIso15ANDHE30Mass70CombMassLastFilter"]

    passedEleCheck=True
    passedMuCheck=True
    
    for filterName in zeroTeslaProcess.filterNames().split():
        if filterName in addedModules: continue #skipping the modules we added to the 0T for the 0T paths
        filtZeroTelsa = getattr(zeroTeslaProcess,filterName)
        if compareFilter(filtZeroTelsa)==False: continue
        filtFullTelsa = getattr(fullTelsaProcess,filterName)
        paraNames= filtZeroTelsa.parameterNames_()
        paraNamesToIgnore = getParaNamesToIgnore(filtZeroTelsa)

        for paraName in paraNames:
            if paraName in paraNamesToIgnore: continue

            if filtZeroTelsa.getParameter(paraName).value()!=filtFullTelsa.getParameter(paraName).value():
                print filterName,paraName," error 3.8T is ",filtFullTelsa.getParameter(paraName).value()," 0T is ",filtZeroTelsa.getParameter(paraName).value()
                passedEleCheck=False

    print "passed electron check ",passedEleCheck
        
    muonModulesToCheck=["hltL3TrajSeedOIState","hltL3MuonsOIState","hltL3MuonsOIHit","hltL3TrajSeedOIHit","hltL3TrajSeedIOHit","hltL3MuonsIOHit","hltL2MuonCandidates"]
    for muModName in muonModulesToCheck:
        modZeroTelsa = getattr(zeroTeslaProcess,muModName)
        modFullTelsa = getattr(fullTelsaProcess,muModName)
        modFullTelsaPython = modFullTelsa.dumpPython().replace("MuonCollectionLabel = cms.InputTag(\"hltL2Muons\",\"UpdatedAtVtx\")","MuonCollectionLabel = cms.InputTag(\"hltL2Muons\")")
        modFullTelsaPython = modFullTelsaPython.replace("InputObjects = cms.InputTag(\"hltL2Muons\",\"UpdatedAtVtx\")","InputObjects = cms.InputTag(\"hltL2Muons\")")

        if modFullTelsaPython!=modZeroTelsa.dumpPython():
            print muModName," changes other than hltL2Muons:UpdatedAtVtx ->hltL2Muons done(or this was not done), please check in the gui"
            passedMuCheck=False

    print "passed muon check ",passedMuCheck
    
          #  print modFullTelsa.dumpPython()

import argparse
parser = argparse.ArgumentParser(description='dumps the save tag filters of a menu')
parser.add_argument('--hltMenuName0T',help="the python file containing the hlt menu zero tesla")
parser.add_argument('--hltMenuNameFT',help="the python file containing the hlt menu full tesla")

args = parser.parse_args()

hltMenuName0T=args.hltMenuName0T.rstrip(".py")
hltMenuNameFT=args.hltMenuNameFT.rstrip(".py")
## #print hltMenuName
import importlib

modFT = importlib.import_module(hltMenuNameFT)
processFullT = getattr(modFT,"process")

mod0T = importlib.import_module(hltMenuName0T)
processZeroT = getattr(mod0T,"process")

###from setSaveTags import *

#from hltFullT import process as processFullT
#from hlt0T import process as processZeroT


validateChanges(processFullT,processZeroT)

printThres=99999.
passedEPCheck=True
for pathName in processZeroT.pathNames().split():
    if printEPValues(processZeroT,pathName,printThres)==False: passedEPCheck=False
print "passed E/p cut check: ",passedEPCheck



#def isEgammaFilter(filterName):
#    if
        

