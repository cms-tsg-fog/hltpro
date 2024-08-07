# required event contents for different menu types

import copy
full = [
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*',
        'keep FEDRawDataCollection_rawDataCollector_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep triggerTriggerEvent_*_*_*']

# core content
core_content = {
        'A': full,

        'B': full,

        'AlcaPi0': [
          'keep *_hltAlCaEtaEBUncalibrator_*_*',
          'keep *_hltAlCaEtaEEUncalibrator_*_*',
          'keep *_hltAlCaEtaRecHitsFilterEEonly_etaEcalRecHitsES_*',
          'keep *_hltAlCaPi0EBUncalibrator_*_*',
          'keep *_hltAlCaPi0EEUncalibrator_*_*',
          'keep *_hltAlCaPi0RecHitsFilterEEonly_pi0EcalRecHitsES_*',
          'keep *_hltGtStage2Digis_*_*',
          'keep edmTriggerResults_*_*_*'],

        'AlcaPhiSym': [
          'keep *_hltAlCaPhiSymUncalibrator_*_*',
          'keep *_hltGtStage2Digis_*_*',
          'keep edmTriggerResults_*_*_*',
          'keep triggerTriggerEvent_*_*_*'],

        'AlcaLumiPixel': [
          'keep *_hltFEDSelectorLumiPixels_*_*',
          'keep *_hltGtStage2Digis_*_*',
          'keep edmTriggerResults_*_*_*'],

       'Calibration': [
          'keep *_hltEcalCalibrationRaw_*_*',
          'keep *_hltHcalCalibrationRaw_*_*',
          'keep edmTriggerResults_*_*_*',
          'keep triggerTriggerEvent_*_*_*'],

        'DQMOnlineBeamspot': [
          'keep *_hltFEDSelectorTCDS_*_*',
          'keep edmTriggerResults_*_*_*'],

        'DQM_PA': full,

        'EcalCalibration': [
          'keep *_hltEcalCalibrationRaw_*_*',
          'keep edmTriggerResults_*_*_*',
          'keep triggerTriggerEvent_*_*_*'],

        'Express': full,

        'HLTDQM': [
          'keep *_hltTriggerSummaryAOD_*_*',
          'keep DcsStatuss_hltScalersRawToDigi_*_*',
          'keep *_hltGtStage2Digis_*_*',
          'keep LumiScalerss_hltScalersRawToDigi_*_*',
          'keep edmTriggerResults_*_*_*'],

        'NanoDST': [
          'keep *_hltFEDSelectorTCDS_*_*',
          'keep *_hltFEDSelectorL1_*_*',
          'keep edmTriggerResults_*_*_*'],

        'PhysicsDST': [
          'keep *_hltActivityPhotonClusterShape_*_*',
          'keep *_hltActivityPhotonEcalIso_*_*',
          'keep *_hltActivityPhotonHcalForHE_*_*',
          'keep *_hltActivityPhotonHcalIso_*_*',
          'keep *_hltCaloJetIDPassed_*_*',
          'keep *_hltElectronActivityDetaDphi_*_*',
          'keep *_hltHitElectronActivityTrackIsol_*_*',
          'keep *_hltKT6CaloJets_rho*_*',
          'keep *_hltL3MuonCandidates_*_*',
          'keep *_hltL3MuonCombRelIsolations_*_*',
          'keep *_hltMetClean_*_*',
          'keep *_hltMet_*_*',
          'keep *_hltPixelMatchElectronsActivity_*_*',
          'keep *_hltPixelVertices_*_*',
          'keep *_hltRecoEcalSuperClusterActivityCandidate_*_*',
          'keep *_hltGtStage2Digis_*_*',
          'keep edmTriggerResults_*_*_*'],

        'RPCMON': [
          'keep edmTriggerResults_*_*_*',
          'keep triggerTriggerEvent_*_*_*',
          'keep *_hltFEDSelectorTCDS_*_*',
          'keep *_hltFEDSelectorGEM_*_*'],

        'TrackerCalibration': [
          'keep *_hltTrackerCalibrationRaw_*_*',
          'keep edmTriggerResults_*_*_*',
          'keep triggerTriggerEvent_*_*_*'],

        'DQM': [
          'keep *_hltOnlineBeamSpot_*_*',
          'keep *_hltPixelTracks_*_*',
          'keep *_hltSiPixelClusters_*_*',
          'keep *_hltTrimmedPixelVertices_*_*',               # from CMSHLT-3274 (core or extra?)
          'keep *_hltEgammaGsfTracks_*_*',                    # from CMSHLT-3274 (core or extra?)
          'keep *_hltGlbTrkMuonCandsNoVtx_*_*',               # from CMSHLT-3274 (core or extra?)
          'keep *_hltVerticesPFFilter_*_*',                   # from CMSHLT-3274 (core or extra?)
          'keep *_hltIter0PFlowTrackSelectionHighPurity_*_*', # from CMSHLT-3274 (core or extra?)
          'keep *_hltIter0PFlowCtfWithMaterialTracks_*_*',    # from CMSHLT-3274 (core or extra?)
          'keep FEDRawDataCollection_rawDataCollector_*_*',
          'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*',
          'keep edmTriggerResults_*_*_*',
          'keep triggerTriggerEvent_*_*_*'],
        }

# extra content
extra_content = {}

extra_content['collisions'] = {
        'DQM': [
          'keep *_hltL3NoFiltersNoVtxMuonCandidates_*_*',
          'keep *_hltSiStripRawToClustersFacility_*_*',
          'keep *_hltHoreco_*_*',
          'keep *_hltHfreco_*_*',
          'keep *_hltHbhereco_*_*',
          'keep *_hltEcalRecHit_*_*',
          'keep *_hltEgammaCandidates_*_*',
          'keep *_hltPixelVertices_*_*',
          'keep *_hltMergedTracks_*_*'],

        'DQMOnlineBeamspot': [
          'keep recoTracks_hltPFMuonMerging_*_*',
          'keep recoVertexs_hltVerticesPFFilter_*_*',
          'keep *_hltFEDSelectorOnlineMetaData_*_*'],
       }

extra_content['collisionsHI'] = {
        'DQM': [
          'keep *_hltL3NoFiltersNoVtxMuonCandidates_*_*',
          'keep *_hltSiStripRawToClustersFacility_*_*',
          'keep *_hltHoreco_*_*',
          'keep *_hltHfreco_*_*',
          'keep *_hltHbhereco_*_*',
          'keep *_hltEcalRecHit_*_*',
          'keep *_hltEgammaCandidates_*_*',
          'keep *_hltPixelVertices_*_*',
          'keep *_hltMergedTracks_*_*',

          # new for HI
          'keep *_hltSiStripClusterizerForRawPrime_*_*',
          'keep *_hltSiStripClusters2ApproxClusters_*_*',
          'keep FEDRawDataCollection_rawDataRepacker_*_*',
          'keep DetIds_hltSiStripRawToDigi_*_*',
          'keep *_hltSiStripClusters2ApproxClusters_*_*'],

        'DQMOnlineBeamspot': [
          'keep recoVertexs_hltVerticesPFFilterPPOnAA_*_*', # new for HI
          'keep recoTracks_hltPFMuonMergingPPOnAA_*_*', # new for HI
          'keep *_hltFEDSelectorOnlineMetaData_*_*'],
       }

extra_content['cosmics'] = {
        'DQMOnlineBeamspot': [
          'keep recoTracks_hltPFMuonMerging_*_*',
          'keep recoVertexs_hltVerticesPFFilter_*_*'],
}

# final event content
event_content = {}

for menuType in ['collisions', 'collisionsHI', 'cosmics']: 
    event_content[menuType] = {key:core_content.get(key,[]) + extra_content[menuType].get(key,[]) for key in set(list(core_content.keys()) + list(extra_content[menuType].keys()))}

event_content['circulating'] = event_content['cosmics']
