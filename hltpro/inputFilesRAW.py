# inputFilesRAW.py containing the list of input RAW files for Hilton

# fileNamesByRun_dict -> dictionary of input files, key-ed by run number
#   - this dictionary is imported by genTestFakeBuFromRAW_cfg.py
#
#   - this dictionary contains the input files associated to a run number
#         [key] = run number (int)
#       [value] = list of strings fed to process.source.fileNames
#
#   - if you need to analyze a new list of files for run X,
#     add a dictionary entry to fileNamesByRun_dict
#     with key X and the list of input files as value
#
#   - once the dictionary holds the correct information,
#     one can specify the run number from the command line
#     (example: cmsRun genTestFakeBuFromRAW_cfg.py runNumber=X)
#     and the script will pick up the corresponding input files

fileNamesByRun_dict = {

  340207 : [# 2021 MWGR2 / Cosmics
    '/store/data/Commissioning2021/Cosmics/RAW/v1/000/340/207/00000/d7836c50-0aa3-4b46-ae9a-770aa4b87e30.root',
  ],

  339579 : [# 2021 MWGR1 / Cosmics with displaced muon seeds
    '/store/data/Commissioning2021/HLTPhysics/RAW/v1/000/339/579/00000/a26e3078-ac1f-49c3-8a40-e9007fbd1b47.root',
  ],

  338717 : [ # 2020 MWGR4 / Cosmics
    '/store/data/Commissioning2020/Cosmics/RAW/v1/000/338/717/00000/9B97E41C-639B-4A46-8BE8-E45B605442DF.root',
  ],

  337242 : [ # 2020 MWGR3 / Cosmics
    '/store/data/Commissioning2020/Cosmics/RAW/v1/000/337/242/00000/F73C6160-3892-8A42-9EB2-B21F7728025E.root',
  ],

  336435 : [ # 2020 MWGR2 / Cosmics
    '/store/data/Commissioning2020/MinimumBias/RAW/v1/000/336/435/00000/E6E0F0FC-9FCB-4444-AFAF-6159FDD40A86.root',
  ],
  
  335443 : [# 2020 MWGR1 / Cosmics
     '/store/data/Commissioning2020/Cosmics/RAW/v1/000/335/443/00000/81EAE361-0FBA-0B4F-9728-227DE2567C7B.root',
  ],

  334518 : [ # 2020 MWGR0 / VirginRaw
    '/store/data/Commissioning2019/VRRandom3/RAW/v1/000/334/518/00000/18B41CEB-DCF7-BD46-B6BC-0E7E56E7B047.root',
  ],

  334393 : [ # 2020 MWGR0 / Cosmics
    '/store/data/Commissioning2019/HLTPhysics/RAW/v1/000/334/393/00000/E0D10C28-5C45-8147-A967-8FCE150D9514.root',
  ],

  331595 : [ # 2019 MWGR4 / VirginRaw
    '/store/data/Commissioning2019/VRRandom3/RAW/v1/000/331/595/00000/3F49019E-7FA1-9A41-A8DE-418E5AEB988E.root',
  ],

  331483 : [ # 2019 MWGR4 / Cosmics
    '/store/data/Commissioning2019/HLTPhysics/RAW/v1/000/331/483/00000/26C27254-3211-3942-B192-AFC3DB02BF1D.root',
  ],

  330061 : [
    'file:/nfshome0/hltpro/hilton_c2f13_20_04/run330061_ls0136_index000005_fu-c2a03-41-02_pid362895.raw',
  ],

  328788 : [ # Cosmics
    '/store/data/Commissioning2019/HLTPhysics/RAW/v1/000/328/788/00000/F5DC78DF-D593-5E41-8DCF-A02F21A3FC44.root',
  ],

  328691 : [ # VirginRaw
    '/store/data/Commissioning2019/VRRandom3/RAW/v1/000/328/691/00000/00117159-5391-2C49-98CA-949BD0537DD9.root',
  ],

  327237 : [
#    '/store/hidata/HIRun2018A/HITrackerNZS/RAW/v1/000/327/237/00000/EDA529BE-0A15-524D-BFFF-053962A8F3BA.root',
  ],

  326722 : [
#    '/store/hidata/HIRun2018A/HITrackerNZS/RAW/v1/000/326/722/00000/E8909FC5-18C8-A045-B969-C21A7D5E5267.root',
  ],

  326547 : [
#    '/store/group/phys_heavyions/abaty/Nov11_2018PbPbRun_HLTCrashErrorStreams_Run326547/ErrorDump1_run326547.root',
#    '/store/group/phys_heavyions/abaty/Nov11_2018PbPbRun_HLTCrashErrorStreams_Run326547/ErrorDump2_run326547.root',
#    '/store/group/phys_heavyions/abaty/Nov11_2018PbPbRun_HLTCrashErrorStreams_Run326547/ErrorDump6_run326547.root',
#    '/store/group/phys_heavyions/abaty/Nov11_2018PbPbRun_HLTCrashErrorStreams_Run326547/ErrorDump7_run326547.root',
  ],

  326535 : [
#    '/store/hidata/HIRun2018A/HITrackerNZS/RAW/v1/000/326/535/00000/3FCF6037-6E19-684D-B9B8-D92508F2EBCF.root',
  ],

  325273 : [
#    '/store/data/Run2018D/HLTPhysics/RAW/v1/000/325/273/00000/4F73F01B-C309-EF4B-939C-C76D09BC4E52.root',
  ],

  325113 : [
#    '/store/data/Run2018D/EphemeralHLTPhysics1/RAW/v1/000/325/113/00000/9DC7900F-0E07-5245-9271-337D38BD94FB.root',
  ],

  325112 : [
#    '/store/data/Run2018D/HIMinimumBias0/RAW/v1/000/325/112/00000/660F62BB-9932-D645-A4A4-0BBBDA3963E8.root',
  ],

  324420 : [
#    '/store/data/Run2018D/HLTPhysics/RAW/v1/000/324/420/00000/487403ED-6DB3-8241-85A0-3D6EAE21B98E.root',
  ],

  # EGamma starting at lumisection 1
  324970 : [
#    '/store/data/Run2018D/EGamma/RAW/v1/000/324/970/00000/8B3773DB-14EA-9844-BE94-D91404291BB9.root',
#    'file:/cmsnfshltdata/hltdata/TSG/FUVAL_INPUT_FILES/EGamma_Run2018D_324970_LS1_8B3773DB-14EA-9844-BE94-D91404291BB9.root',
     'file:/cmsnfshltdata/hltdata/TSG/FUVAL_INPUT_FILES/EGamma_Run2018D-v1_RAW_Run324970_LS1_numEvent100.root',
     'file:/cmsnfshltdata/hltdata/TSG/FUVAL_INPUT_FILES/EGamma_Run2018D-v1_RAW_Run324970_LS2_numEvent100.root',
     'file:/cmsnfshltdata/hltdata/TSG/FUVAL_INPUT_FILES/EGamma_Run2018D-v1_RAW_Run324970_LS3_numEvent100.root',
     'file:/cmsnfshltdata/hltdata/TSG/FUVAL_INPUT_FILES/EGamma_Run2018D-v1_RAW_Run324970_LS4_numEvent100.root',
     'file:/cmsnfshltdata/hltdata/TSG/FUVAL_INPUT_FILES/EGamma_Run2018D-v1_RAW_Run324970_LS5_numEvent100.root',
     'file:/cmsnfshltdata/hltdata/TSG/FUVAL_INPUT_FILES/EGamma_Run2018D-v1_RAW_Run324970_LS6_numEvent100.root',
     'file:/cmsnfshltdata/hltdata/TSG/FUVAL_INPUT_FILES/EGamma_Run2018D-v1_RAW_Run324970_LS7_numEvent100.root',
     'file:/cmsnfshltdata/hltdata/TSG/FUVAL_INPUT_FILES/EGamma_Run2018D-v1_RAW_Run324970_LS8_numEvent100.root',
     'file:/cmsnfshltdata/hltdata/TSG/FUVAL_INPUT_FILES/EGamma_Run2018D-v1_RAW_Run324970_LS9_numEvent100.root',
     'file:/cmsnfshltdata/hltdata/TSG/FUVAL_INPUT_FILES/EGamma_Run2018D-v1_RAW_Run324970_LS10_numEvent100.root',
     'file:/cmsnfshltdata/hltdata/TSG/FUVAL_INPUT_FILES/EGamma_Run2018D-v1_RAW_Run324970_LS11_numEvent500.root',
  ],

  323778 : [
#    '/store/data/Run2018D/HLTPhysics/RAW/v1/000/323/778/00000/D64468A2-C1A9-BD4A-81BE-EF0287C1B5DE.root',
#    '/store/data/Run2018D/HLTPhysics/RAW/v1/000/323/778/00000/E603254F-3776-DA48-B42C-AE957D98B402.root',
#    '/store/data/Run2018D/HLTPhysics/RAW/v1/000/323/778/00000/E78B79AE-42D4-1142-B8A6-01DD27739012.root',
#    '/store/data/Run2018D/HLTPhysics/RAW/v1/000/323/778/00000/F0938726-EA4E-7340-9824-EF54B059A24F.root',
#    '/store/data/Run2018D/HLTPhysics/RAW/v1/000/323/778/00000/F3B99342-F73F-D749-84FA-CFEFE24D6808.root',
  ],

  320917 : [
#    'file:/nfshome0/hltpro/sam/CMSSW_10_1_9_patch1/src/run320917_ls0149_index000167_fu-c2d44-34-03_pid22180_RAW.root',
#    'file:/store/error_stream/run320917/run320917_ls0149_index000167_fu-c2d44-34-03_pid22180.raw',
  ],

  320068 : [
#    '/store/data/Run2018C/Cosmics/RAW/v1/000/320/068/00000/148CE1DF-348E-E811-97DA-FA163EEA1BCB.root',
#    '/store/data/Run2018C/Cosmics/RAW/v1/000/320/068/00000/2E4FD074-3D8E-E811-8D87-FA163EDE3448.root',
  ],

  320058 : [
#    '/store/data/Run2018C/HLTPhysics/RAW/v1/000/320/058/00000/18188A2B-E88D-E811-AB9D-02163E0147E0.root',
  ],

  320033 : [
#    '/store/data/Run2018C/HLTPhysics/RAW/v1/000/320/033/00000/D2BEC630-878D-E811-9258-FA163E591793.root',
#    '/store/data/Run2018C/HLTPhysics/RAW/v1/000/320/033/00000/D8F827E8-888D-E811-8DDD-FA163E9CA9FB.root',
  ],

  319756 : [
#    '/store/data/Run2018C/HLTPhysics/RAW/v1/000/319/756/00000/FE975FEF-6589-E811-8AD5-FA163E3EB9DB.root',
  ],

  319176 : [ # TOTEM ZeroBias
#    '/store/data/Run2018B/ZeroBiasTOTEM1/RAW/v1/000/319/176/00000/6E38E640-F67E-E811-8077-FA163E13F978.root',
  ],

  319077 : [
#    '/store/data/Run2018B/HLTPhysics/RAW/v1/000/319/077/00000/3E3BAA26-8F7D-E811-A910-FA163EA89334.root',
  ],

  318945 : [
#    '/store/data/Run2018B/HighMultiplicityEOF/RAW/v1/000/318/945/00000/D8A0B196-C97B-E811-9FC4-FA163EA60C9D.root',
  ],

  318817 : [
#    '/store/data/Run2018B/ZeroBias1/RAW/v1/000/318/817/00000/F2ADC11A-5B7A-E811-A5AB-FA163EF075B3.root', # ZeroBias from BSRT scan end of June
#    '/store/data/Run2018B/AlCaLumiPixels2/RAW/v1/000/318/817/00000/A8AEFBF9-717A-E811-B7E0-FA163EC03988.root', # AlCaLumiPixels2 from BSRT end of June
  ],

  318712 : [
#    '/store/data/Run2018B/ZeroBias/RAW/v1/000/318/712/00000/500DE39E-8F79-E811-83F8-FA163EE9B4D4.root',
#    '/store/data/Run2018B/HighMultiplicityEOF/RAW/v1/000/318/712/00000/480CC86B-0E7A-E811-8289-FA163E0286FE.root',
  ],

  316380 : [
#    'file:/cmsnfshltdata/hltdata/TSG/FUVAL_INPUT_FILES/SingleMuon_Run2018A_316380_LS100.root',
#    'file:/cmsnfshltdata/hltdata/TSG/FUVAL_INPUT_FILES/EGamma_Run2018A_316380_LS101.root',
#    'file:/cmsnfshltdata/hltdata/TSG/FUVAL_INPUT_FILES/JetHT_Run2018A_316380_LS102.root',
#    'file:/cmsnfshltdata/hltdata/TSG/FUVAL_INPUT_FILES/MET_Run2018A_316380_LS103.root',
#    'file:/cmsnfshltdata/hltdata/TSG/FUVAL_INPUT_FILES/MuOnia_Run2018A_316380_LS104.root',
#
#    '/store/data/Run2018A/ZeroBias/RAW/v1/000/316/380/00000/B026B33C-C458-E811-852B-FA163E87B8EE.root',
#    '/store/data/Run2018A/HLTPhysics/RAW/v1/000/316/380/00000/00B33F0D-DB58-E811-A48A-02163E019F0F.root',
#    '/store/data/Run2018A/HLTPhysics/RAW/v1/000/316/380/00000/06B76EDA-E358-E811-89EF-FA163E36E829.root',
#    '/store/data/Run2018A/HLTPhysics/RAW/v1/000/316/380/00000/0C0BAD04-E058-E811-BFB6-02163E012ED7.root',
#    '/store/data/Run2018A/HLTPhysics/RAW/v1/000/316/380/00000/1403BE1D-C558-E811-8995-FA163E2628C1.root',
#    '/store/data/Run2018A/HLTPhysics/RAW/v1/000/316/380/00000/1892329A-F058-E811-91F1-FA163ED6DF53.root',
#    '/store/data/Run2018A/HLTPhysics/RAW/v1/000/316/380/00000/282D8527-C558-E811-BE22-FA163EBE7D37.root',
#    '/store/data/Run2018A/HLTPhysics/RAW/v1/000/316/380/00000/30E64488-F758-E811-BA91-FA163EEFBF2A.root',
#    '/store/data/Run2018A/HLTPhysics/RAW/v1/000/316/380/00000/32D8E849-D058-E811-A336-FA163EDC9ED5.root',
#    '/store/data/Run2018A/HLTPhysics/RAW/v1/000/316/380/00000/34EEB29E-E458-E811-A80E-FA163E816F3E.root',
#    '/store/data/Run2018A/HLTPhysics/RAW/v1/000/316/380/00000/4C720BB6-EC58-E811-ABBD-FA163ECD3FFB.root',
#    '/store/data/Run2018A/HLTPhysics/RAW/v1/000/316/380/00000/5EE4E1EA-FD58-E811-938C-FA163EF44C5F.root',
#    '/store/data/Run2018A/HLTPhysics/RAW/v1/000/316/380/00000/6870852E-FE58-E811-A0D6-FA163E591793.root',
#    '/store/data/Run2018A/HLTPhysics/RAW/v1/000/316/380/00000/6CC81E4E-D058-E811-A79E-FA163E8ECDD2.root',
#    '/store/data/Run2018A/HLTPhysics/RAW/v1/000/316/380/00000/72F7B2D9-DA58-E811-9414-FA163EBDD80B.root',
  ],

  316187 : [
#    'file:/cmsnfshltdata/hltdata/TSG/ErrorStream/run316187_LS641_ErrorStream_RAW.root',
#    'file:/cmsnfshltdata/hltdata/TSG/ErrorStream/run316187_LS642_ErrorStream_RAW.root',
  ],

# other inputs (run number not specified)
#  '/store/group/phys_exotica/HNL/74AB8BD0-9379-E811-A0C0-02163E017FD1.root',
#  'file:/cmsnfsscratch/globalscratch/hltpro/step1_DIGI_L1_DIGI2RAW_HLT_49.root',
#  'file:/cmsnfsscratch/globalscratch/hltpro/FEF52EFA-D5AF-E711-AD18-02163E0142DA.root',
}
