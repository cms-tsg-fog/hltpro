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
    391952: [ # Collisions 2025, era Run2025B, PD HLTPhysics, Run 391952, LSs 1–327 (L1Menu_Collisions2025_v1_0_0)
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
    385094: [ # /cdaq/physics/Run2024/2e34/v1.4.4/HLT/V1, LS 1003, Run2024G, 2024-08-28
        'root://eoscms.cern.ch//eos/cms/store/data/Run2024G/HLTPhysics/RAW/v1/000/385/094/00000/0212b6f9-c79a-4ddc-a6d2-3449d6b6814a.root',
        'root://eoscms.cern.ch//eos/cms/store/data/Run2024G/HLTPhysics/RAW/v1/000/385/094/00000/be2c8eb8-0632-419c-bfc7-7cbb0ca97444.root',
        'root://eoscms.cern.ch//eos/cms/store/data/Run2024G/HLTPhysics/RAW/v1/000/385/094/00000/a5c8735c-7fd2-494f-ad44-c15ddb1eb70a.root'
    ],
    385016: [
        'root://eoscms.cern.ch//eos/cms/store/data/Run2024G/HLTPhysics/RAW/v1/000/385/016/00000/00237177-3afe-4042-8cb2-45169f041299.root',
        'root://eoscms.cern.ch//eos/cms/store/data/Run2024G/HLTPhysics/RAW/v1/000/385/016/00000/04cf8c95-a8e5-44b3-977f-95677ffd1a10.root',
        'root://eoscms.cern.ch//eos/cms/store/data/Run2024G/HLTPhysics/RAW/v1/000/385/016/00000/097554da-d30c-4887-8493-5ccee4bcd63f.root',
        'root://eoscms.cern.ch//eos/cms/store/data/Run2024G/HLTPhysics/RAW/v1/000/385/016/00000/09d21d02-ad59-410d-b2e3-07b868f4848d.root',
        'root://eoscms.cern.ch//eos/cms/store/data/Run2024G/HLTPhysics/RAW/v1/000/385/016/00000/0bce2108-d059-458e-9e00-04cae2a89b68.root',
    ],
    383449 : [
        '/store/data/Run2024F/HLTPhysics/RAW/v1/000/383/449/00000/467b5b10-5158-4e8c-ab29-9d3bd05d8244.root',
        '/store/data/Run2024F/HLTPhysics/RAW/v1/000/383/449/00000/16bf76b7-8c3c-4a86-8be8-f27ccb982a12.root',
        '/store/data/Run2024F/HLTPhysics/RAW/v1/000/383/449/00000/316fb71f-f59b-4e25-a809-f1fb2d80f49a.root',
    ],
    383418 : [
        'root://eoscms.cern.ch//store/data/Run2024F/EGamma0/RAW/v1/000/383/418/00000/ea621243-0275-40fe-9377-671e6508cdb5.root'
    383254 : [
        '/store/data/Run2024F/HLTPhysics/RAW/v1/000/383/254/00000/c454aaa4-9bda-4351-a7d1-91e8c28d4dba.root',
        '/store/data/Run2024F/HLTPhysics/RAW/v1/000/383/254/00000/c655e3c4-208e-42bf-abea-b8f7999c880f.root',
        '/store/data/Run2024F/HLTPhysics/RAW/v1/000/383/254/00000/fdb563c6-0fee-495a-beaa-c77b41adce64.root',
    ],
    382937 : [
        '/store/data/Run2024F/HLTPhysics/RAW/v1/000/382/937/00000/01ae1efe-9296-4c5e-868f-d18ea4401081.root',
        '/store/data/Run2024F/HLTPhysics/RAW/v1/000/382/937/00000/13518ad5-e4bc-4e82-97b6-6fa91f09a90c.root',
        '/store/data/Run2024F/HLTPhysics/RAW/v1/000/382/937/00000/069ef2f0-a0cc-4ba1-8470-2c9be0a2fec2.root',
    ],
    382343 : [
        '/store/data/Run2024F/HLTPhysics/RAW/v1/000/382/343/00000/01dec942-c274-4e71-b2b9-c3fb917db3ac.root',
        '/store/data/Run2024F/HLTPhysics/RAW/v1/000/382/343/00000/f400c83f-0b87-481e-97e0-03f3e84ff089.root'
        ],
    381516 : [
        'root://eoscms.cern.ch//store/data/Run2024E/JetMET0/RAW/v1/000/381/516/00000/00e12191-9b77-4421-a101-6dfe3ee49885.root'
    ],
    381455 : [ # Run2024E, Cosmics (L1Menu_Collisions2024_v1_2_0), LS 443-452
        '/store/data/Run2024E/Cosmics/RAW/v1/000/381/455/00000/e8278873-33b0-4114-b15b-3e693db7a943.root'
    ],
    381443 : [ #Run2024E, HLTPhysics, Collisions, (L1Menu_Collisions2024_v1_2_0), LS 257-272
        '/store/data/Run2024E/HLTPhysics/RAW/v1/000/381/443/00000/2dd5dd33-b3ae-4ab8-9903-b855655de25f.root',
        '/store/data/Run2024E/HLTPhysics/RAW/v1/000/381/443/00000/d9ebc5ce-b138-46e8-b93a-45cd68f15483.root'
    ],
    381065 : [ #Run2024E, EphemeralHLTPhysics, Collisions, (L1Menu_Collisions2024_v1_2_0), LS ???
        '/store/data/Run2024E/EphemeralHLTPhysics0/RAW/v1/000/381/065/00000/98923c2f-92d0-4022-80bd-4d2928e4d372.root'
    ],
    380346 : [ #Run2024D, EphemeralHLTPhysics, Collisions, (L1Menu_Collisions2024_v1_1_0), LS 180-183
        '/store/data/Run2024D/EphemeralHLTPhysics0/RAW/v1/000/380/346/00000/0022f303-1189-4153-bc42-28a68d2104bb.root',
        '/store/data/Run2024D/EphemeralHLTPhysics0/RAW/v1/000/380/346/00000/0cea2f25-7409-4fbd-a162-f3082088d94d.root',
        '/store/data/Run2024D/EphemeralHLTPhysics0/RAW/v1/000/380/346/00000/c78380b6-65d6-460f-84ae-8ae369bd412e.root',
        '/store/data/Run2024D/EphemeralHLTPhysics0/RAW/v1/000/380/346/00000/4372e803-964a-4062-b3b0-ce0344a18aae.root'
    ],
    379793 : [ # Run2024C, Cosmics (L1Menu_Collisions2024_v1_1_0)
        '/store/data/Run2024C/Cosmics/RAW/v1/000/379/793/00000/7ae3a695-9581-4227-af54-216876989e08.root',
        '/store/data/Run2024C/Cosmics/RAW/v1/000/379/793/00000/2930aed3-7d05-4fc2-abe7-67dfdf0dfd62.root'
    ],
    379728 : [ # Run2024C, Circulating (L1Menu_Collisions2024_v1_1_0)
        '/store/data/Run2024C/MinimumBias/RAW/v1/000/379/728/00000/222c8979-4816-49d8-8929-4bf719555767.root'
    ],
    379070 : [ # Run2024B, Cosmics (L1Menu_Collisions2024_v1_0_0)
        '/store/data/Run2024B/Cosmics/RAW/v1/000/379/070/00000/d844923b-5e69-42ef-8da7-27e7e38591c1.root',
        '/store/data/Run2024B/Cosmics/RAW/v1/000/379/070/00000/ed803fc0-2a96-47d7-b387-4e017cee7946.root'
    ],
    379154 : [ # Run2024B, EphemeralHLTPhysics, 13.6 TeV, 62b colliding, PU ~ 60 (leveling) (L1Menu_Collisions2024_v1_0_0)
        '/store/data/Run2024B/EphemeralHLTPhysics0/RAW/v1/000/379/154/00000/9693f794-3962-4fdf-9625-f434d8dc9729.root',
        '/store/data/Run2024B/EphemeralHLTPhysics0/RAW/v1/000/379/154/00000/cb686c8b-0cb8-4654-ad67-bd69f1c2b2bd.root',
        '/store/data/Run2024B/EphemeralHLTPhysics0/RAW/v1/000/379/154/00000/44098a74-d89f-4440-930f-6778bb470fea.root',
        '/store/data/Run2024B/EphemeralHLTPhysics0/RAW/v1/000/379/154/00000/a31cbad9-22de-43c6-addf-e4c1845cff1b.root',
    ],
    378238 : [ # Fill 9400, Run2024A, HLTPhysics, 2 bunches
        '/store/data/Run2024A/HLTPhysics/RAW/v1/000/378/238/00000/fd49502f-7fca-4325-ba70-9b2ae392aa0f.root',
        '/store/data/Run2024A/HLTPhysics/RAW/v1/000/378/238/00000/fd8984f7-6069-47a0-94a6-b6aeac5ef61e.root',
    ],
}
