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
    398600:[ #HLTPhysics, Run2025G, run 398600
       '/store/data/Run2025G/HLTPhysics/RAW/v1/000/398/600/00000/043f5e13-fa7e-4a58-8ebb-09b88f24d30e.root',
       '/store/data/Run2025G/HLTPhysics/RAW/v1/000/398/600/00000/062a7aa4-239f-4a69-96ee-2afa45c01c26.root',
       '/store/data/Run2025G/HLTPhysics/RAW/v1/000/398/600/00000/0b8ba66c-f237-4c23-90e6-055334b3cef4.root',
       '/store/data/Run2025G/HLTPhysics/RAW/v1/000/398/600/00000/0dbd8520-c847-49da-8d76-1230fb8c6148.root',
       '/store/data/Run2025G/HLTPhysics/RAW/v1/000/398/600/00000/0e69eabd-7ac0-4d30-b9dc-431a549477ef.root',    
    ],
    398342:[ # Cosmics, Run2025G, run 398342, LS = [224, 228], 42701 events (RUCIO rule created)
       '/store/data/Run2025G/Cosmics/RAW/v1/000/398/342/00000/cce317da-17e9-4465-9ba5-4bc9eb207317.root',
    ],
    398335: [ # HLTPhysics, Run2025G, run 398335, LS = [], 17037 events
       '/store/data/Run2025G/HLTPhysics/RAW/v1/000/398/335/00000/033dbf5e-d09a-4b8a-944e-3d337428ffeb.root',
       '/store/data/Run2025G/HLTPhysics/RAW/v1/000/398/335/00000/055907eb-a34b-4cfe-aaf0-8a446bbebd36.root',
       '/store/data/Run2025G/HLTPhysics/RAW/v1/000/398/335/00000/0684d03d-61a9-4f35-98a8-576674b77b54.root',
       '/store/data/Run2025G/HLTPhysics/RAW/v1/000/398/335/00000/07b1b55f-64e5-4e2a-9493-b1b2cc46b8d8.root',
    ],
    398308:[ # HLTPhysics, Run2025G, run 398308, LS = [], 17236 events
       '/store/data/Run2025G/HLTPhysics/RAW/v1/000/398/308/00000/0055e4bd-e956-4030-a717-ecc7ff1fd49d.root',
       '/store/data/Run2025G/HLTPhysics/RAW/v1/000/398/308/00000/04e189c7-cee8-451b-be97-0cd586636cfd.root',
       '/store/data/Run2025G/HLTPhysics/RAW/v1/000/398/308/00000/08d12008-0a22-4e7c-aa6d-c6421f8f6057.root',
       '/store/data/Run2025G/HLTPhysics/RAW/v1/000/398/308/00000/0fd1f5f9-ebe8-4095-b2a9-f8f650702fb1.root',
    ],
    398040:[ # HLTPhysics, Run2025G, run 398040, LS = [14, 23], 4241 events (RUCIO rule created)
       '/store/data/Run2025G/HLTPhysics/RAW/v1/000/398/040/00000/0994ecc9-5975-49bf-b078-f943d4248860.root',
    ],
    398226:[
        'root://eoscms.cern.ch//eos/cms/tier0/store/data/Run2025G/Cosmics/RAW/v1/000/398/226/00000/a348aa0d-f9ef-4693-9ecb-d071763863a3.root'
    ],
    397817:[
        #'root://eoscms.cern.ch//eos/cms/tier0/store/data/Run2025F/HLTPhysics/RAW/v1/000/397/817/00000/7d8e25fb-6161-
        #'/store/data/Run2025F/EGamma0/RAW/v1/000/397/817/00000/fa90bf6c-b987-4c69-87c8-b9cfe1641df7.root'
        '/store/data/Run2025F/EGamma0/RAW/v1/000/397/817/00000/f6b10cdb-d578-4b48-8e64-535d6c8caca9.root'
    ],
    397698: [ # Cosmics 2025F
        'root://eoscms.cern.ch//eos/cms/tier0/store/data/Run2025F/Cosmics/RAW/v1/000/397/698/00000/0208d8a5-7bb2-4daf-9d22-6c2d566f7305.root',
        #'root://eoscms.cern.ch//eos/cms/tier0/store/data/Run2025F/Cosmics/RAW/v1/000/397/698/00000/101235c9-53fd-416e-ad22-af7ce62b1764.root',
        #'root://eoscms.cern.ch//eos/cms/tier0/store/data/Run2025F/Cosmics/RAW/v1/000/397/698/00000/212ed47d-e945-4717-95d7-d444752c7d78.root',
        #'root://eoscms.cern.ch//eos/cms/tier0/store/data/Run2025F/Cosmics/RAW/v1/000/397/698/00000/2ee584a9-642f-4940-9535-e144b24240f5.root',
        #'root://eoscms.cern.ch//eos/cms/tier0/store/data/Run2025F/Cosmics/RAW/v1/000/397/698/00000/3f1e8c3b-0942-470c-9dfd-efcdc054686e.root',
        'root://eoscms.cern.ch//eos/cms/tier0/store/data/Run2025F/Cosmics/RAW/v1/000/397/698/00000/3fcb1176-396b-4c70-965c-4828a74739ca.root',
        'root://eoscms.cern.ch//eos/cms/tier0/store/data/Run2025F/Cosmics/RAW/v1/000/397/698/00000/4572a4f2-409e-44fd-b78e-057b336e55f6.root',
        'root://eoscms.cern.ch//eos/cms/tier0/store/data/Run2025F/Cosmics/RAW/v1/000/397/698/00000/5781c668-9437-4a2f-9468-96a7f16948fd.root',
        'root://eoscms.cern.ch//eos/cms/tier0/store/data/Run2025F/Cosmics/RAW/v1/000/397/698/00000/5a8654f8-fdce-41a7-8ff5-6ffbface7b81.root'
    ],
    397492:[
        '/store/data/Run2025F/HLTPhysics/RAW/v1/000/397/492/00000/02a80049-15c9-4c41-ae91-9ed221a4338a.root',
        #'/store/data/Run2025F/HLTPhysics/RAW/v1/000/397/492/00000/aad4745b-b6f9-435a-bfdd-83b06cc2ccf6.root',
        #'/store/data/Run2025F/HLTPhysics/RAW/v1/000/397/492/00000/30db2cea-e3b1-461a-aff2-bb60c3674b65.root',
        '/store/data/Run2025F/HLTPhysics/RAW/v1/000/397/492/00000/7ae6601b-9a63-451b-900a-6436f601fb25.root',
        '/store/data/Run2025F/HLTPhysics/RAW/v1/000/397/492/00000/a23e2d45-89b1-4592-897b-1378785a9961.root',
        '/store/data/Run2025F/HLTPhysics/RAW/v1/000/397/492/00000/379c4d56-f31a-4d54-a19e-f06d7b43b71f.root',
    ],
    396805: [ # Collisions 2025, era Run2025F, 2460b fill, PD HLTPhysics, Run 396805, LS = 607-615, 948-956, 966-974, L1Menu_Collisions2025_v1_3_0
        # Express run
        #'/store/express/Run2025F/ExpressPhysics/FEVT/Express-v1/000/396/805/00000/0034d394-cb04-4640-acea-01a6969234aa.root',
        'root://eoscms.cern.ch//eos/cms/store/data/Run2025F/HLTPhysics/RAW/v1/000/396/805/00000/53e9e1aa-30d0-4683-870e-7ceda767b46a.root',
        'root://eoscms.cern.ch//eos/cms/store/data/Run2025F/HLTPhysics/RAW/v1/000/396/805/00000/18e43e08-688a-40d0-970b-c889d4f16ed4.root',
        'root://eoscms.cern.ch//eos/cms/store/data/Run2025F/HLTPhysics/RAW/v1/000/396/805/00000/4e20363a-4ec9-40cc-ad29-2f117d59e15c.root',
    ],
    395670: [
        'root://eoscms.cern.ch//eos/cms/store/data/Run2025D/HLTPhysics/RAW/v1/000/395/670/00000/99245758-c190-4d80-ae5c-781df89b7f86.root',
    ],
    394748:[
#        '/store/data/Run2025D/Cosmics/RAW/v1/000/394/748/00000/6df1b290-bac8-49aa-8b31-4671c0b5005d.root'
         'root://eoscms.cern.ch//eos/cms/tier0/store/data/Run2025D/Cosmics/RAW/v1/000/394/748/00000/10674650-0b59-4183-9d98-4b21cc3be2ba.root'
    ],
    394536:[                                                                                              
        'root://eoscms.cern.ch//eos/cms/store/data/Run2025D/Cosmics/RAW/v1/000/394/536/00000/ad81351b-6e8d-47c8-9387-7a208b16ccc4.root',
        'root://eoscms.cern.ch//eos/cms/store/data/Run2025D/Cosmics/RAW/v1/000/394/536/00000/85f93a0b-e8c3-4817-8b54-5d266beb61e3.root',
    ],
    394635:[                                                                                              
        'root://eoscms.cern.ch//eos/cms/store/data/Run2025D/HLTPhysics/RAW/v1/000/394/635/00000/82f3e333-26c7-4714-9a8a-b294163372db.root',
        'root://eoscms.cern.ch//eos/cms/store/data/Run2025D/HLTPhysics/RAW/v1/000/394/635/00000/b59507eb-0118-4522-9fa1-de30c92ef13f.root',
        'root://eoscms.cern.ch//eos/cms/store/data/Run2025D/HLTPhysics/RAW/v1/000/394/635/00000/70b68534-6a1a-4255-a65c-8112712d1afd.root',
        'root://eoscms.cern.ch//eos/cms/store/data/Run2025D/HLTPhysics/RAW/v1/000/394/635/00000/22c287d2-1156-4abf-9729-28faa0962925.root'
    ],
    394494:[
        'root://eoscms.cern.ch//eos/cms/store/data/Run2025D/HLTPhysics/RAW/v1/000/394/494/00000/6a906022-2b9a-4dfc-a69e-fd497a1a85a2.root',
        'root://eoscms.cern.ch//eos/cms/store/data/Run2025D/HLTPhysics/RAW/v1/000/394/494/00000/56089140-cfc9-42bd-b18e-d07c0d28e1d1.root',
        'root://eoscms.cern.ch//eos/cms/store/data/Run2025D/HLTPhysics/RAW/v1/000/394/494/00000/f24ecbc7-fa3a-4af3-8eb5-7d454a321bc4.root',
        'root://eoscms.cern.ch//eos/cms/store/data/Run2025D/HLTPhysics/RAW/v1/000/394/494/00000/7f6e9f9b-bdd7-4646-9ea7-e69d3854117a.root',
        'root://eoscms.cern.ch//eos/cms/store/data/Run2025D/HLTPhysics/RAW/v1/000/394/494/00000/3a87e29d-08e2-470a-ac0e-8f32f8537a7e.root'
    ],
    393918: ['root://eoscms.cern.ch//eos/cms/store/data/pORun2025/HLTPhysics/RAW/v1/000/393/918/00000/08e2a5e9-2e1a-4bdb-b977-612d450c5ebb.root',
             'root://eoscms.cern.ch//eos/cms/store/data/pORun2025/HLTPhysics/RAW/v1/000/393/918/00000/26c28186-0b69-423b-b189-214e3357ca92.root',
             'root://eoscms.cern.ch//eos/cms/store/data/pORun2025/HLTPhysics/RAW/v1/000/393/918/00000/3cf0658a-5ad7-47b5-9d82-557c3de4077a.root'], 
    393998: ['root://eoscms.cern.ch//eos/cms/store/data/pORun2025/HLTPhysics/RAW/v1/000/393/998/00000/5f1ff1e6-4cec-405c-b167-983553c7dc9d.root'],
    393952: [      
      'root://eoscms.cern.ch//eos/cms/store/data/pORun2025/HLTPhysics/RAW/v1/000/393/952/00000/2b00ba7f-2cd3-4fd3-9b78-9d9e3b1df0f2.root',
      'root://eoscms.cern.ch//eos/cms/store/data/pORun2025/HLTPhysics/RAW/v1/000/393/952/00000/8499a2af-833a-4aeb-a125-193a90351ce9.root',
      'root://eoscms.cern.ch//eos/cms/store/data/pORun2025/HLTPhysics/RAW/v1/000/393/952/00000/a74a21ff-526e-4bf8-9e67-2b40907d540d.root',
      'root://eoscms.cern.ch//eos/cms/store/data/pORun2025/HLTPhysics/RAW/v1/000/393/952/00000/ad531924-d230-4cd9-b9b3-5455f5bb9d04.root'
  ],
    393378: [                                                                                                                     
        'root://eoscms.cern.ch//eos/cms/store/data/Run2025C/HLTPhysics/RAW/v1/000/393/378/00000/01568974-3cb5-42a3-8153-aa9c918a0c84.root',
        'root://eoscms.cern.ch//eos/cms/store/data/Run2025C/HLTPhysics/RAW/v1/000/393/378/00000/03e9bd70-48e7-4abe-864c-d5fe4a751866.root',
        'root://eoscms.cern.ch//eos/cms/store/data/Run2025C/HLTPhysics/RAW/v1/000/393/378/00000/0cfdc782-4f01-4027-aeeb-525744879a70.root'
    ],

    393376: [                                                                                                                     
    'root://eoscms.cern.ch//eos/cms/store/data/Run2025C/HLTPhysics/RAW/v1/000/393/376/00000/00773c15-cce5-4a51-86d5-c7158e7a3da4.root',                                                                                                                               
#    'root://eoscms.cern.ch//eos/cms/store/data/Run2025C/HLTPhysics/RAW/v1/000/393/376/00000/030b4768-07fb-4ea2-b6a6-af4d79710190.root',                                                                                                                               
#    'root://eoscms.cern.ch//eos/cms/store/data/Run2025C/HLTPhysics/RAW/v1/000/393/376/00000/03694a51-2890-4dc1-86ae-e2e0026c3a02.root',                                                                                                                               
    ],                                                                                                                             
    393747: [ 'root://eoscms.cern.ch//eos/cms/store/data/pORun2025/HLTPhysics/RAW/v1/000/393/747/00000/946b82b6-bd3c-44c8-bf89-a43352a3563f.root'
    ],

    393461: [ 'root://eoscms.cern.ch//eos/cms/store/data/Run2025C/HLTPhysics/RAW/v1/000/393/461/00000/0043114e-858e-499d-970a-df7dac3b6e2e.root'

    ],

    392477: [
        'root://eoscms.cern.ch//eos/cms/store/data/Run2025C/HLTPhysics/RAW/v1/000/392/477/00000/039247e3-345e-4637-9359-25ec7515ce21.root',
        #'root://eoscms.cern.ch//eos/cms/store/data/Run2025C/HLTPhysics/RAW/v1/000/392/477/00000/0786c0bf-f716-4955-b2ee-6594a21e8ae4.root',
        #'root://eoscms.cern.ch//eos/cms/store/data/Run2025C/HLTPhysics/RAW/v1/000/392/477/00000/179fff9b-44a3-4dfa-8a02-5134268c98e3.root',
    ],
    392363: [
    '/store/data/Run2025C/EGamma0/RAW/v1/000/392/363/00000/aacec9fa-b678-41ce-8895-d06170f74267.root',
    ],
    392542: [
    '/store/data/Run2025C/EGamma0/RAW/v1/000/392/542/00000/cd3ade98-ddb7-4969-9d0f-d4913fb8460f.root',
    ],
    392538: [
    'root://eoscms.cern.ch//store/data/Run2025C/EGamma0/RAW/v1/000/392/538/00000/012215a5-f5b2-486a-a425-98c5621a395c.root',
    'root://eoscms.cern.ch//store/data/Run2025C/EGamma0/RAW/v1/000/392/538/00000/004e90ef-bce9-4124-9f4a-8719b8b33d76.root',
    #'/store/data/Run2025C/EGamma0/RAW/v1/000/392/538/00000/cd3ade98-ddb7-4969-9d0f-d4913fb8460f.root',
    ],
    386951: [
     '/store/data/Run2024I/HLTPhysics/RAW/v1/000/386/951/00000/9ef14b4a-536a-45f4-ab41-055bf7d08881.root'
    ],
    392175: [
    #'root://eoscms.cern.ch//eos/cms/store/data/Run2025C/Muon0/RAW/v1/000/392/175/00000/d2c6f593-7c7d-4a5c-99b2-baf3278806fa.root',
    '/store/data/Run2025C/Muon0/RAW/v1/000/392/175/00000/d2c6f593-7c7d-4a5c-99b2-baf3278806fa.root',
    ],
    392442: [
    '/store/data/Run2025C/Muon0/RAW/v1/000/392/442/00000/0150ccc0-bd49-4aa3-95a0-e0059c8d0f79.root',
    ],
    392440: [
    'root://eoscms.cern.ch//eos/cms/store/data/Run2025C/Muon0/RAW/v1/000/392/440/00000/fd37d2dc-1d11-4eba-b511-ca41ec5a4a5c.root',
    ],
    392382: [
    #'root://eoscms.cern.ch//eos/cms/store/data/Run2025C/Muon0/RAW/v1/000/392/382/00000/aa76351f-f62d-4ade-a0b2-5394f6572487.root',
    'root://eoscms.cern.ch//eos/cms/store/data/Run2025C/Muon0/RAW/v1/000/392/382/00000/7680aaac-fed0-4737-926d-4b37453c1126.root',
    #'root://eoscms.cern.ch/eos/cms/store/data/Run2025C/Muon0/RAW/v1/000/392/382/00000/aa76351f-f62d-4ade-a0b2-5394f6572487.root',
    #'root://eoscms.cern.ch/eos/cms/store/data/Run2025C/Muon0/RAW/v1/000/392/382/00000/7680aaac-fed0-4737-926d-4b37453c1126.root',
    ],
    392256: [
    'root://eoscms.cern.ch/eos/cms/store/data/Run2025C/HLTPhysics/RAW/v1/000/392/256/00000/fab3b7cf-fa98-498a-a648-a012cd3087d1.root',
    ],
    392250: [
    '/store/data/Run2025C/HLTPhysics/RAW/v1/000/392/250/00000/8102dde0-5c9b-455c-9c1c-e08b113bd427.root',
    '/store/data/Run2025C/HLTPhysics/RAW/v1/000/392/250/00000/8a06e77b-b965-4331-bb1d-d095b8f50a57.root',
    '/store/data/Run2025C/HLTPhysics/RAW/v1/000/392/250/00000/945ade33-a33d-47c6-8648-2077ca7f9f70.root',
    #'root://eoscms.cern.ch/eos/cms/store/data/Run2025C/HLTPhysics/RAW/v1/000/392/250/00000/6ac44868-3356-4a5c-85c7-a4e017ab174d.root',
    #'root://eoscms.cern.ch/eos/cms/store/data/Run2025C/HLTPhysics/RAW/v1/000/392/250/00000/301a103e-b25c-4dbc-9ec7-5cd65704c2d4.root',
    #'root://eoscms.cern.ch/eos/cms/store/data/Run2025C/HLTPhysics/RAW/v1/000/392/250/00000/9dd7538d-7000-429c-b676-40b8af694506.root ',
    ],
    392071: [
    #'/store/data/Run2025B/EphemeralZeroBias7/RAW/v1/000/392/071/00000/5a7dcdbd-bf13-4e02-a1ab-de023381da3b.root'
    #'/store/data/Run2025B/EphemeralZeroBias7/RAW/v1/000/392/071/00000/fd20a444-15c5-4dc9-aa9e-44a6b5a14e61.root'
    #'root://eoscms.cern.ch//eos/cms/tier0/store/data/Run2025B//EGamma0/RAW/v1/000/392/071/00000/4c8d6831-d9d1-469e-969d-16768cd4cfb3.root',
    #'root://eoscms.cern.ch//eos/cms/tier0/store/data/Run2025B/Muon0/RAW/v1/000/392/071/00000/6d1d3553-2d7b-46c1-829d-d3046022d678.root',
    #'root://eoscms.cern.ch//eos/cms//store/data/Run2025B/ZeroBias/RAW/v1/000/392/071/00000/1e7bfdac-c84b-46d6-9112-bc5bfe576acd.root',
    '/store/data/Run2025B/EGamma0/RAW/v1/000/392/071/00000/ae3bb3ab-43fa-4ce3-be03-85eea9e5c2b4.root',
    ],
    391952: [ # Collisions 2025, era Run2025B, 75b fill, PD HLTPhysics, Run 391952, LSs 1–327 (L1Menu_Collisions2025_v1_0_0)
        '/store/data/Run2025B/HLTPhysics/RAW/v1/000/391/952/00000/6e346ea3-b667-4cc8-a6d4-4b846067691c.root',
        '/store/data/Run2025B/HLTPhysics/RAW/v1/000/391/952/00000/b2b30328-6da0-4ceb-866c-f508bd678168.root',
        '/store/data/Run2025B/HLTPhysics/RAW/v1/000/391/952/00000/cb63a3b8-9ec7-45f1-9124-ac4a4da01f80.root',
    ],
    390785: [ # Cosmics 2025, era Run2025A, PD Cosmics, Run 390785 (L1Menu_Collisions2024_v1_3_0)
        '/store/data/Run2025A/Cosmics/RAW/v1/000/390/785/00000/33600d33-1946-489b-8735-e813df0a081d.root',
        '/store/data/Run2025A/Cosmics/RAW/v1/000/390/785/00000/6ac8dbe0-4017-4373-a521-ed6cb1390bf1.root',
        '/store/data/Run2025A/Cosmics/RAW/v1/000/390/785/00000/d007af47-11ae-4a9c-affe-84b62b21f227.root',
    ],
    386674: [ # Cosmics 2024, Run 386674, LS 1 (L1Menu_Collisions2024_v1_3_0)
        'root://eoscms.cern.ch//eos/cms/store/group/tsg/FOG/Cosmics2024/run386674/run386674_ls0006_streamPhysicsCommissioning_StorageManager.root',
    ],
    393918: [
        'root://eoscms.cern.ch//eos/cms/store/data/pORun2025/HLTPhysics/RAW/v1/000/393/918/00000/3cf0658a-5ad7-47b5-9d82-557c3de4077a.root',
    ],
    395670: [
        'root://eoscms.cern.ch//eos/cms/store/data/Run2025D/HLTPhysics/RAW/v1/000/395/670/00000/0fb61f14-6487-4862-a441-f03b50ca36cc.root'
    ],
    396405: [
        'root://eoscms.cern.ch//eos/cms/store/data/Run2025E/HLTPhysics/RAW/v1/000/396/405/00000/027d7cf3-ffd9-4f52-ad5c-0e3e22cc868c.root',
        'root://eoscms.cern.ch//eos/cms/store/data/Run2025E/HLTPhysics/RAW/v1/000/396/405/00000/028d8efe-5acc-47b0-bc16-edb43e8d1ae3.root',
        'root://eoscms.cern.ch//eos/cms//store/data/Run2025E/HLTPhysics/RAW/v1/000/396/405/00000/041813ad-ef1f-4d73-9031-115ec550a0e0.root'
    ]

}
