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

}