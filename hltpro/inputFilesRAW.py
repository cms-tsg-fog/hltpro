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
  355134 : [ # 2022 First Run 3 Collisions at 13.6 TeV / ZeroBias
    '/store/data/Run2022B/ZeroBias8/RAW/v1/000/355/134/00000/44286f48-0494-4766-b077-bb573a3e085b.root'
  ],

  355100 : [ # 2022 First Run 3 Collisions at 13.6 TeV / ZeroBias
    '/store/data/Run2022B/ZeroBias/RAW/v1/000/355/100/00000/11c592ae-1b21-44db-8c0c-6dd02f6b64a2.root'
  ],

  353087 : [ # 2022 900 GeV Collisions / MinimumBias
    '/store/data/Run2022A/MinimumBias0/RAW/v1/000/353/087/00000/87be9c0d-1baa-4e31-a454-c0bac953dc27.root'
  ],

  352929 : [ # 2022 900 GeV Collisions / MinimumBias including PPS
    '/store/data/Run2022A/MinimumBias9/RAW/v1/000/352/929/00000/01c1f45d-ed04-472c-8263-4fe58d5c4f43.root'
  ],

  352568 : [ # 2022 900 GeV Collisions / Zero/MinimumBias
    '/store/data/Run2022A/MinimumBias0/RAW/v1/000/352/568/00000/d4dcc6b1-0c5d-4b89-a117-d82fbceec7d1.root'
    #'/store/data/Run2022A/ZeroBias0/RAW/v1/000/352/568/00000/78760484-60c3-49c8-818c-4a9ae589d28f.root'
  ],

  352417 : [ # 2022 900 GeV Collisions / Zero/MinimumBias (Note: HCAL timing scan, so data can not be trusted)
    '/store/data/Run2022A/MinimumBias0/RAW/v1/000/352/417/00000/33f8bcaa-00d6-4ef6-b7b5-c682b1779030.root'
    #'/store/data/Run2022A/ZeroBias0/RAW/v1/000/352/417/00000/20ded97e-4d10-44fc-943d-f9ef05521e35.root'
  ],

  352173 : [ # 2022 900 GeV Collisions (Unstable) / ZeroBias
    '/store/data/Commissioning2022/ZeroBias0/RAW/v1/000/352/173/00000/054f8331-1703-4ce4-b099-428e37f42ff9.root'
  ],
  
  352041 : [ # 2022 CRAFT (L1Menu_Collisions2022_v1_0_1) / Cosmics
    '/store/data/Commissioning2022/Cosmics/RAW/v1/000/352/041/00000/d6b8697a-9e77-436c-b4b7-1317e34e403e.root'
  ],

  347945 : [ # 2022 MWGR1 / Cosmics
    '/store/data/Commissioning2022/Cosmics/RAW/v1/000/347/945/00000/7ee8472c-59e0-469e-972a-a4e191dc500a.root'
  ],

  346512 : [ # 2021 Pilot Beam Test / HLTPhysics (900 GeV Collisions, last run)
    '/store/data/Commissioning2021/HLTPhysics/RAW/v1/000/346/512/00000/9e1384d9-83b8-4240-8486-950fa0e22a77.root'
  ],

  346452 : [ # 2021 Pilot Beam Test / Zero/MinimumBias (900 GeV Collisions)
    '/store/data/Commissioning2021/ZeroBias0/RAW/v1/000/346/452/00000/38409370-1134-4f45-b3be-856633d53f4c.root'
    #'/store/data/Commissioning2021/MinimumBias0/RAW/v1/000/346/452/00000/49591bec-6089-4058-b2e3-399734bd9506.root'
  ],

  345823 : [ # 2021 CRAFT / Cosmics
    '/store/data/Commissioning2021/Cosmics/RAW/v1/000/345/823/00000/06948445-a237-4d8b-91ce-727932458c03.root'
    #'/store/data/Commissioning2021/MinimumBias/RAW/v1/000/345/823/00000/2babeef2-32e9-41f9-906d-db8b43c0aa0f.root' 
  ],

  343171 : [ # 2021 CRUZET / Cosmics
    '/store/data/Commissioning2021/Cosmics/RAW/v1/000/343/171/00000/fd7d4ede-2d31-4011-bea1-489444a23ed4.root',
  ],

  342154 : [ # 2021 MWGR4 / Cosmics
    '/store/data/Commissioning2021/Cosmics/RAW/v1/000/342/154/00000/2b42c3f4-b6d7-444b-9dca-47c2d249dd53.root',
  ],

  341169 : [ # 2021 MWGR3 / Cosmics
    '/store/data/Commissioning2021/Cosmics/RAW/v1/000/341/169/00000/886d4e47-00e3-4ccd-9d2d-a9683622f51b.root',
  ],

  341139 : [ # 2021 MWGR3 / MiniDaq
    '/store/data/Commissioning2021/MiniDaq/RAW/v1/000/341/139/00000/3bdad23c-5e58-4510-a5d9-8b9747ba634b.root',
  ],

  340207 : [ # 2021 MWGR2 / Cosmics
    '/store/data/Commissioning2021/Cosmics/RAW/v1/000/340/207/00000/d7836c50-0aa3-4b46-ae9a-770aa4b87e30.root',
  ],

  339579 : [ # 2021 MWGR1 / Cosmics with displaced muon seeds
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

  335518 : [ # 2020 MWGR1 / VirginRaw
    '/store/data/Commissioning2020/VRRandom0/RAW/v1/000/335/518/00000/8289EA59-260C-1746-B67A-09B96FE73C0A.root',
  ],

  335443 : [ # 2020 MWGR1 / Cosmics
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
