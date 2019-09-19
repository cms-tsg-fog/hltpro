import FWCore.ParameterSet.Config as cms

process = cms.Process("LHC")


import FWCore.ParameterSet.VarParsing as VarParsing
options = VarParsing.VarParsing ('analysis') 
options.register('firstRun',0,options.multiplicity.singleton,options.varType.int,"pass to firstRun")
options.parseArguments()

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.source = cms.Source("ErrorStreamSource",
#                            fileNames = cms.untracked.vstring("/store/error_stream/run320917/run320917_ls0149_index000167_fu-c2d44-34-03_pid22180.raw"),
                            fileNames = cms.untracked.vstring(options.inputFiles),
                            firstRun  = cms.untracked.uint32(options.firstRun)
                            )


from EventFilter.RawDataCollector.rawDataCollectorByLabel_cfi import rawDataCollector
process.rawDataCollector = rawDataCollector.clone(
        verbose = cms.untracked.int32(0),
            RawCollectionList = cms.VInputTag( cms.InputTag('source') )
        )

process.output = cms.OutputModule( "PoolOutputModule",
#                                   fileName = cms.untracked.string( "file:/cmsnfshltdata/hltdata/TSG/ErrorStream/test.root" ),
                                   fileName = cms.untracked.string(options.outputFile ),
                                   outputCommands = cms.untracked.vstring(
                                                                          'drop *',
                                                                          'keep *_rawDataCollector_*_*'
                                   )
)

process.raw = cms.Path( process.rawDataCollector )
process.end = cms.EndPath( process.output ) 
