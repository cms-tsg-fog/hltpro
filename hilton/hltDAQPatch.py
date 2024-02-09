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

options.register ('runUniqueKey',
                  'InValid', # default value
                  VarParsing.VarParsing.multiplicity.singleton,
                  VarParsing.VarParsing.varType.string,          # string, int, or float
                  "Unique run key from RCMS for Frontier")

options.parseArguments()

process.options.numberOfThreads = options.numThreads
process.options.numberOfStreams = options.numFwkStreams
process.options.numberOfConcurrentLuminosityBlocks = 2

process.EvFDaqDirector.buBaseDir    = options.buBaseDir
process.EvFDaqDirector.baseDir      = options.dataDir
process.EvFDaqDirector.runNumber    = options.runNumber
process.EvFDaqDirector.fileBrokerHost = options.fileBrokerHost
process.EvFDaqDirector.useFileBroker  = True

#parameter will be removed from future releases
try:
    process.EvFDaqDirector.fileBrokerHostFromCfg = False
except:
    print("Unable to set process.EvFDaqDirector.fileBrokerHostFromCfg = False")

#pass transfer mode to the director module for setting stream destinations
try:
    process.EvFDaqDirector.selectedTransferMode = options.transferMode
except:
    print("unable to set process.EvFDaqDirector.selectedTransferMode =", options.transferMode)

#options to override compression algorithm and level for the streamer output
C_LEVEL_UNDEFINED = -1
C_ALGO_UNDEFINED = ""
for moduleName in process.__dict__['_Process__outputmodules']:
    modified_module = getattr(process,moduleName)
    if -1 != C_LEVEL_UNDEFINED:
        modified_module.compression_level=cms.untracked.int32(-1)
    if "" != C_ALGO_UNDEFINED:
        modified_module.compression_algorithm=cms.untracked.string("")

#enable or disable parking depending on the transfer mode
try:
    if options.transferMode.endswith("_NOPARKING"):
        process.hltEnableParking.result = False
    else:
        process.hltEnableParking.result = True
except:
    pass

#unique run key used to create a separate squid cache grouping per run for lumi-based conditions
try:
    process.GlobalTag.frontierKey = cms.untracked.string(options.runUniqueKey)
    print("Set GlobalTag.frontierKey to", options.runUniqueKey)
except:
    print("Unable to set GlobalTag.frontierKey to", options.runUniqueKey)
