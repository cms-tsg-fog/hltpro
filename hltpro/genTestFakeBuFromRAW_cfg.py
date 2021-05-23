import os
import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing

from inputFilesRAW import fileNamesByRun_dict

# fileNamesByRun_dict -> dictionary of input files, key-ed by run number
#   - this dictionary is imported from inputFilesRAW.py (containing specific instructions) 
#
#   - once the dictionary holds the correct information,
#     one can specify the run number from the command line
#     (example: cmsRun genTestFakeBuFromRAW_cfg.py runNumber=X)
#     and the script will pick up the corresponding input files

options = VarParsing.VarParsing('analysis')

options.register ('runNumber', 1,
                  VarParsing.VarParsing.multiplicity.singleton,
                  VarParsing.VarParsing.varType.int,          # string, int, or float
                  "Run Number")

options.register ('buBaseDir',
                  '/fff/BU0', # default value
                  VarParsing.VarParsing.multiplicity.singleton,
                  VarParsing.VarParsing.varType.string,          # string, int, or float
                  "BU base directory")

options.register ('dataDir',
                  '/fff/BU0/ramdisk', # default value (on standalone FU)
                  VarParsing.VarParsing.multiplicity.singleton,
                  VarParsing.VarParsing.varType.string,          # string, int, or float
                  "BU data write directory")

options.parseArguments()

if options.runNumber not in fileNamesByRun_dict:
   log_msg = 'no file-list defined for run='+str(options.runNumber)+' (key '+str(options.runNumber)+' missing in dictionary)'
   log_msg += ' --> modify fileNamesByRun_dict dictionary in genTestFakeBuFromRAW_cfg.py'
   raise SystemExit('\033[1m\033[91m[FATAL] '+log_msg+'\033[0m')

elif len(fileNamesByRun_dict[options.runNumber]) == 0:
   log_msg = 'invalid file-list associated to run='+str(options.runNumber)+' (must be a non-empty list of strings)'
   log_msg += ' --> modify fileNamesByRun_dict dictionary in genTestFakeBuFromRAW_cfg.py'
   raise SystemExit('\033[1m\033[91m[FATAL] '+log_msg+'\033[0m')

# -----------------------------------------------------------------------------------------------------------------

process = cms.Process("FAKEBU")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(400)
    #input = cms.untracked.int32(1000)
    #input = cms.untracked.int32(10000)
)

#process.options = cms.untracked.PSet(
#  multiProcesses = cms.untracked.PSet(
#    maxChildProcesses = cms.untracked.int32(0)
#  )
#)

process.MessageLogger = cms.Service("MessageLogger",
                                    destinations = cms.untracked.vstring( 'cout' ),
                                    cout = cms.untracked.PSet(
    FwkReport = cms.untracked.PSet(
    reportEvery = cms.untracked.int32(-1),
    optionalPSet = cms.untracked.bool(True),
    #limit = cms.untracked.int32(10000000)
    ),
    threshold = cms.untracked.string( "INFO" ),
    )
)

process.source = cms.Source("PoolSource",
  fileNames = cms.untracked.vstring(fileNamesByRun_dict[options.runNumber]),
  skipEvents = cms.untracked.uint32(0),
)

def isPreCMSSW11():
   try:
      import os
      return int(os.environ['CMSSW_VERSION'].split("_")[1])<11
   except:
      print "error trying to get CMSSW version, assuming version >=11"
      return False

if isPreCMSSW11():
   print "setting up DAQ director for CMSSW versions <11"
   process.EvFDaqDirector = cms.Service("EvFDaqDirector",
                                        runNumber= cms.untracked.uint32(options.runNumber),
                                        baseDir = cms.untracked.string(options.dataDir),
                                        buBaseDir = cms.untracked.string("/fff/BU0"),
                                        directorIsBu = cms.untracked.bool(True),
                                        #obsolete:
                                        hltBaseDir = cms.untracked.string("/fff/BU0/ramdisk"),
                                        smBaseDir  = cms.untracked.string("/fff/BU0/ramdisk"),
                                        slaveResources = cms.untracked.vstring('dvfu-c2f37-38-01'),
                                        slavePathToData = cms.untracked.string("/fff/BU/ramdisk")
                                     )
else:
   print "setting up DAQ director for CMSSW versions >=11"
   process.EvFDaqDirector = cms.Service("EvFDaqDirector",
                                        runNumber= cms.untracked.uint32(options.runNumber),
                                        baseDir = cms.untracked.string(options.dataDir),
                                        buBaseDir = cms.untracked.string(options.buBaseDir),
                                        hltSourceDirectory = cms.untracked.string("/tmp/hltpro/hlt/"),
                                        directorIsBU = cms.untracked.bool(True),
                                     )

process.a = cms.EDAnalyzer("ExceptionGenerator",
                           defaultAction = cms.untracked.int32(0),
                           defaultQualifier = cms.untracked.int32(10)
                           )

process.out = cms.OutputModule("RawStreamFileWriterForBU",
    source = cms.InputTag("rawDataCollector"),
    numEventsPerFile = cms.uint32(10),
    frdVersion = cms.uint32(6),
    frdFileVersion = cms.uint32(1)
)

process.p = cms.Path(process.a)

process.ep = cms.EndPath(process.out)
