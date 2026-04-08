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
    402655:[ # Low PU, test for LumiScan2026
        '/store/data/Run2026C/HLTPhysics/RAW/v1/000/402/655/00000/01dfdecf-9da1-4a2d-bbc7-6fe7bf4f8642.root',
        '/store/data/Run2026C/HLTPhysics/RAW/v1/000/402/655/00000/0364eeca-aecc-4a62-9822-9ebdd452d87c.root',
        '/store/data/Run2026C/HLTPhysics/RAW/v1/000/402/655/00000/0ff5b5e6-6428-4893-883f-465ab660529a.root',
        '/store/data/Run2026C/HLTPhysics/RAW/v1/000/402/655/00000/140a9fe2-205d-45e0-8fe6-e0ca50c7e5b0.root',
        '/store/data/Run2026C/HLTPhysics/RAW/v1/000/402/655/00000/144bb639-46f8-4061-a916-c9ddd4abfa56.root',
        '/store/data/Run2026C/HLTPhysics/RAW/v1/000/402/655/00000/19d06af6-ab94-4127-833f-a037ebbd1b8e.root',
        '/store/data/Run2026C/HLTPhysics/RAW/v1/000/402/655/00000/1b40cb18-936b-4cfa-8b4e-14c48c4a480a.root',
        '/store/data/Run2026C/HLTPhysics/RAW/v1/000/402/655/00000/1cea592b-a59a-42e6-9f26-e2bfc82c22e3.root',
        '/store/data/Run2026C/HLTPhysics/RAW/v1/000/402/655/00000/1e4084fd-3e1f-4f46-8970-0596a5b6ad28.root',
    ],
    402360: [ # Ephemeral HLTPhysics data at L~2.2E34 (PU~64), L1T menu 2026-v1_1_0, ~5K events per file
        '/store/data/Run2026B/EphemeralHLTPhysics0/RAW/v1/000/402/360/00000/98362554-ea94-40e3-b558-fd2a7a72166b.root',
        '/store/data/Run2026B/EphemeralHLTPhysics0/RAW/v1/000/402/360/00000/9a8d32b8-96b1-43cd-b1a9-3edb5d6d98ea.root',
        '/store/data/Run2026B/EphemeralHLTPhysics0/RAW/v1/000/402/360/00000/c35992c4-4b6a-49d6-b215-68d9d764a1cc.root',
    ],
    401871:[ # Low PU fill 11505: 800b, PU=1, SpecialZeroBias
        #'/store/data/Run2026B/SpecialZeroBias0/RAW/v1/000/401/871/00000/97ce8114-4401-4209-8843-34231aa8efe3.root', # {"401871": [[22, 22]]}
        #'/store/data/Run2026B/SpecialZeroBias0/RAW/v1/000/401/871/00000/bf57c7c2-c545-44e8-99f1-ebe4201376c7.root', # {"401871": [[47, 47]]}
        #'/store/data/Run2026B/SpecialZeroBias0/RAW/v1/000/401/871/00000/00e0b8c0-0b22-4c11-a3c1-0ab058d84a2f.root', # {"401871": [[48, 48]]}
        #'/store/data/Run2026B/SpecialZeroBias0/RAW/v1/000/401/871/00000/54b700e6-bf39-40d6-ad05-e0d5e4cf4436.root', # {"401871": [[54, 54]]}
        #'/store/data/Run2026B/SpecialZeroBias0/RAW/v1/000/401/871/00000/df12e221-11b9-4a06-baf5-d82cc2df3a6d.root', # {"401871": [[60, 60]]}
        #'/store/data/Run2026B/SpecialZeroBias0/RAW/v1/000/401/871/00000/dad2506e-b825-4617-ad46-92640e28c568.root', # {"401871": [[61, 61]]}
        #'/store/data/Run2026B/SpecialZeroBias0/RAW/v1/000/401/871/00000/c6361c90-dcc2-4df9-ace2-8fb4dedf0d31.root', # {"401871": [[63, 63]]}
        '/store/data/Run2026B/SpecialZeroBias0/RAW/v1/000/401/871/00000/808bef6c-ef79-4779-b188-71f78a76c666.root', # {"401871": [[68, 68]]}
    ],
    402168:[ # for CMSALCAFAST-144
        '/store/data/Run2026B/HLTPhysics/RAW/v1/000/402/168/00000/0c4eff7b-004a-47f8-87b9-28f7c3637e8e.root', # {"402168": [[433, 607]]}
        '/store/data/Run2026B/HLTPhysics/RAW/v1/000/402/168/00000/1893f23c-9825-425c-907c-2a404959bef1.root', # {"402168": [[252, 432]]}
        '/store/data/Run2026B/HLTPhysics/RAW/v1/000/402/168/00000/1893f23c-9825-425c-907c-2a404959bef1.root', # {"402168": [[252, 432]]}
        '/store/data/Run2026B/HLTPhysics/RAW/v1/000/402/168/00000/969953ed-0b56-4153-b217-f14d5488ead5.root', # {"402168": [[28, 241]]}
        '/store/data/Run2026B/HLTPhysics/RAW/v1/000/402/168/00000/d5b38e9f-cbae-414d-920c-ad676eee6017.root', # {"402168": [[242, 251]]}
    ],
    402263:[ # Run took with the L1Menu_Collisions2026_v1_1_0
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/0103aa88-46b9-4034-ba95-97b2d0776e82.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/01f9d5f7-9d20-4e62-a2fc-fb89808993d2.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/04fc2aa0-fc4b-403c-ae8d-ba39fe453f98.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/0730510a-0393-4507-9917-98d782004ea7.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/08362c84-d58c-44e5-abcb-c51afc24d74a.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/0a6af1cd-fc58-408e-9b3a-eb1461f64b09.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/0cf51876-4db2-48fb-ae0f-ce32b72e5822.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/0dd816a0-ea39-4bd0-92f4-32e44afe6bfa.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/0e38f281-b314-4932-aaa5-6b716a4b8db5.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/163ce440-6895-447b-a9bf-80c3f65f2e29.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/1c8fd2e0-4fdf-44af-83d9-c92c984a7430.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/1d509971-af3d-4022-bb56-c9d4fc7c1321.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/1dc03a20-bab0-4d52-9b51-536936b767d6.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/22c46874-5be4-4358-8675-770625fc0e58.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/2737dddc-8de8-49e8-b5ca-b6d9f8630876.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/29c8c56a-40f1-457c-8a26-2e94d03fdc54.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/316c3f65-7b81-48de-ba56-c9a218aaf1c0.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/32c28d9a-c893-4c76-9d7b-135960247b70.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/363fc4cf-09bf-48af-9d63-8ee1bdcd35ce.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/3c6c4715-02b7-42e6-8c3c-7470d9c11e36.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/3e3d4182-630f-4f22-85a4-2654bc66c170.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/40eede9d-2458-4a9a-a4ae-410b33fe43e3.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/43ea7d2d-b1dc-4eca-90a4-0a3e484ad7a9.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/441d22e9-4edd-4f85-ae7c-d76d8c73e1a6.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/45c1835f-9cea-4a2a-bab3-486f6313b114.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/4cd96038-6970-463c-9b78-b0d8541a0f22.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/4e1e66ab-49f3-4381-b4b8-9f7d35a7e9ea.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/4e4c702c-d55a-41ff-b452-6af6fe14494a.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/51420a4a-9bda-4157-bbe0-aaa200ec38ac.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/54ebae6f-8beb-4931-b7e1-d659cc25778f.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/5f0df9fa-1848-4fe0-8854-cbe18c9f1b2e.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/600e125c-9acc-4bbd-89ff-dabed52b7260.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/615bfefc-377f-4d3b-a69a-7c72701c5f46.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/61983e78-5996-4be0-8f95-86949d4efb7d.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/62e63072-acbd-493d-89b0-6efc319cf23a.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/67ad707a-5c71-4143-b636-4432f18cc77c.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/69d0fa99-0f7d-41af-a62b-4560c156411b.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/6fda11c3-e623-4424-9c53-e30426375dc2.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/735dad39-fe45-47c3-aa80-76ea75276dab.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/7386fe4b-4bd7-44a5-851f-44304cccf0fd.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/74802c2e-f147-48b0-aee8-d30bc1d623d2.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/795889dc-6262-4d70-96c3-068ae81ac602.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/7d5ef0d2-b0eb-4c09-a1fe-9095ff0bbace.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/7d7422b6-c74b-40bb-8f9f-0b287906f4d8.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/7fadd216-e68c-461a-a1e9-57615bbc2aab.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/8337929f-0d69-4a33-80c7-896a421e6f0f.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/84920a3f-c76a-441d-9913-9e8d1c3a1666.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/871953f3-b77f-417b-92c5-e82436e05dd1.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/899cdd0b-1647-41f1-9f17-953f7728efb6.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/8ff0b6a2-0c3a-4bcc-83d1-0e03a35462bb.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/953b7517-4db3-4331-aed0-6cf5352624d0.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/95da0dcb-3189-479e-907a-3732e582a059.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/9eafe9ca-cdda-43e8-864d-6b4745f405d4.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/9ee16b30-d909-4986-9242-d136a1bb9121.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/a05d9a88-b5a6-49bf-86f6-7ef766f01a05.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/a13f5ebe-6f5e-4cd6-81d8-2f99309eb786.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/a1ef66c4-6de6-44d6-8039-7325aa319829.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/a317c03a-ed7a-42ed-a6da-897ad4a023bc.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/a460de51-2043-41da-b6d2-bdf77e4db1a2.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/ab245eb0-a4eb-47f8-a98a-83e234c2d520.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/ad42f03e-e350-4a69-8ff5-ee3b9c18a25a.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/ae29cf9e-8fb5-499a-b31e-abb6a75d578d.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/b01530c5-f0bd-4189-b39e-d05c6873e5d1.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/b0656059-ce7f-4543-a63d-203169d293ac.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/b1b711b8-775b-4ec1-b988-3a3fb2b1cec0.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/b29efebf-aa9a-4a59-83df-a03229515031.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/b40f79cb-ba61-4d9a-831d-bb69c15afce0.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/b4760a1f-7c35-4b02-a6ff-1f79de8d6816.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/b4a002f6-82fe-4871-8962-e56a06d9a6b8.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/bd2fffc0-5143-41d2-a441-55b251632083.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/bd966f2a-2e80-4941-92af-07cbb9d79c63.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/be5b0b62-4067-4478-a785-a96be84bbf56.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/bedfd561-ae23-45b5-8c88-265316073392.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/c1eb130c-2229-4a7a-8b36-4e5c2d7e4a48.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/c467c14f-7c69-40f5-b7d8-c3f3bf449e5b.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/c4fb38bd-1b30-4e88-a0f6-7225323c791d.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/c52f95de-081c-440d-9eb9-91c10154897e.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/c583503f-261e-40bf-af25-9955bc621266.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/caa1eadb-637b-467f-a8d8-d75722445eac.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/cb642217-ac7a-4b42-89e6-6f1bd5b063d0.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/cb6d29f0-4cdd-4a39-b44f-beaeb2f47ad1.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/cd6abec7-e003-4dd5-b8b7-bb6f0f196669.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/ce44ef54-b2ed-471b-a6be-1c64b6465e42.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/cfafa4c0-83d9-4309-a13e-5581da0aec4d.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/cff51607-0f87-4592-8f22-1628fb0aae7f.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/d14b4819-3cc8-4546-923d-12b740a258a8.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/d18f196b-1291-4011-9875-145807e8055d.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/d249bfa6-6536-4078-98f8-71b40d40cc07.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/d67c1b1e-0035-4e13-9363-003b7df82bfe.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/db4bb8e8-b441-4e81-af0a-5de3ea9649ec.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/dfb40da3-8c6a-40db-8d53-06d4c1da7384.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/e18d26b6-0e66-4100-aa82-ab13d845749d.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/e2363930-f1d9-4fdc-9a8f-9c9c4638f5d0.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/e311bf1d-96e9-41e2-9c4b-4d30ee1fa081.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/e3178ebc-9c63-4aee-9d41-250ee3082d70.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/e8ec0c6b-423e-477f-b8b8-f726473d9c85.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/ec53e2d1-9eb9-46ea-aeab-4935a20030d2.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/f0a2af56-349a-403d-a406-dac99d913db0.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/f40328b3-6173-4e1b-9320-6e8a895b68de.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/f5b3fb40-604a-4f13-9160-9802dc8b7096.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/f6f02419-860c-460f-bd4b-c55628637602.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/f758b846-a4bb-4edc-bbca-ce175ecd14eb.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/fa177137-b816-4cbf-8a02-b078de1c19f9.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/402/263/00000/fb96fb6c-d672-4396-b0c5-511a787a8fb0.root',
    ],
    402069:[
        '/store/data/Run2026B/HLTPhysics/RAW/v1/000/402/069/00000/09036320-d8a1-4745-acbe-6bdd601e76a2.root',
        '/store/data/Run2026B/HLTPhysics/RAW/v1/000/402/069/00000/8dc16d39-01bf-43f0-a749-d387f101b1c4.root',
        '/store/data/Run2026B/HLTPhysics/RAW/v1/000/402/069/00000/7b114ca2-1716-4aff-9bcf-ce0570ed2401.root',
    ],
    401973:[
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/401/973/00000/a70db169-c7ec-4609-93a4-f27cae0111a6.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/401/973/00000/add69c1c-9081-48ea-80a4-ab5843933051.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/401/973/00000/ea605334-6bcb-49d5-8701-0e7915c75081.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/401/973/00000/03dad30c-11c4-400f-89f5-a1d1fe59c098.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/401/973/00000/d6e9945e-505d-453f-bfb1-2f60967d1010.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/401/973/00000/4d5db2ef-839e-4ef5-b888-f9ebaf2274d0.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/401/973/00000/713de40c-5a4b-4288-94f1-2a7a5fe8299b.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/401/973/00000/6a3d3447-46df-47eb-a4ed-f6889d80b49d.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/401/973/00000/41e8f724-1243-4e48-a2d1-2ce1c7aaabb6.root',
        '/store/data/Run2026B/ZeroBias/RAW/v1/000/401/973/00000/41e8f724-1243-4e48-a2d1-2ce1c7aaabb6.rootb912dfb5-4606-4f9d-a27d-b9332bc27f01.root',
    ],
    401867:[ #MiniDAQ (EcalCalibration), Run2026A, run 401704 (to test EcalCalibration MiniDAQ menu)
       '/store/data/Run2026B/EphemeralHLTPhysics6/RAW/v1/000/401/867/00000/37b2abd2-b76d-40da-a234-265faa3c9624.root',
    ],
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
