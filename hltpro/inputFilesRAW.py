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
    366043 :    
        '/store/data/Run2023A/EphemeralZeroBias0/RAW/v1/000/366/043/00000/d5d15bdb-780a-444e-b9fb-7f2a9080ef4f.root',                           
        '/store/data/Run2023A/EphemeralZeroBias0/RAW/v1/000/366/043/00000/5f470ec3-fa59-4c52-8b84-f9aec268b9ae.root',                           
        '/store/data/Run2023A/EphemeralZeroBias0/RAW/v1/000/366/043/00000/187f40e0-fe10-44bf-9f14-96c138ffbad8.root',                           
    ],                                                                                                                                          
    366035 : [  # Run2023A, 900 GeV stable beams -- the "good run"                                                                                                                                
        '/store/data/Run2023A/EphemeralZeroBias0/RAW/v1/000/366/035/00000/cf091ae2-578b-4053-9314-71b77e88d125.root',                           
        '/store/data/Run2023A/EphemeralZeroBias0/RAW/v1/000/366/035/00000/cf25cf47-2412-4a34-859f-f0f58bcc0b26.root',                           
        '/store/data/Run2023A/EphemeralZeroBias0/RAW/v1/000/366/035/00000/cfc33005-4f1a-4f19-aa7c-8893d2783514.root',                           
    ],
    365844 : [  # Run2023A, EphemeralZeroBias0, first 38 files (more available)                                                                 
        '/store/data/Run2023A/EphemeralZeroBias0/RAW/v1/000/365/844/00000/0095f8e8-51d6-4f04-b6bf-ff983967bc1f.root',                           
        '/store/data/Run2023A/EphemeralZeroBias0/RAW/v1/000/365/844/00000/01129298-228a-471f-b174-1676de24c90f.root',                           
        '/store/data/Run2023A/EphemeralZeroBias0/RAW/v1/000/365/844/00000/011432d8-e477-4760-a12a-e3d6eda24218.root',                           
        '/store/data/Run2023A/EphemeralZeroBias0/RAW/v1/000/365/844/00000/016aa5b9-43c4-4608-8d35-d3e7dcb7caec.root',                           
        '/store/data/Run2023A/EphemeralZeroBias0/RAW/v1/000/365/844/00000/01abe8b9-f7db-42d3-8e18-79ab73a00f7a.root',                           
        '/store/data/Run2023A/EphemeralZeroBias0/RAW/v1/000/365/844/00000/01e43583-0d23-4bc7-aa1c-d7758776e47b.root',                           
        '/store/data/Run2023A/EphemeralZeroBias0/RAW/v1/000/365/844/00000/01eea7d9-00e7-4445-ae14-efa973f2e50e.root',                           
        '/store/data/Run2023A/EphemeralZeroBias0/RAW/v1/000/365/844/00000/022f9068-1705-4232-be2e-db9a330b23d9.root',                           
        '/store/data/Run2023A/EphemeralZeroBias0/RAW/v1/000/365/844/00000/026c83f8-743d-472c-9f60-77d108884834.root',                           
        '/store/data/Run2023A/EphemeralZeroBias0/RAW/v1/000/365/844/00000/02dfe14f-e62d-4bbf-a9f9-f3b17ba43790.root',                           
        '/store/data/Run2023A/EphemeralZeroBias0/RAW/v1/000/365/844/00000/02f57797-97c8-4e79-89c3-c2693e9175c5.root',                           
        '/store/data/Run2023A/EphemeralZeroBias0/RAW/v1/000/365/844/00000/03168628-3f20-4305-84b4-08929a8bbb5a.root', 
        '/store/data/Run2023A/EphemeralZeroBias0/RAW/v1/000/365/844/00000/032290d6-6032-41c3-8814-de721f86653d.root',                           
        '/store/data/Run2023A/EphemeralZeroBias0/RAW/v1/000/365/844/00000/03d86d0b-3300-412b-844b-8bc0ac18ffdc.root',                           
        '/store/data/Run2023A/EphemeralZeroBias0/RAW/v1/000/365/844/00000/040a5acf-d9a9-47e8-9aae-59c2aba93687.root',                           
        '/store/data/Run2023A/EphemeralZeroBias0/RAW/v1/000/365/844/00000/0438c840-c18b-4173-8ad3-f847105a8159.root',                           
        '/store/data/Run2023A/EphemeralZeroBias0/RAW/v1/000/365/844/00000/04d57685-790f-433c-a98a-0613aa4ee038.root',                           
        '/store/data/Run2023A/EphemeralZeroBias0/RAW/v1/000/365/844/00000/054000cc-642f-466d-bc93-62d32b84274c.root',                           
        '/store/data/Run2023A/EphemeralZeroBias0/RAW/v1/000/365/844/00000/05ce823b-5fcb-4eec-a054-5132d672b2bb.root',
        '/store/data/Run2023A/EphemeralZeroBias0/RAW/v1/000/365/844/00000/0629ac9f-7f22-4f1c-9ad0-caacd88aee6c.root',                                                                                                                      
        '/store/data/Run2023A/EphemeralZeroBias0/RAW/v1/000/365/844/00000/0652d8f5-3bca-4eb0-997d-83539b697e33.root',                                                                                                                      
        '/store/data/Run2023A/EphemeralZeroBias0/RAW/v1/000/365/844/00000/0665af9c-81cb-489c-ae08-f3de3a936176.root',                                                                                                                      
        '/store/data/Run2023A/EphemeralZeroBias0/RAW/v1/000/365/844/00000/06ac3c39-376d-420d-b91d-a75134dfcba5.root',                                                                                                                      
        '/store/data/Run2023A/EphemeralZeroBias0/RAW/v1/000/365/844/00000/06c1b0d7-fa8c-4d06-9520-99535661c17f.root',                                                                                                                      
        '/store/data/Run2023A/EphemeralZeroBias0/RAW/v1/000/365/844/00000/06cc1e34-9254-46e2-aa1d-5f032472b9ba.root',                                                                                                                      
        '/store/data/Run2023A/EphemeralZeroBias0/RAW/v1/000/365/844/00000/06de5b78-38df-470d-98af-6cd95a2b021f.root',                                                                                                                      
        '/store/data/Run2023A/EphemeralZeroBias0/RAW/v1/000/365/844/00000/072e9ace-ef16-48c1-aade-5103dc4977bd.root',                                                                                                                      
        '/store/data/Run2023A/EphemeralZeroBias0/RAW/v1/000/365/844/00000/0736b080-ea73-4f36-a5b5-dc492d023331.root',                                                                                                                      
        '/store/data/Run2023A/EphemeralZeroBias0/RAW/v1/000/365/844/00000/0736ed1a-4a2a-4e2f-bd24-e0f5fdb579f9.root',                                                                                                                      
        '/store/data/Run2023A/EphemeralZeroBias0/RAW/v1/000/365/844/00000/07c39d9f-b2f5-4284-84d5-9179595af33f.root',                                                                                                                      
        '/store/data/Run2023A/EphemeralZeroBias0/RAW/v1/000/365/844/00000/081e1e74-d26f-43ec-8683-7062c326e128.root',                                                                                                                      
        '/store/data/Run2023A/EphemeralZeroBias0/RAW/v1/000/365/844/00000/083c85a6-bd8d-4ec2-b5f0-64615f4b0bb2.root',                                                                                                                      
        '/store/data/Run2023A/EphemeralZeroBias0/RAW/v1/000/365/844/00000/08b6c022-674f-4d58-8451-cf8c527d8da2.root',                                                                                                                      
        '/store/data/Run2023A/EphemeralZeroBias0/RAW/v1/000/365/844/00000/08d47865-5398-46f7-a470-d5934e7e3b0f.root',                                                                                                                      
        '/store/data/Run2023A/EphemeralZeroBias0/RAW/v1/000/365/844/00000/090170ef-8ae5-4cd5-b1da-7e38bd0a43e2.root',                                                                                                                      
        '/store/data/Run2023A/EphemeralZeroBias0/RAW/v1/000/365/844/00000/09117e0d-8fbe-4d80-977d-6bb34cf3f060.root',                                                                                                                      
        '/store/data/Run2023A/EphemeralZeroBias0/RAW/v1/000/365/844/00000/09370205-48e2-4057-8f45-bd6109e92a7a.root',                                                                                                                      
        '/store/data/Run2023A/EphemeralZeroBias0/RAW/v1/000/365/844/00000/09b9e0fb-db7b-497f-aac8-841a94dcc0ca.root',   
    364997 : [
        '/store/data/Commissioning2023/Cosmics/RAW/v2/000/364/997/00000/3013b9b9-bafd-4de2-98f3-74424cbd47aa.root',
    ],
    363862 : [
        '/store/data/Commissioning2023/Cosmics/RAW/v1/000/363/862/00000/8df101a9-b057-419d-93a4-06acd15d9f14.root',
    ],
    363833: [  # MWGR 2 2023 - overnight run
        '/store/data/Commissioning2023/Cosmics/RAW/v1/000/363/833/00000/b949e1a7-935d-4ecf-9ee2-084ac67dd3bd.root',
        '/store/data/Commissioning2023/Cosmics/RAW/v1/000/363/833/00000/bbe32f6e-8934-43e0-a29b-8371785882fb.root',
    ],
    362047:[
        '/store/data/Run2022F/Cosmics/RAW/v1/000/362/047/00000/20543d76-a962-41e9-bf6a-5a870707527a.root',
    ],
    361468: [  # EphemeralHLTPhysics, Run2022F
        '/store/data/Run2022F/EphemeralHLTPhysics0/RAW/v1/000/361/468/00000/00095ea5-792d-461a-93cb-0a44f9bfe98e.root',
        '/store/data/Run2022F/EphemeralHLTPhysics0/RAW/v1/000/361/468/00000/01ffc938-4a3c-4fcf-9f47-2bb40c3771dc.root',
        '/store/data/Run2022F/EphemeralHLTPhysics0/RAW/v1/000/361/468/00000/027756cb-aa30-44d8-9fac-c2fe0d7b13ac.root',
        '/store/data/Run2022F/EphemeralHLTPhysics0/RAW/v1/000/361/468/00000/02a81112-ba83-4147-9f29-c2b9acf7eab0.root',
        '/store/data/Run2022F/EphemeralHLTPhysics0/RAW/v1/000/361/468/00000/0315dc51-0b9f-4bb4-9b92-0129a8baa4f1.root',
        '/store/data/Run2022F/EphemeralHLTPhysics0/RAW/v1/000/361/468/00000/03c55102-b310-45d9-ae08-4ab1f6f406dd.root'
    ],
    360486: [  # EphemeralHLTPhysics, Run2022F
        '/store/data/Run2022F/EphemeralHLTPhysics0/RAW/v1/000/360/486/00000/0005c702-fdc5-4bc3-bfff-20792954febb.root',
        '/store/data/Run2022F/EphemeralHLTPhysics0/RAW/v1/000/360/486/00000/00157acc-957e-4227-bd20-cf52e76045da.root',
        '/store/data/Run2022F/EphemeralHLTPhysics0/RAW/v1/000/360/486/00000/088a51e9-8013-41a9-afe1-2d3f5696e914.root',
        '/store/data/Run2022F/EphemeralHLTPhysics0/RAW/v1/000/360/486/00000/0bdde5c9-9a5f-401a-bfa2-fb22c0b5bd7a.root',
        '/store/data/Run2022F/EphemeralHLTPhysics0/RAW/v1/000/360/486/00000/0eec72fa-e5ba-4167-9ba5-8655025e1ce6.root',
        '/store/data/Run2022F/EphemeralHLTPhysics0/RAW/v1/000/360/486/00000/13a8a77c-26fa-493d-a8a4-478f6a5eeb36.root'
    ],
    360991: [  # EphemeralHLTPhysics, Run2022F, PU~70
        '/store/data/Run2022F/HLTPhysics/RAW/v1/000/360/991/00000/69592673-b357-4478-b6c8-fb4fb2bcb980.root'
    ],
    360761: [  # HLTPhysics Run2022F
        '/store/data/Run2022F/HLTPhysics/RAW/v1/000/360/761/00000/355543ab-c208-455a-8b23-304c769cfc62.root'
    ],
    360336: [  # Cosmics, Run 2022F
        '/store/data/Run2022F/Cosmics/RAW/v1/000/360/336/00000/46f2579c-3df9-4cff-a2b4-8131fa671384.root'
    ],
    360295: [  # HLTPhysics
        '/store/data/Run2022E/HLTPhysics/RAW/v1/000/360/295/00000/586c0988-05cf-4d74-b283-be2bbc80f9f2.root'
    ],
    360225: [  # HLTPhysics
        '/store/data/Run2022E/HLTPhysics/RAW/v1/000/360/225/00000/0311b0e9-3d05-4017-9e48-ff6e6862612c.root'
    ],
    360019: [  # HLTPhysics 2400b PU~50 for FastTrackValidation test
        '/store/data/Run2022E/HLTPhysics/RAW/v1/000/360/019/00000/081e9328-45ff-4d11-b1f7-c97a0e9ec4ed.root'
    ],
    359694: [
        'file:/cmsnfshome0/nfshome0/hltpro/hilton_c2b02_44_01/hltpro/samScratch/run359694_ls0609.root'
    ],
    359686: [  # HLTPhysics only for FastTrackValidation test
        '/store/data/Run2022E/HLTPhysics/RAW/v1/000/359/686/00000/062f8a76-74e8-4e9d-be29-d0e87facf09c.root'
    ],
    357735: [
        '/store/data/Run2022D/ZeroBias/RAW/v1/000/357/735/00000/03e2d5bb-efac-4b56-8149-fbe68152c9c3.root'
    ],
    357542: [  # HLTPhysics 2400b
        '/store/data/Run2022D/EphemeralHLTPhysics6/RAW/v1/000/357/542/00000/004e561f-17bd-48ae-915c-33589bc0e4eb.root'
    ],
    357271: [  # HLTPhysics PU~55 2100b - L1Menu_2022_v1_3_0
        '/store/data/Run2022C/EphemeralHLTPhysics19/RAW/v1/000/357/271/00000/d75a3a15-fbb2-49c4-96ff-dbc3d4fafd12.root'
    ],
    356378: [  # 2022 EphemeralHLTPhysics
        '/store/data/Run2022C/EphemeralHLTPhysics0/RAW/v1/000/356/378/00000/026d6b6b-66b9-462c-b09e-11ef309ccbea.root'
    ],
    355991: [  # EphemeralHLTPhysics, 600 bunches, many L1 seeds where active and with PU~55
        '/store/data/Run2022C/EphemeralHLTPhysics19/RAW/v1/000/355/991/00000/15d87e6c-f718-454b-9fc6-d3073f98e630.root'
    ],
    355680: [  # 2022 Run-3 Collisions at 13.6 TeV / 300 bunches
        '/store/data/Run2022B/HLTPhysics/RAW/v1/000/355/680/00000/0007173a-9858-48b8-bf0d-fab29dce5796.root'
    ],
    355640: [
        '/store/data/Run2022B/MinimumBias/RAW/v1/000/355/640/00000/86792ce8-605f-48d1-949c-ddbdbaf5a7d4.root'
    ],
    355404: [  # 2022 First HLTPhysics, 62b
        '/store/data/Run2022B/HLTPhysics/RAW/v1/000/355/404/00000/8ed34947-7e72-4fe7-906d-90cc77b18fa3.root '
    ],
    355134: [  # 2022 First Run 3 Collisions at 13.6 TeV / ZeroBias
        '/store/data/Run2022B/ZeroBias8/RAW/v1/000/355/134/00000/44286f48-0494-4766-b077-bb573a3e085b.root'
    ],
    355101: [  # GPU Test
        '/store/data/Run2022B/MinimumBias/RAW/v1/000/355/101/00000/28feacdf-d021-42f6-acbb-91be363959b5.root',
        '/store/data/Run2022B/HLTPhysics/RAW/v1/000/355/101/00000/14310f7a-0c8a-4677-b87d-849783956a01.root',
        #'/store/data/Run2022B/TestEnablesEcalHcal/RAW/Express-v1/000/355/101/00000/42b8cf63-d089-4413-af59-3b0e4d143327.root',
        #'/store/data/Run2022B/AlCaLumiPixelsCountsPrompt/RAW/v1/000/355/101/00000/d22ab2aa-ec4b-402a-83e9-648e5041ef26.root',
        #'/store/data/Run2022B/AlCaPhiSym/RAW/v1/000/355/101/00000/ff93450f-09ba-4448-bc3a-c3e8cbf867c6.root',
        #'/store/data/Run2022B/AlCaPhiSym/RAW/v1/000/355/101/00000/a4ac511c-7ebb-45d4-81dc-fcbfa2d1f6cf.root',
        #'/store/data/Run2022B/AlCaPhiSym/RAW/v1/000/355/101/00000/b86ad64d-7485-42ac-a3f8-7ebc9a5eb92a.root',
        #'/store/data/Run2022B/AlCaPhiSym/RAW/v1/000/355/101/00000/4ab85c76-3964-4722-85d6-f0d361cd9531.root',
        #'/store/data/Run2022B/AlCaP0/RAW/v1/000/355/101/00000/eb6191c6-725f-44f5-b6b4-4eaa0ca63165.root',
        #'/store/data/Run2022B/L1Accept/RAW/v1/000/355/101/00000/90c1e8a2-dd0d-4141-ab4c-411197cbe1e1.root',
        #'/store/data/Run2022B/L1Accept/RAW/v1/000/355/101/00000/a31bc5e4-e7eb-4b12-a81a-e6cc6eda4934.root',
        #'/store/data/Run2022B/L1Accept/RAW/v1/000/355/101/00000/f946c7b0-aced-4026-aa93-b94b7b752a25.root',
        #'/store/data/Run2022B/L1Accept/RAW/v1/000/355/101/00000/321f511f-a317-406d-b738-c8c9122abe34.root',
        '/store/data/Run2022B/ZeroBias0/RAW/v1/000/355/101/00000/ffce1815-4065-47d4-bdfb-83789f220a9d.root',
        '/store/data/Run2022B/ZeroBias0/RAW/v1/000/355/101/00000/29490308-0822-4425-8274-2e64e91394f2.root',
        '/store/data/Run2022B/ZeroBias0/RAW/v1/000/355/101/00000/f13c2797-acf4-47a1-abb2-ef298d2eceb2.root',
        '/store/data/Run2022B/ZeroBias0/RAW/v1/000/355/101/00000/bcbba366-a752-4258-a215-21640d783e13.root',
        '/store/data/Run2022B/ZeroBias0/RAW/v1/000/355/101/00000/4c133cb3-e848-47dd-b824-fc272ce2b96c.root',
        '/store/data/Run2022B/ZeroBias0/RAW/v1/000/355/101/00000/126a8323-0f67-40b8-a56c-4b38eea4900b.root',
        '/store/data/Run2022B/ZeroBias0/RAW/v1/000/355/101/00000/9060c870-2a67-434b-a593-809b97a0a9bb.root',
        '/store/data/Run2022B/ZeroBias0/RAW/v1/000/355/101/00000/4d957488-0544-4a5e-a152-ee5837f407fb.root',
        '/store/data/Run2022B/ZeroBias0/RAW/v1/000/355/101/00000/018d1ade-0dab-4b83-abca-32e5071745fe.root',
        '/store/data/Run2022B/ZeroBias0/RAW/v1/000/355/101/00000/55751c11-6c3f-4228-9274-30449165b8bb.root',
        '/store/data/Run2022B/ZeroBias0/RAW/v1/000/355/101/00000/15555f37-2f89-4ae9-abd6-be9db873899b.root',
        '/store/data/Run2022B/ZeroBias0/RAW/v1/000/355/101/00000/a8b86a9f-958c-4a3a-9c48-c3647220b282.root',
        '/store/data/Run2022B/ZeroBias0/RAW/v1/000/355/101/00000/9b66de2c-6d14-4e1e-9173-784865fb615a.root',
        '/store/data/Run2022B/ZeroBias0/RAW/v1/000/355/101/00000/787ad655-36c0-4d99-9ec7-419920ace13e.root',
        '/store/data/Run2022B/ZeroBias0/RAW/v1/000/355/101/00000/492151f3-60cd-4593-932d-3ffd92cee5e3.root',
        '/store/data/Run2022B/ZeroBias0/RAW/v1/000/355/101/00000/989e6a5c-c7b8-4cfe-b1e4-facfe26e727c.root',
        '/store/data/Run2022B/ZeroBias0/RAW/v1/000/355/101/00000/e0866a09-d16d-486c-90f7-34f3048549a3.root',
        '/store/data/Run2022B/ZeroBias0/RAW/v1/000/355/101/00000/6f139683-5511-4bed-a5bd-2e69a07ca7d3.root',
        '/store/data/Run2022B/ZeroBias0/RAW/v1/000/355/101/00000/930867d0-5c5b-4ede-b44a-f8dec3a5720c.root',
        '/store/data/Run2022B/ZeroBias0/RAW/v1/000/355/101/00000/0ae30b0e-53a9-45c0-b14c-18b1478d5a35.root',
        '/store/data/Run2022B/ZeroBias0/RAW/v1/000/355/101/00000/f654b27d-4b85-45da-bbb1-b3e97c1c05f4.root',
        '/store/data/Run2022B/ZeroBias0/RAW/v1/000/355/101/00000/71fc43b0-7c42-48a8-b2e7-8be31c65010a.root',
        '/store/data/Run2022B/ZeroBias0/RAW/v1/000/355/101/00000/d6b5403d-757d-4429-8846-110e38ad843a.root',
        '/store/data/Run2022B/ZeroBias0/RAW/v1/000/355/101/00000/ae7bd503-7d02-4b20-819b-fd33372de714.root',
        '/store/data/Run2022B/ZeroBias0/RAW/v1/000/355/101/00000/4e32c948-e48f-4c56-80c9-4dba05c2c17f.root',
        '/store/data/Run2022B/ZeroBias0/RAW/v1/000/355/101/00000/e0df8a6b-ce0e-46e6-896e-c325687e0edf.root',
        '/store/data/Run2022B/ZeroBias0/RAW/v1/000/355/101/00000/afaacc08-176e-489c-b54c-860dae76bfb6.root',
        '/store/data/Run2022B/ZeroBias0/RAW/v1/000/355/101/00000/4e175af3-8336-4e11-b316-9893b7ce75b8.root',
        '/store/data/Run2022B/ZeroBias1/RAW/v1/000/355/101/00000/302117f8-c0c7-4d56-8075-9d1ed4ec5fe0.root',
        '/store/data/Run2022B/ZeroBias1/RAW/v1/000/355/101/00000/70353fe6-7718-487a-aade-6edb24d89f91.root',
        '/store/data/Run2022B/ZeroBias1/RAW/v1/000/355/101/00000/f49511e1-c0c3-4194-8cf1-7844a9e99dbf.root',
        '/store/data/Run2022B/ZeroBias1/RAW/v1/000/355/101/00000/80b2658d-c872-445b-aa3a-d3514ce42c0c.root',
        '/store/data/Run2022B/ZeroBias1/RAW/v1/000/355/101/00000/cb5d90a1-2e68-4709-9cbc-6a92d462e98e.root',
        '/store/data/Run2022B/ZeroBias1/RAW/v1/000/355/101/00000/2fa058e0-572c-4b30-8d16-c82c2ff4e982.root',
        '/store/data/Run2022B/ZeroBias1/RAW/v1/000/355/101/00000/af9a317d-7c65-4107-8e10-d349429d8ed3.root',
        '/store/data/Run2022B/ZeroBias1/RAW/v1/000/355/101/00000/f68e1c35-1f0f-4720-b69f-e5ed8a7e309c.root',
        '/store/data/Run2022B/ZeroBias1/RAW/v1/000/355/101/00000/9a17f8ca-c338-4185-b65b-726ddcdd097e.root',
        '/store/data/Run2022B/ZeroBias1/RAW/v1/000/355/101/00000/0fdc85c8-e68b-4146-bc6b-edb7b8ca75a2.root',
        '/store/data/Run2022B/ZeroBias1/RAW/v1/000/355/101/00000/3579bb17-2467-46ed-9b3f-2c0136329e80.root',
        '/store/data/Run2022B/ZeroBias1/RAW/v1/000/355/101/00000/1c84773f-0bd6-4954-9c25-65ff718dc1e5.root',
        '/store/data/Run2022B/ZeroBias1/RAW/v1/000/355/101/00000/100eade0-3349-4d20-b1eb-0399b4680d90.root',
        '/store/data/Run2022B/ZeroBias1/RAW/v1/000/355/101/00000/7ac3442c-227b-42dd-9d53-4257ea81c201.root',
        '/store/data/Run2022B/ZeroBias1/RAW/v1/000/355/101/00000/c64f4b93-df66-41c0-95d4-6bd5bc6ebf09.root',
        '/store/data/Run2022B/ZeroBias1/RAW/v1/000/355/101/00000/64546761-33af-4412-9876-35d153be240a.root',
        '/store/data/Run2022B/ZeroBias1/RAW/v1/000/355/101/00000/f1ad3554-aa62-40d9-bd4a-e94ed5e249c1.root',
        '/store/data/Run2022B/ZeroBias1/RAW/v1/000/355/101/00000/60eb5ebc-ac59-4690-93a3-a5fb3f9808bf.root',
        '/store/data/Run2022B/ZeroBias1/RAW/v1/000/355/101/00000/e4b5221a-6340-429a-aa7c-27ad3dcfd4ef.root',
        '/store/data/Run2022B/ZeroBias1/RAW/v1/000/355/101/00000/f473efc5-0df8-433b-8cfc-0642b1d49120.root',
        '/store/data/Run2022B/ZeroBias1/RAW/v1/000/355/101/00000/3e4545c5-be0e-43e3-ba28-f222084aaace.root',
        '/store/data/Run2022B/ZeroBias1/RAW/v1/000/355/101/00000/4e9a740c-8827-4e73-b3f5-5bdc9fb4d246.root',
        '/store/data/Run2022B/ZeroBias1/RAW/v1/000/355/101/00000/a4d9a218-9b1e-4d94-bb7a-072d5bed818d.root',
        '/store/data/Run2022B/ZeroBias1/RAW/v1/000/355/101/00000/1bca7334-30d8-4ef7-88d4-8fa4e53d29b3.root',
        '/store/data/Run2022B/ZeroBias1/RAW/v1/000/355/101/00000/4c7231ce-9352-4cfa-9dcd-7b00890012f3.root',
        '/store/data/Run2022B/ZeroBias1/RAW/v1/000/355/101/00000/d51213e3-deca-41cc-bab1-1ece66eea20c.root',
        '/store/data/Run2022B/ZeroBias1/RAW/v1/000/355/101/00000/8257ed34-875f-4eb6-8a6d-6f72b50e5cf5.root',
        '/store/data/Run2022B/ZeroBias1/RAW/v1/000/355/101/00000/6b635d4e-e2c3-4fb9-a7f6-595950234ab1.root',
        '/store/data/Run2022B/ZeroBias2/RAW/v1/000/355/101/00000/f5289402-5d92-4159-a9eb-23dc850e687a.root',
        '/store/data/Run2022B/ZeroBias2/RAW/v1/000/355/101/00000/c545268b-63ea-4f1c-aabb-4f004ae40eb0.root',
        '/store/data/Run2022B/ZeroBias2/RAW/v1/000/355/101/00000/075606a4-6b83-4360-a306-a31f940d16af.root',
        '/store/data/Run2022B/ZeroBias2/RAW/v1/000/355/101/00000/d74ed7d0-8854-452f-b1a9-6732cf73d597.root',
        '/store/data/Run2022B/ZeroBias2/RAW/v1/000/355/101/00000/45bbe7f9-52dd-4684-964d-0dbe7234f327.root',
        '/store/data/Run2022B/ZeroBias2/RAW/v1/000/355/101/00000/249af257-594f-47e4-af0c-299efa1374c5.root',
        '/store/data/Run2022B/ZeroBias2/RAW/v1/000/355/101/00000/d10e005d-68c7-4d11-803f-635d1d351fe3.root',
        '/store/data/Run2022B/ZeroBias2/RAW/v1/000/355/101/00000/013a491e-fc20-441f-b2bc-f993f0be3dd7.root',
        '/store/data/Run2022B/ZeroBias2/RAW/v1/000/355/101/00000/97408875-af85-42fb-92a2-c1f91c868b08.root',
        '/store/data/Run2022B/ZeroBias2/RAW/v1/000/355/101/00000/d8422fef-0a86-4dae-983f-dcb9e908f629.root',
        '/store/data/Run2022B/ZeroBias2/RAW/v1/000/355/101/00000/9f9e0558-d032-42a5-b583-216e5aaed5a0.root',
        '/store/data/Run2022B/ZeroBias2/RAW/v1/000/355/101/00000/ee27618a-77ca-4cf2-a84b-899ce1b98061.root',
        '/store/data/Run2022B/ZeroBias2/RAW/v1/000/355/101/00000/18184238-4430-4bf0-8687-bafed1b4c459.root',
        '/store/data/Run2022B/ZeroBias2/RAW/v1/000/355/101/00000/0dbb41cd-49d2-4367-a1a1-aad5aca78797.root',
        '/store/data/Run2022B/ZeroBias2/RAW/v1/000/355/101/00000/56b03fda-b9a4-46b1-bb13-b560bae83489.root',
        '/store/data/Run2022B/ZeroBias2/RAW/v1/000/355/101/00000/8c54e691-37d4-4531-90c8-0e31f5e28758.root',
        '/store/data/Run2022B/ZeroBias2/RAW/v1/000/355/101/00000/129930be-d606-4490-850e-563d2b30545c.root',
        '/store/data/Run2022B/ZeroBias2/RAW/v1/000/355/101/00000/c76f8be8-d4ff-4e05-83d9-109969f015fc.root',
        '/store/data/Run2022B/ZeroBias2/RAW/v1/000/355/101/00000/95e84895-8371-4b47-88db-f4abe87ddb67.root',
        '/store/data/Run2022B/ZeroBias2/RAW/v1/000/355/101/00000/2524bfbf-fe38-43ad-817b-2c0d3486e8ed.root',
        '/store/data/Run2022B/ZeroBias2/RAW/v1/000/355/101/00000/88d64cf7-1ef2-4422-a1fe-f6314a508042.root',
        '/store/data/Run2022B/ZeroBias2/RAW/v1/000/355/101/00000/88295003-bc5e-4d01-beb5-446fcd3ca09f.root',
        '/store/data/Run2022B/ZeroBias2/RAW/v1/000/355/101/00000/bd5292f9-88fa-4531-a363-e70a7fd5086b.root',
        '/store/data/Run2022B/ZeroBias2/RAW/v1/000/355/101/00000/df444818-b0de-4687-8f92-270d62127856.root',
        '/store/data/Run2022B/ZeroBias2/RAW/v1/000/355/101/00000/c3c0277a-0873-4fd1-aa6a-9079b77803d3.root',
        '/store/data/Run2022B/ZeroBias2/RAW/v1/000/355/101/00000/4fbc06d1-af34-45ed-9a64-9d2543f9c7ad.root',
        '/store/data/Run2022B/ZeroBias2/RAW/v1/000/355/101/00000/4dccb585-fee1-478a-818f-4042a4e77b5c.root',
        '/store/data/Run2022B/ZeroBias2/RAW/v1/000/355/101/00000/4a6bbf69-27dd-494c-b72a-762fce894aa1.root',
        #'/store/data/Run2022B/HcalNZS/RAW/v1/000/355/101/00000/4bdfed20-301c-4200-8039-d8ff2b69206b.root',
        #'/store/data/Run2022B/Cosmics/RAW/v1/000/355/101/00000/70618426-3c64-4fb5-93e1-8e03f4f2f1a6.root'
    ],
    355100: [  # 2022 First Run 3 Collisions at 13.6 TeV / ZeroBias
        '/store/data/Run2022B/ZeroBias/RAW/v1/000/355/100/00000/11c592ae-1b21-44db-8c0c-6dd02f6b64a2.root'
    ],
    353689: [
        '/store/data/Run2022A/MinimumBias0/RAW/v1/000/353/689/00000/ac4f2816-6f46-43d8-9b82-84338bdc5a66.root'
    ],
    353087: [  # 2022 900 GeV Collisions / MinimumBias
        '/store/data/Run2022A/MinimumBias0/RAW/v1/000/353/087/00000/87be9c0d-1baa-4e31-a454-c0bac953dc27.root'
    ],
    352929: [  # 2022 900 GeV Collisions / MinimumBias including PPS
        '/store/data/Run2022A/MinimumBias9/RAW/v1/000/352/929/00000/01c1f45d-ed04-472c-8263-4fe58d5c4f43.root'
    ],
    352568: [  # 2022 900 GeV Collisions / Zero/MinimumBias
        '/store/data/Run2022A/MinimumBias0/RAW/v1/000/352/568/00000/d4dcc6b1-0c5d-4b89-a117-d82fbceec7d1.root'
    ],
    352417: [  # 2022 900 GeV Collisions / Zero/MinimumBias (Note: HCAL timing scan, so data can not be trusted)
        '/store/data/Run2022A/MinimumBias0/RAW/v1/000/352/417/00000/33f8bcaa-00d6-4ef6-b7b5-c682b1779030.root'
    ],
    352173: [  # 2022 900 GeV Collisions (Unstable) / ZeroBias
        '/store/data/Commissioning2022/ZeroBias0/RAW/v1/000/352/173/00000/054f8331-1703-4ce4-b099-428e37f42ff9.root'
    ],
    352041: [  # 2022 CRAFT (L1Menu_Collisions2022_v1_0_1) / Cosmics
        '/store/data/Commissioning2022/Cosmics/RAW/v1/000/352/041/00000/d6b8697a-9e77-436c-b4b7-1317e34e403e.root'
    ],
    347945: [  # 2022 MWGR1 / Cosmics
        '/store/data/Commissioning2022/Cosmics/RAW/v1/000/347/945/00000/7ee8472c-59e0-469e-972a-a4e191dc500a.root'
    ],
    346512: [  # 2021 Pilot Beam Test / HLTPhysics (900 GeV Collisions, last run)
        '/store/data/Commissioning2021/HLTPhysics/RAW/v1/000/346/512/00000/9e1384d9-83b8-4240-8486-950fa0e22a77.root'
    ],
    346452: [  # 2021 Pilot Beam Test / Zero/MinimumBias (900 GeV Collisions)
        '/store/data/Commissioning2021/ZeroBias0/RAW/v1/000/346/452/00000/38409370-1134-4f45-b3be-856633d53f4c.root'
    ],
    345823: [  # 2021 CRAFT / Cosmics
        '/store/data/Commissioning2021/Cosmics/RAW/v1/000/345/823/00000/06948445-a237-4d8b-91ce-727932458c03.root'
    ],
    343171: [  # 2021 CRUZET / Cosmics
        '/store/data/Commissioning2021/Cosmics/RAW/v1/000/343/171/00000/fd7d4ede-2d31-4011-bea1-489444a23ed4.root'
    ],
    342154: [  # 2021 MWGR4 / Cosmics
        '/store/data/Commissioning2021/Cosmics/RAW/v1/000/342/154/00000/2b42c3f4-b6d7-444b-9dca-47c2d249dd53.root'
    ],
    341169: [  # 2021 MWGR3 / Cosmics
        '/store/data/Commissioning2021/Cosmics/RAW/v1/000/341/169/00000/886d4e47-00e3-4ccd-9d2d-a9683622f51b.root'
    ],
    341139: [  # 2021 MWGR3 / MiniDaq
        '/store/data/Commissioning2021/MiniDaq/RAW/v1/000/341/139/00000/3bdad23c-5e58-4510-a5d9-8b9747ba634b.root'
    ],
    340207: [  # 2021 MWGR2 / Cosmics
        '/store/data/Commissioning2021/Cosmics/RAW/v1/000/340/207/00000/d7836c50-0aa3-4b46-ae9a-770aa4b87e30.root'
    ],
    339579: [  # 2021 MWGR1 / Cosmics with displaced muon seeds
        '/store/data/Commissioning2021/HLTPhysics/RAW/v1/000/339/579/00000/a26e3078-ac1f-49c3-8a40-e9007fbd1b47.root'
    ],
    338717: [  # 2020 MWGR4 / Cosmics
        '/store/data/Commissioning2020/Cosmics/RAW/v1/000/338/717/00000/9B97E41C-639B-4A46-8BE8-E45B605442DF.root'
    ],
    337242: [  # 2020 MWGR3 / Cosmics
        '/store/data/Commissioning2020/Cosmics/RAW/v1/000/337/242/00000/F73C6160-3892-8A42-9EB2-B21F7728025E.root'
    ],
    336435: [  # 2020 MWGR2 / Cosmics
        '/store/data/Commissioning2020/MinimumBias/RAW/v1/000/336/435/00000/E6E0F0FC-9FCB-4444-AFAF-6159FDD40A86.root'
    ],
    335518: [  # 2020 MWGR1 / VirginRaw
        '/store/data/Commissioning2020/VRRandom0/RAW/v1/000/335/518/00000/8289EA59-260C-1746-B67A-09B96FE73C0A.root'
    ],
    335443: [  # 2020 MWGR1 / Cosmics
        '/store/data/Commissioning2020/Cosmics/RAW/v1/000/335/443/00000/81EAE361-0FBA-0B4F-9728-227DE2567C7B.root'
    ],
    334518: [  # 2020 MWGR0 / VirginRaw
        '/store/data/Commissioning2019/VRRandom3/RAW/v1/000/334/518/00000/18B41CEB-DCF7-BD46-B6BC-0E7E56E7B047.root'
    ],
    334393: [  # 2020 MWGR0 / Cosmics
        '/store/data/Commissioning2019/HLTPhysics/RAW/v1/000/334/393/00000/E0D10C28-5C45-8147-A967-8FCE150D9514.root'
    ],
    331595: [  # 2019 MWGR4 / VirginRaw
        '/store/data/Commissioning2019/VRRandom3/RAW/v1/000/331/595/00000/3F49019E-7FA1-9A41-A8DE-418E5AEB988E.root'
    ],
    331483: [  # 2019 MWGR4 / Cosmics
        '/store/data/Commissioning2019/HLTPhysics/RAW/v1/000/331/483/00000/26C27254-3211-3942-B192-AFC3DB02BF1D.root'
    ],
    330061: [
        'file:/nfshome0/hltpro/hilton_c2f13_20_04/run330061_ls0136_index000005_fu-c2a03-41-02_pid362895.raw'
    ],
    328788: [  # Cosmics
        '/store/data/Commissioning2019/HLTPhysics/RAW/v1/000/328/788/00000/F5DC78DF-D593-5E41-8DCF-A02F21A3FC44.root'
    ],
    328691: [  # VirginRaw
        '/store/data/Commissioning2019/VRRandom3/RAW/v1/000/328/691/00000/00117159-5391-2C49-98CA-949BD0537DD9.root'
    ],
}
