import FWCore.ParameterSet.Config as cms

# example: cmsRun FRD2RAW.py inputFiles=file:fedraw1.raw,file:fedraw2.raw [outputFile=output.root] [firstRun=0] [firstLS=1] [maxEvents=-1]

process = cms.Process('LHC')

import FWCore.ParameterSet.VarParsing as VarParsing
options = VarParsing.VarParsing ('analysis') 
options.register('firstRun', 0, options.multiplicity.singleton, options.varType.int, 'value passed to process.source.firstRun')
options.register('firstLS', 1, options.multiplicity.singleton, options.varType.int, 'first luminosity block for selected run')
options.parseArguments()

if len(options.inputFiles) == 0:
   raise RuntimeError('empty list of input files (use "inputFiles=..")')

process.maxEvents = cms.untracked.PSet(
  input = cms.untracked.int32(options.maxEvents)
)

process.source = cms.Source('ErrorStreamSource',
  fileNames = cms.untracked.vstring(options.inputFiles),
  firstRun = cms.untracked.uint32(options.firstRun),
  firstLuminosityBlockForEachRun = cms.untracked.VLuminosityBlockID(*[cms.LuminosityBlockID(options.firstLS, options.firstRun)]),
)

from EventFilter.RawDataCollector.rawDataCollectorByLabel_cfi import rawDataCollector
process.rawDataCollector = rawDataCollector.clone(
  verbose = cms.untracked.int32(0),
  RawCollectionList = cms.VInputTag(cms.InputTag('source'))
)

process.output = cms.OutputModule('PoolOutputModule',
  fileName = cms.untracked.string(options.outputFile),
  outputCommands = cms.untracked.vstring(
    'drop *',
    'keep *_rawDataCollector_*_*',
  ),
)

process.raw = cms.Path( process.rawDataCollector )
process.end = cms.EndPath( process.output ) 
