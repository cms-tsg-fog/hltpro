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
    381455 : [ # Run2024E, Cosmics (L1Menu_Collisions2024_v1_2_0), LS 443-452
        '/store/data/Run2024E/Cosmics/RAW/v1/000/381/455/00000/e8278873-33b0-4114-b15b-3e693db7a943.root'
    ],
    381065 : [ #Run2024E, EphemeralHLTPhysics, Collision, (L1Menu_Collisions2024_v1_2_0), LS ???
        '/store/data/Run2024E/EphemeralHLTPhysics0/RAW/v1/000/381/065/00000/98923c2f-92d0-4022-80bd-4d2928e4d372.root'
    ],
    380346 : [ #Run2024D, EphemeralHLTPhysics, Collision, (L1Menu_Collisions2024_v1_1_0), LS 180-183
        '/store/data/Run2024D/EphemeralHLTPhysics0/RAW/v1/000/380/346/00000/0022f303-1189-4153-bc42-28a68d2104bb.root',
        '/store/data/Run2024D/EphemeralHLTPhysics0/RAW/v1/000/380/346/00000/0cea2f25-7409-4fbd-a162-f3082088d94d.root',
        '/store/data/Run2024D/EphemeralHLTPhysics0/RAW/v1/000/380/346/00000/c78380b6-65d6-460f-84ae-8ae369bd412e.root',
        '/store/data/Run2024D/EphemeralHLTPhysics0/RAW/v1/000/380/346/00000/4372e803-964a-4062-b3b0-ce0344a18aae.root'
    ],
    379793 : [ # Run2024C, Cosmics (L1Menu_Collisions2024_v1_1_0)
        '/store/data/Run2024C/Cosmics/RAW/v1/000/379/793/00000/7ae3a695-9581-4227-af54-216876989e08.root',
        '/store/data/Run2024C/Cosmics/RAW/v1/000/379/793/00000/2930aed3-7d05-4fc2-abe7-67dfdf0dfd62.root'
    ],
    379729 : [ # Run2024C, HLTPhysics, Collisions, (L1Menu_Collisions2024_v1_1_0, LS 194-205)
        'root://eoscms.cern.ch//eos/cms/tier0/store/data/Run2024C/HLTPhysics/RAW/v1/000/379/729/00000/9a4c061e-39e4-496a-9cb6-285be4b77367.root',
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
    375013 : [ # Fill 9247, Run2023HI, HLTPhysics, 1240 bunches
        '/store/hidata/HIRun2023A/HIHLTPhysics/RAW/v1/000/375/013/00000/fcb1850b-1898-4b18-b23d-d0a754595286.root',
        '/store/hidata/HIRun2023A/HIHLTPhysics/RAW/v1/000/375/013/00000/fb3ea037-cc5c-462c-ae04-120cd5bf87b4.root',
        '/store/hidata/HIRun2023A/HIHLTPhysics/RAW/v1/000/375/013/00000/f6f42064-1626-41b8-96f8-21ef049d2784.root',
    ],
    374833 : [ # Fill 9235, LS 87--180
        '/store/hidata/HIRun2023A/HIHLTPhysics/RAW/v1/000/374/833/00000/1a9230ee-f58b-44c2-b835-c4f5f75287db.root',
        '/store/hidata/HIRun2023A/HIHLTPhysics/RAW/v1/000/374/833/00000/309bea77-bec9-47e2-99dd-d223c8707b26.root',
        '/store/hidata/HIRun2023A/HIHLTPhysics/RAW/v1/000/374/833/00000/3e98e93e-4a9c-4955-a76f-6e18f2e6be05.root',
    ],
    371290 : [ # Run2023D, Cosmics
        '/store/data/Run2023D/Cosmics/RAW/v1/000/371/290/00000/00a5ef35-50bc-4140-8e23-5d06e43e3e02.root',
    ],
    370772 : [ # Run2023D, HLTPhysics, 13.6 TeV, 2400 bunches, PU 60
        '/store/data/Run2023D/HLTPhysics/RAW/v1/000/370/772/00000/a9e5dc8f-b4fe-407a-9f3e-918c8bd28ecb.root',
    ],
    370293 : [ # Run2023D, EphemeralHLTPhysics, 13.6 TeV, 2400 bunches, PU 60
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/003420ea-0f24-49f4-a69f-0528ffc517c2.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/038c7164-4c63-4177-951d-f65245674bc7.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/0b4e0b14-114c-4df8-8acf-698ccff2eab0.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/0dcc270a-8d36-4ad3-a089-91f7faaa5b5e.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/15fa65ed-bda1-44e0-b3d7-6d9fc92a814d.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/1c5aa037-9741-433e-b410-ec1b5afb1862.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/1f498e17-9b99-49ef-98cc-6226889e2e98.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/1ffc726e-c612-470d-b734-590fc00d5452.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/20190ed0-d7fb-437c-b153-1d081f66ed0d.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/29c565a4-6179-497a-a9e4-6dfdedb60388.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/2a065f65-89c7-45d3-8b02-edd3547f0023.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/2b3bfb0d-4296-470b-a1e2-ce5a72dc8a67.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/2ba6996f-4ee2-4dd7-9e29-b4ff42fb437a.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/2e11918b-1e89-4b23-ae81-3d1c4143df6e.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/2e6b78d6-076a-463c-9dde-8db4ed3df18d.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/2ef73d2a-1fb7-4dac-9961-149525f9e887.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/2fe5a660-3cdc-4906-95a8-cac4986cc074.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/303b0104-65f3-4518-8b32-8de062eb9713.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/337c6812-59fb-4928-bd3a-5a94c904e6ba.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/383667b7-89b0-47b2-8d84-83b978a92306.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/39c49848-e9a8-44e6-b300-0f5282108834.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/3b6036e6-2828-4856-9248-052b7590d8e0.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/3d993222-fd69-4e88-95ed-05c8cc015dd3.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/49bfd744-78c2-4120-966c-4fccca21e566.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/4b220aed-1f8d-4e7d-becf-8fb5d97532e8.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/4bfaf0f7-b665-4e42-8f5a-f7e3946f344d.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/51a35728-d172-4dda-be38-a1654f9525fe.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/5205fe59-16d9-4487-88c1-29566acb7ef0.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/55e5744e-5e0c-4d33-861b-63eff4e14343.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/56fca96f-67fb-4b51-a23a-4399a8eb3110.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/5ae644b2-4576-4e55-b92e-462e510ddaea.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/5ba7ce4a-212f-40ab-889c-e3215ddc5e82.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/5befa192-fff9-4eab-8a7b-fabdaf28aa6a.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/5e01ba3a-43ae-4716-990b-232d6e4d814a.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/6010ed5e-02a1-4f8e-a385-4b1783e93466.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/60307005-e4e1-4773-935f-d8c8a4ec2626.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/61549890-4715-4e93-8364-6ffd97cff1e9.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/63424247-e3a9-498e-ba77-774bc159b5ce.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/654408a3-0a98-4ed6-974c-a551b1af12ea.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/66464463-95bf-4795-8fef-af0e4e7f6c10.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/6c0b88ca-1a2f-42ce-bb05-e957101cc81c.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/6c60046c-011f-4716-821e-dc97c3da4841.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/732a83e3-dfeb-4a51-8232-bd77bcd8a1e0.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/78224bc0-18ca-44f1-ab7e-a2a79c0df67d.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/79ec6a68-565f-45c3-b2e6-35115301ca03.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/7aef00d1-f079-4840-a119-d60721d9d4f0.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/7c34f606-fb19-465a-8f5d-1c6843f85fef.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/7d88f451-f210-4229-94c4-b735d13961d2.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/8250dc85-e842-4fbf-bf1d-9bf7c109885a.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/8292e2f8-be91-4bbb-97f1-3a7457b8c89b.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/844f7f54-f1cd-4903-94a6-20b4d689a827.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/888ec56a-1f88-40c8-9399-f1cf65d0d05d.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/9008956d-e11f-4714-95bd-aa1f4e55ce4e.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/937740e0-278a-4b68-9593-261b3fdaee1c.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/98130d7e-01a4-4d90-915d-fde5ae3dbc5a.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/985951ed-cfb0-45ea-8b9a-9bc64cab308b.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/999db197-953e-4810-8723-d1bfbe9e1629.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/9bc5e69b-10ea-4e94-8c6e-994a86fc70e3.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/9dc25bb7-70e4-4c19-a4c8-87e6f3392311.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/a1627ede-c15b-46c4-8007-d7fc804b4644.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/a36f9833-572d-4250-befe-6b3fae9e62db.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/a468847e-15de-4abf-b882-4158c84158c0.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/a7cfd540-360f-41d9-8150-5ca10b7ad421.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/acc0b880-4b37-4ab4-8b42-5499dcbd3cfc.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/b5fd6d6e-d206-49ce-a0f6-d17e78da1b05.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/b7b91a4e-04b3-4cc7-abf9-d029d0504f6c.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/b965e270-fe36-409f-9406-c7bfdf9d3727.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/bf712f3f-8aa8-4848-b799-984658c7e363.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/c5969a31-adf2-482f-b726-8c67d34b490a.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/cb01e961-95fd-4314-9043-ef0409e651f6.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/cde9f2b6-6a2a-47e9-a688-4fe4257873d6.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/cf494d41-357b-495a-a601-bb302ffcac8a.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/d13addb4-6141-4302-9de9-02a6d95e9d38.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/d32ef0d1-d7da-481f-a923-732cfe84700f.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/d50e07c5-857c-47f9-8d17-234306f00a25.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/db72e4d1-6c13-47de-921b-0e979756ea11.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/dcd87c26-eaff-4a51-8324-95fe4c5dd669.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/de5574f5-5dca-4c76-967a-7fd9a16ab859.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/df135216-fa3d-498b-b9c3-1e6ccf9c48cb.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/e267383d-60b8-4797-a2f3-3f1740f5167d.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/e3952f1c-179f-4d59-9847-681bd6f05512.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/e4af223f-23c3-4ec2-b8fa-7a1248fdcac8.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/ebb16358-1326-491c-b358-41af54acedc2.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/ec599caf-fae9-421b-aa38-17cb77d37a2c.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/edede9fc-2562-4589-b550-0fb3ac3e8487.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/f0504d77-7eeb-4e67-8325-3199e095dabb.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/f26c22bf-b2f0-4018-8f25-ac18c593d522.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/f307a0a4-3d9e-4959-88df-bafb2e42c209.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/fac6c3e6-ac1b-4dc1-9567-942700de3439.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/fb23cad9-f67f-4f42-92ad-2b78c9593c49.root',
        '/store/data/Run2023D/EphemeralHLTPhysics0/RAW/v1/000/370/293/00000/fe18a230-171a-47ff-b3a3-af0d2c4ee067.root',
    ],
    369956 : [ # Run2023D, SpecialZeroBias data
        '/store/data/Run2023D/SpecialZeroBias0/RAW/v1/000/369/956/00000/0b236b9e-57da-4d5d-8ab6-bbac5f6f17f2.root'
    ],
    369596 : [ # Run2023C, TOTEM run
        '/store/data/Run2023C/HLTPhysics/RAW/v1/000/369/596/00000/60925a12-e21d-4df7-80d7-82b8021a9340.root'
    ],
    369339 : [ # Run2023C, Cosmics
        '/store/data/Run2023C/Cosmics/RAW/v1/000/369/339/00000/8fd811e1-e622-4b3c-a35b-86faa0875eb5.root',
    ],
    367910 : [ # Run2023C, 13.6 TeV, 2400 bunches, for the June HLT DOC Tutorial
        '/store/data/Run2023C/HLTPhysics/RAW/v1/000/367/910/00000/89ed2513-ade2-4971-8f97-28a87bbafc22.root',
    ],
    367771 : [ # Run2023C, 13.6 TeV, 2400 bunches, PU 60
        '/store/data/Run2023C/EphemeralHLTPhysics0/RAW/v2/000/367/771/00000/f9ced4c2-6587-40b4-836b-8dd2f8170fbc.root',
        '/store/data/Run2023C/EphemeralHLTPhysics0/RAW/v2/000/367/771/00000/fcd1dad5-b33b-4b58-891d-32b6baafbef1.root',
        '/store/data/Run2023C/EphemeralHLTPhysics0/RAW/v2/000/367/771/00000/fceeb6eb-eabb-43be-8744-26e7d60ea50b.root',
    ],
    367667 : [ # Run2023C, Cosmics
        '/store/data/Run2023C/Cosmics/RAW/v1/000/367/667/00000/d398f7c0-d76a-4f62-82a4-6ca8c4b3af78.root',
    ],
    367262 : [ # Run2023C, EphemeralHLTPhysics, 13.6 TeV, 1800 bunches
        '/store/data/Run2023C/EphemeralHLTPhysics0/RAW/v1/000/367/262/00000/e4b8c5ee-35a7-42f9-b956-295902b1a879.root',
    ],
    366875 : [
        '/store/data/Run2023B/EGamma0/RAW/v1/000/366/895/00000/baef5b0a-48ba-4b99-86d8-61449551d128.root',
    ],
    366729 : [
        '/store/data/Run2023B/EphemeralZeroBias0/RAW/v1/000/366/729/00000/004148e5-7796-4476-93b4-cd0f775b59bd.root',
    ],
    366504 : [ # Run2023B, 13.6 TeV stable beams, 75b fill
        '/store/data/Run2023B/EphemeralHLTPhysics13/RAW/v1/000/366/504/00000/a13518f4-7261-43fb-b8a4-b3377c3c5e04.root',
    ],
    366451 : [ # Run2023B, 13.6 TeV stable beams, 12b fill
        '/store/data/Run2023B/EphemeralZeroBias0/RAW/v1/000/366/451/00000/06d3f724-cdb8-455f-8ba7-dbe2652ca526.root',
        '/store/data/Run2023B/EphemeralZeroBias0/RAW/v1/000/366/451/00000/09662c68-7df8-4524-996b-ad53a92e98dc.root',
    ],
    366043 : [
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
    ],
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
