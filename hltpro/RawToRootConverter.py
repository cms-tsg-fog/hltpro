import FWCore.ParameterSet.Config as cms

process = cms.Process("LHC")
import FWCore.ParameterSet.VarParsing as VarParsing
options = VarParsing.VarParsing ('analysis') 
options.parseArguments()

if len(options.inputFiles)<1:
    raise Exception("Please insert an inputFile. Eg. cmsRun RawToRootConverter.py inputFiles=/store/error_stream/run356997/run356997_ls0142_index000229_fu-c2b03-37-01_pid3478586.raw outputFile=outputFile.root")

if len(options.inputFiles)>1:
    raise Exception("Please insert only one inputFile")

file_ = options.inputFiles[0]
if "run" in file_ and "_ls" in file_:
    run = int(file_.split("run")[-1].split("_ls")[0])
else:
    raise Exception("%s has not the format [...]runNNNNNN_ls[...]")

process.source = cms.Source("ErrorStreamSource",
                            fileNames = cms.untracked.vstring(options.inputFiles),
                            firstRun  = cms.untracked.uint32(run),
                            firstLuminosityBlockForEachRun = cms.untracked.VLuminosityBlockID([])
                            )

from EventFilter.RawDataCollector.rawDataCollectorByLabel_cfi import rawDataCollector
process.rawDataCollector = rawDataCollector.clone(
        verbose = cms.untracked.int32(0),
            RawCollectionList = cms.VInputTag( cms.InputTag('source') )
        )

process.output = cms.OutputModule( "PoolOutputModule",
                                   fileName = cms.untracked.string( options.outputFile ),
                                   outputCommands = cms.untracked.vstring(
'drop *',
'keep *_rawDataCollector_*_*'
                                   )
)

process.raw = cms.Path( process.rawDataCollector )
process.end = cms.EndPath( process.output )

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32( -1 )
)
