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
    401704:[ #MiniDAQ (EcalCalibration), Run2026A, run 401704 (to test EcalCalibration MiniDAQ menu)
       '/store/data/Run2026A/MiniDaq/RAW/v1/000/401/704/00000/d9b97556-58be-49f7-875d-6ebda38bf75d.root',
    ],
    401733:[ #HLTPhysics, Run2026A, run 401733 (830b fill 11481, LS = 499-513)
       '/store/data/Run2026A/HLTPhysics/RAW/v1/000/401/733/00000/d5b8a312-5230-469a-a451-d199e74012c2.root',
    ],
    401628:[ #Cosmics, Run2026A, run 401628 (LS = 17-31, all detectors IN and with HV ON)
       '/store/data/Run2026A/Cosmics/RAW/v1/000/401/628/00000/cadc68ba-b807-4548-a4fb-509babe06ba1.root',
    ],
    401420:[ #MiniDAQ (EcalCalibration), Commissioning2026, run 401420 (to test EcalCalibration MiniDAQ menu)
       '/store/data/Commissioning2026/MiniDaq/RAW/v1/000/401/420/00000/bfa68be5-7ac4-4d80-a3da-3a386faae421.root',
    ],
    401704: [ # 2026A MiniDAQ EcalCalibration
        'root://eoscms.cern.ch//eos/cms/tier0/store/data/Run2026A/MiniDaq/RAW/v1/000/401/704/00000/d9b97556-58be-49f7-875d-6ebda38bf75d.root',
    ],
    398803: [ # 2025G LowPU 7 run
        'root://eoscms.cern.ch//eos/cms/store/data/Run2025G/HLTPhysics/RAW/v1/000/398/803/00000/07c0e6ef-5301-47f9-bfb9-a2517d609f2b.root',
        'root://eoscms.cern.ch//eos/cms/store/data/Run2025G/HLTPhysics/RAW/v1/000/398/803/00000/d4282346-4667-4761-9c19-284130d339aa.root',
#        'root://eoscms.cern.ch//eos/cms/store/data/Run2025G/SpecialZeroBias0/RAW/v1/000/398/803/00000/f1c2c8f6-94f5-4e26-857f-57246b15007c.root',
#        'root://eoscms.cern.ch//eos/cms/store/data/Run2025G/SpecialZeroBias0/RAW/v1/000/398/803/00000/72c5c646-bee6-4f11-a6e4-29ab675781c7.root',
#        'root://eoscms.cern.ch//eos/cms/store/data/Run2025G/SpecialZeroBias0/RAW/v1/000/398/803/00000/b9e2115a-94b1-4381-b00d-9a0b538eb19a.root',
#        'root://eoscms.cern.ch//eos/cms/store/data/Run2025G/SpecialZeroBias0/RAW/v1/000/398/803/00000/5e75b23a-d222-41b7-af93-985e2b37bea2.root',
    ],
    401693: [ # 400b HLTPhysics
        'root://eoscms.cern.ch//eos/cms/tier0/store/data/Run2026A/HLTPhysics/RAW/v1/000/401/693/00000/a3749f6d-5c9b-421b-9929-764674135dcb.root',
        'root://eoscms.cern.ch//eos/cms/tier0/store/data/Run2026A/HLTPhysics/RAW/v1/000/401/693/00000/a395cac6-bc83-4258-9eb2-aec188bed0d1.root',
        'root://eoscms.cern.ch//eos/cms/tier0/store/data/Run2026A/HLTPhysics/RAW/v1/000/401/693/00000/a7f31833-6aaa-4528-aaae-5f55709cff60.root',
        'root://eoscms.cern.ch//eos/cms/tier0/store/data/Run2026A/HLTPhysics/RAW/v1/000/401/693/00000/a8653375-45ff-4b12-82d8-8ecde8105937.root',
        'root://eoscms.cern.ch//eos/cms/tier0/store/data/Run2026A/HLTPhysics/RAW/v1/000/401/693/00000/aae4fecc-4b07-42d0-90eb-5da00cc12f0b.root',
        'root://eoscms.cern.ch//eos/cms/tier0/store/data/Run2026A/HLTPhysics/RAW/v1/000/401/693/00000/ab22f432-cbc5-4740-af48-5434b956646e.root',
        'root://eoscms.cern.ch//eos/cms/tier0/store/data/Run2026A/HLTPhysics/RAW/v1/000/401/693/00000/b09751c7-02bb-4390-b61f-61a5a316d76f.root',
        'root://eoscms.cern.ch//eos/cms/tier0/store/data/Run2026A/HLTPhysics/RAW/v1/000/401/693/00000/b20d338e-4c3d-42f7-a8a3-da3e96145020.root',
        'root://eoscms.cern.ch//eos/cms/tier0/store/data/Run2026A/HLTPhysics/RAW/v1/000/401/693/00000/ba18d2b7-a29e-484b-adf7-724372c670f9.root',
        'root://eoscms.cern.ch//eos/cms/tier0/store/data/Run2026A/HLTPhysics/RAW/v1/000/401/693/00000/bb4911b7-1915-439a-b137-756ae58a5921.root',
        'root://eoscms.cern.ch//eos/cms/tier0/store/data/Run2026A/HLTPhysics/RAW/v1/000/401/693/00000/bd66c8a9-25b4-4859-b1f5-28ea5b2b614e.root',
        'root://eoscms.cern.ch//eos/cms/tier0/store/data/Run2026A/HLTPhysics/RAW/v1/000/401/693/00000/c03663a9-abcd-4fae-8018-5798d7e9441f.root',
        'root://eoscms.cern.ch//eos/cms/tier0/store/data/Run2026A/HLTPhysics/RAW/v1/000/401/693/00000/c120e71d-e5cc-413c-b996-32ca45164de9.root',
        'root://eoscms.cern.ch//eos/cms/tier0/store/data/Run2026A/HLTPhysics/RAW/v1/000/401/693/00000/c9864a94-a81a-432a-95b5-0c4fdfbce5a4.root',
    ],
    401642: [ # test for BSRT fill  CMSHLT-3773
        'root://eoscms.cern.ch//eos/cms/tier0/store/data/Run2026A/ZeroBias/RAW/v1/000/401/642/00000/b0c6c02b-1902-4a48-8ab3-555a85f1609a.root',
        'root://eoscms.cern.ch//eos/cms/tier0/store/data/Run2026A/ZeroBias/RAW/v1/000/401/642/00000/b1b3c586-ad82-4ff7-86c8-47a7e00ca8ae.root',
        'root://eoscms.cern.ch//eos/cms/tier0/store/data/Run2026A/ZeroBias/RAW/v1/000/401/642/00000/b1df2de9-fea2-4d4d-88d3-b993b5fbb5a7.root',
        'root://eoscms.cern.ch//eos/cms/tier0/store/data/Run2026A/ZeroBias/RAW/v1/000/401/642/00000/b216821b-37c8-4223-993d-c7a9b6766bd3.root',
        'root://eoscms.cern.ch//eos/cms/tier0/store/data/Run2026A/ZeroBias/RAW/v1/000/401/642/00000/b24aa9e6-d413-459d-910f-b6c058501c1e.root',
        'root://eoscms.cern.ch//eos/cms/tier0/store/data/Run2026A/ZeroBias/RAW/v1/000/401/642/00000/b2b270cf-7448-4faa-a345-928b4cb929cd.root',
        'root://eoscms.cern.ch//eos/cms/tier0/store/data/Run2026A/ZeroBias/RAW/v1/000/401/642/00000/b35fc480-9676-4743-8425-104b2204f12d.root',
        'root://eoscms.cern.ch//eos/cms/tier0/store/data/Run2026A/ZeroBias/RAW/v1/000/401/642/00000/b36cb44c-69ee-4b42-b516-c7c7b62ce4a2.root',
        'root://eoscms.cern.ch//eos/cms/tier0/store/data/Run2026A/ZeroBias/RAW/v1/000/401/642/00000/b39a1347-0840-483d-b0f0-211008d7db49.root',
        'root://eoscms.cern.ch//eos/cms/tier0/store/data/Run2026A/ZeroBias/RAW/v1/000/401/642/00000/b3da9440-ebfc-4709-8df7-c0799fc938e7.root',
        'root://eoscms.cern.ch//eos/cms/tier0/store/data/Run2026A/ZeroBias/RAW/v1/000/401/642/00000/b4173b36-0e13-4a96-a73a-7bd91960991b.root',
        'root://eoscms.cern.ch//eos/cms/tier0/store/data/Run2026A/ZeroBias/RAW/v1/000/401/642/00000/b50438c9-2710-4719-8745-add64fea6bf0.root',
        'root://eoscms.cern.ch//eos/cms/tier0/store/data/Run2026A/ZeroBias/RAW/v1/000/401/642/00000/b508e824-5b0d-4bc0-ab14-93adb19fc164.root',
        'root://eoscms.cern.ch//eos/cms/tier0/store/data/Run2026A/ZeroBias/RAW/v1/000/401/642/00000/b5bc4b97-04d6-408b-83e5-18f61b710d4c.root',
        'root://eoscms.cern.ch//eos/cms/tier0/store/data/Run2026A/ZeroBias/RAW/v1/000/401/642/00000/b603191b-8884-45ad-a451-76e29fac7102.root',
        'root://eoscms.cern.ch//eos/cms/tier0/store/data/Run2026A/ZeroBias/RAW/v1/000/401/642/00000/b627629d-98bd-41f6-aa91-d460ae2c9b3a.root',
    ],
    401669: [
        'root://eoscms.cern.ch//eos/cms/tier0/store/data/Run2026A/HLTPhysics/RAW/v1/000/401/669/00000/07cc3f2b-1579-4466-b6f0-68b1030f5964.root',
        'root://eoscms.cern.ch//eos/cms/tier0/store/data/Run2026A/HLTPhysics/RAW/v1/000/401/669/00000/16dea94d-defb-48fd-b5d6-db10dc9cfea4.root',
        'root://eoscms.cern.ch//eos/cms/tier0/store/data/Run2026A/HLTPhysics/RAW/v1/000/401/669/00000/2299fa61-ffd9-4b09-9ba8-09cbdf416aee.root',
        'root://eoscms.cern.ch//eos/cms/tier0/store/data/Run2026A/HLTPhysics/RAW/v1/000/401/669/00000/43d2d946-2669-4e42-95a7-b704288d350d.root',
        'root://eoscms.cern.ch//eos/cms/tier0/store/data/Run2026A/HLTPhysics/RAW/v1/000/401/669/00000/5118436a-df34-4030-8720-8b9a87c15640.root',
        'root://eoscms.cern.ch//eos/cms/tier0/store/data/Run2026A/HLTPhysics/RAW/v1/000/401/669/00000/5fc9a73b-f573-4030-9e56-5945bad51747.root',
        'root://eoscms.cern.ch//eos/cms/tier0/store/data/Run2026A/HLTPhysics/RAW/v1/000/401/669/00000/80fb0fef-976e-40a6-9319-d4498ecbd39a.root',
        'root://eoscms.cern.ch//eos/cms/tier0/store/data/Run2026A/HLTPhysics/RAW/v1/000/401/669/00000/89fec21f-a1a3-465e-8938-42cda4f0bfab.root'
    ],
    401411: [
        'root://eoscms.cern.ch//eos/cms/tier0/store/data/Commissioning2026/HLTPhysics/RAW/v1/000/401/411/00000/9a7ac0d9-c8a6-445a-84ac-50eff0dab0a2.root',
        'root://eoscms.cern.ch//eos/cms/tier0/store/data/Commissioning2026/HLTPhysics/RAW/v1/000/401/411/00000/ce73f96f-7b59-425d-a4f2-599e66fc4d41.root',
    ],
    401311: [
        'root://eoscms.cern.ch//eos/cms/tier0/store/data/Commissioning2026/HLTPhysics/RAW/v1/000/401/311/00000/78fd6524-bea9-4b66-9f7d-104835470efe.root',
        'root://eoscms.cern.ch//eos/cms/tier0/store/data/Commissioning2026/HLTPhysics/RAW/v1/000/401/311/00000/99b5790a-eeb4-4157-bee2-faba237b91ae.root',
        'root://eoscms.cern.ch//eos/cms/tier0/store/data/Commissioning2026/HLTPhysics/RAW/v1/000/401/311/00000/ce94ba24-7dd8-4085-b75d-9b0e292a5471.root',
        'root://eoscms.cern.ch//eos/cms/tier0/store/data/Commissioning2026/HLTPhysics/RAW/v1/000/401/311/00000/f988631d-e16e-469c-86e9-d65786c5b295.root',
    ],
    401302: [
        'root://eoscms.cern.ch//eos/cms/tier0/store/data/Commissioning2026/HLTPhysics/RAW/v1/000/401/302/00000/24660da1-f364-4a09-bf4f-0927a057b833.root',
        'root://eoscms.cern.ch//eos/cms/tier0/store/data/Commissioning2026/HLTPhysics/RAW/v1/000/401/302/00000/3043e813-531c-49df-846a-27631f05f2fb.root',
        'root://eoscms.cern.ch//eos/cms/tier0/store/data/Commissioning2026/HLTPhysics/RAW/v1/000/401/302/00000/3bc949d8-9bf6-435d-9950-40ba621f787b.root',
        'root://eoscms.cern.ch//eos/cms/tier0/store/data/Commissioning2026/HLTPhysics/RAW/v1/000/401/302/00000/3c3caf34-26d1-49ad-a3e2-bf305e6df32f.root',
        'root://eoscms.cern.ch//eos/cms/tier0/store/data/Commissioning2026/HLTPhysics/RAW/v1/000/401/302/00000/416a7468-f13d-4551-9cfd-07cf2516eed2.root',
        'root://eoscms.cern.ch//eos/cms/tier0/store/data/Commissioning2026/HLTPhysics/RAW/v1/000/401/302/00000/50e97ff0-0619-427d-9c67-fc060c262b92.root',
    ],
    401201: [ # Commissioning 2026 Cosmics
        'root://eoscms.cern.ch//eos/cms/tier0/store/data/Commissioning2026/Cosmics/RAW/v1/000/401/201/00000/00748ee6-be29-45ea-a57a-51d730948afd.root',
        'root://eoscms.cern.ch//eos/cms/tier0/store/data/Commissioning2026/Cosmics/RAW/v1/000/401/201/00000/01346f92-2f49-484a-b76e-e127de9a7c79.root',
        'root://eoscms.cern.ch//eos/cms/tier0/store/data/Commissioning2026/Cosmics/RAW/v1/000/401/201/00000/02999cf5-e8a6-4531-b9bd-876cd2a1fa68.root',
    ],
    400813: [
        'root://eoscms.cern.ch//eos/cms/tier0/store/data/Commissioning2026/Cosmics/RAW/v1/000/400/813/00000/13890ac3-2223-4c75-9397-b662bae20ae0.root',
        'root://eoscms.cern.ch//eos/cms/tier0/store/data/Commissioning2026/Cosmics/RAW/v1/000/400/813/00000/21239d10-33f7-4a71-88ad-595a9b63103a.root',
    ],
    399720:[ #HIPhysicsRawPrime HIRun2025A
       '/store/hidata/HIRun2025A/HIPhysicsRawPrime0/RAW/v1/000/399/720/00000/62c474b8-48f2-4ad9-ad27-fb509eca1ce3.root',
     ],
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
    ]
}
