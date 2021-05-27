import FWCore.ParameterSet.VarParsing as VarParsing

import os

cmsswbase = os.path.expandvars('$CMSSW_BASE/')

options = VarParsing.VarParsing ('analysis')

options.register ('runNumber',
                  1, # default value
                  VarParsing.VarParsing.multiplicity.singleton,
                  VarParsing.VarParsing.varType.int,          # string, int, or float
                  "Run Number")

options.register ('buBaseDir',
                  '/fff/BU0', # default value
                  VarParsing.VarParsing.multiplicity.singleton,
                  VarParsing.VarParsing.varType.string,          # string, int, or float
                  "BU base directory")

options.register ('dataDir',
                  '/fff/data', # default value
                  VarParsing.VarParsing.multiplicity.singleton,
                  VarParsing.VarParsing.varType.string,          # string, int, or float
                  "FU data directory")

options.register ('numThreads',
                  1, # default value
                  VarParsing.VarParsing.multiplicity.singleton,
                  VarParsing.VarParsing.varType.int,          # string, int, or float
                  "Number of CMSSW threads")

options.register ('numFwkStreams',
                  1, # default value
                  VarParsing.VarParsing.multiplicity.singleton,
                  VarParsing.VarParsing.varType.int,          # string, int, or float
                  "Number of CMSSW streams")

options.register ('fileBrokerHost',
                  '', # default value
                  VarParsing.VarParsing.multiplicity.singleton,
                  VarParsing.VarParsing.varType.string,       # string, int, or float
                  "File broker host data network address")

options.register ('transferMode',
                  '', # default value
                  VarParsing.VarParsing.multiplicity.singleton,
                  VarParsing.VarParsing.varType.string,          # string, int, or float
                  "Selected transfer mode propagated by RCMS")

options.parseArguments()

process.options = cms.untracked.PSet(
    numberOfThreads = cms.untracked.uint32(options.numThreads),
    numberOfStreams = cms.untracked.uint32(options.numFwkStreams)
)

process.EvFDaqDirector.buBaseDir    = options.buBaseDir
process.EvFDaqDirector.baseDir      = options.dataDir
process.EvFDaqDirector.runNumber    = options.runNumber

try:
     process.EvFDaqDirector.selectedTransferMode = options.transferMode
except:
     print "unable to set process.EvFDaqDirector.selectedTransferMode=", options.transferMode

C_ALGO_VALUE = ""
C_ALGO_UNDEFINED = ""
for moduleName in process.__dict__['_Process__outputmodules']:
    modified_module = getattr(process,moduleName)
    modified_module.compression_level=cms.untracked.int32(1)
    if C_ALGO_VALUE != C_ALGO_UNDEFINED:
        modified_module.compression_algorithm=cms.untracked.string(C_ALGO_VALUE)

# to be replaced with variable passed by hltd on command line
try:
    if options.transferMode.endswith("_NOPARKING"):
        process.hltEnableParking.result = False
    else:
        process.hltEnableParking.result = True
except:
    pass

try:
    process.EvFDaqDirector.useFileBroker  = True
except:
    print "no process.EvFDaqDirector.useFileBroker in Python configuration"

if options.fileBrokerHost:
    try:
        process.EvFDaqDirector.fileBrokerHostFromCfg = False
    except:
        print "Unable to set process.EvFDaqDirector.fileBrokerHostFromCfg = True"
    try:
        process.EvFDaqDirector.fileBrokerHost = options.fileBrokerHost
    except:
        print "Unable to set process.EvFDaqDirector.fileBrokerHost =",options.fileBrokerHost

try:
    from HLTrigger.Configuration.customizeHLTforPatatrack import customizeHLTforPatatrack
    process = customizeHLTforPatatrack(process)
except ImportError:
    pass