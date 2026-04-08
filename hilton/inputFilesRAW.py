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
    402655: [ # Low PU, test for LumiScan2026
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
    402538: [ #ls to 66
        '/store/data/Run2026C/HLTPhysics/RAW/v1/000/402/538/00000/abb838b8-65cd-48ac-982d-308e0f47f4d8.root',
        '/store/data/Run2026C/HLTPhysics/RAW/v1/000/402/538/00000/dcc0eba1-9df0-4d65-9883-67efb4b2ecf4.root',
    ],
    402419: [ #402419, LS 81 to 118
        '/store/data/Run2026B/Commissioning/RAW/v1/000/402/419/00000/bc5c7aed-4526-4656-a680-92a22eb925be.root',
        '/store/data/Run2026B/HLTPhysics/RAW/v1/000/402/419/00000/6c113e15-909d-4c36-af4f-c1db53826d72.root',
    ],
    402360: [ # Ephemeral HLTPhysics data at L~2.2E34 (PU~64), L1T menu 2026-v1_1_0, ~5K events per file
        '/store/data/Run2026B/EphemeralHLTPhysics0/RAW/v1/000/402/360/00000/98362554-ea94-40e3-b558-fd2a7a72166b.root',
        '/store/data/Run2026B/EphemeralHLTPhysics0/RAW/v1/000/402/360/00000/9a8d32b8-96b1-43cd-b1a9-3edb5d6d98ea.root',
        '/store/data/Run2026B/EphemeralHLTPhysics0/RAW/v1/000/402/360/00000/c35992c4-4b6a-49d6-b215-68d9d764a1cc.root',
    ],
    402263: [ # Run took with the L1Menu_Collisions2026_v1_1_0
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
    402168: [ # for CMSALCAFAST-144
        '/store/data/Run2026B/HLTPhysics/RAW/v1/000/402/168/00000/0c4eff7b-004a-47f8-87b9-28f7c3637e8e.root', # {"402168": [[433, 607]]}
        '/store/data/Run2026B/HLTPhysics/RAW/v1/000/402/168/00000/1893f23c-9825-425c-907c-2a404959bef1.root', # {"402168": [[252, 432]]}
        '/store/data/Run2026B/HLTPhysics/RAW/v1/000/402/168/00000/1893f23c-9825-425c-907c-2a404959bef1.root', # {"402168": [[252, 432]]}
        '/store/data/Run2026B/HLTPhysics/RAW/v1/000/402/168/00000/969953ed-0b56-4153-b217-f14d5488ead5.root', # {"402168": [[28, 241]]}
        '/store/data/Run2026B/HLTPhysics/RAW/v1/000/402/168/00000/d5b38e9f-cbae-414d-920c-ad676eee6017.root', # {"402168": [[242, 251]]}
    ],
    402069: [
        '/store/data/Run2026B/HLTPhysics/RAW/v1/000/402/069/00000/09036320-d8a1-4745-acbe-6bdd601e76a2.root',
        '/store/data/Run2026B/HLTPhysics/RAW/v1/000/402/069/00000/8dc16d39-01bf-43f0-a749-d387f101b1c4.root',
        '/store/data/Run2026B/HLTPhysics/RAW/v1/000/402/069/00000/7b114ca2-1716-4aff-9bcf-ce0570ed2401.root',
    ],
    401973: [
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
    401871: [ # Low PU fill 11505: 800b, PU=1, SpecialZeroBias
        #'/store/data/Run2026B/SpecialZeroBias0/RAW/v1/000/401/871/00000/97ce8114-4401-4209-8843-34231aa8efe3.root', # {"401871": [[22, 22]]}
        #'/store/data/Run2026B/SpecialZeroBias0/RAW/v1/000/401/871/00000/bf57c7c2-c545-44e8-99f1-ebe4201376c7.root', # {"401871": [[47, 47]]}
        #'/store/data/Run2026B/SpecialZeroBias0/RAW/v1/000/401/871/00000/00e0b8c0-0b22-4c11-a3c1-0ab058d84a2f.root', # {"401871": [[48, 48]]}
        #'/store/data/Run2026B/SpecialZeroBias0/RAW/v1/000/401/871/00000/54b700e6-bf39-40d6-ad05-e0d5e4cf4436.root', # {"401871": [[54, 54]]}
        #'/store/data/Run2026B/SpecialZeroBias0/RAW/v1/000/401/871/00000/df12e221-11b9-4a06-baf5-d82cc2df3a6d.root', # {"401871": [[60, 60]]}
        #'/store/data/Run2026B/SpecialZeroBias0/RAW/v1/000/401/871/00000/dad2506e-b825-4617-ad46-92640e28c568.root', # {"401871": [[61, 61]]}
        #'/store/data/Run2026B/SpecialZeroBias0/RAW/v1/000/401/871/00000/c6361c90-dcc2-4df9-ace2-8fb4dedf0d31.root', # {"401871": [[63, 63]]}
        '/store/data/Run2026B/SpecialZeroBias0/RAW/v1/000/401/871/00000/808bef6c-ef79-4779-b188-71f78a76c666.root', # {"401871": [[68, 68]]}
    ],
    401867: [
       '/store/data/Run2026B/EphemeralHLTPhysics6/RAW/v1/000/401/867/00000/37b2abd2-b76d-40da-a234-265faa3c9624.root',
    ],
    401733: [ # HLTPhysics, Run2026A, run 401733 (830b fill 11481, LS = 499-513)
       '/store/data/Run2026A/HLTPhysics/RAW/v1/000/401/733/00000/d5b8a312-5230-469a-a451-d199e74012c2.root',
    ],
    401704: [ # MiniDAQ (EcalCalibration), Run2026A, run 401704 (to test EcalCalibration MiniDAQ menu)
       '/store/data/Run2026A/MiniDaq/RAW/v1/000/401/704/00000/d9b97556-58be-49f7-875d-6ebda38bf75d.root',
    ],
    401699: [ # Run2026A collisions ZeroBias
        '/store/data/Run2026A/ZeroBias/RAW/v1/000/401/699/00000/d766932c-26b6-4299-9edd-1c96a8da2ab3.root',
        '/store/data/Run2026A/ZeroBias/RAW/v1/000/401/699/00000/28377208-e0ea-415b-95aa-510bf6212b2e.root',
    ],
    401693: [ # 400b HLTPhysics
        '/store/data/Run2026A/HLTPhysics/RAW/v1/000/401/693/00000/a3749f6d-5c9b-421b-9929-764674135dcb.root',
        '/store/data/Run2026A/HLTPhysics/RAW/v1/000/401/693/00000/a395cac6-bc83-4258-9eb2-aec188bed0d1.root',
        '/store/data/Run2026A/HLTPhysics/RAW/v1/000/401/693/00000/a7f31833-6aaa-4528-aaae-5f55709cff60.root',
        '/store/data/Run2026A/HLTPhysics/RAW/v1/000/401/693/00000/a8653375-45ff-4b12-82d8-8ecde8105937.root',
        '/store/data/Run2026A/HLTPhysics/RAW/v1/000/401/693/00000/aae4fecc-4b07-42d0-90eb-5da00cc12f0b.root',
        '/store/data/Run2026A/HLTPhysics/RAW/v1/000/401/693/00000/ab22f432-cbc5-4740-af48-5434b956646e.root',
        '/store/data/Run2026A/HLTPhysics/RAW/v1/000/401/693/00000/b09751c7-02bb-4390-b61f-61a5a316d76f.root',
        '/store/data/Run2026A/HLTPhysics/RAW/v1/000/401/693/00000/b20d338e-4c3d-42f7-a8a3-da3e96145020.root',
        '/store/data/Run2026A/HLTPhysics/RAW/v1/000/401/693/00000/ba18d2b7-a29e-484b-adf7-724372c670f9.root',
        '/store/data/Run2026A/HLTPhysics/RAW/v1/000/401/693/00000/bb4911b7-1915-439a-b137-756ae58a5921.root',
        '/store/data/Run2026A/HLTPhysics/RAW/v1/000/401/693/00000/bd66c8a9-25b4-4859-b1f5-28ea5b2b614e.root',
        '/store/data/Run2026A/HLTPhysics/RAW/v1/000/401/693/00000/c03663a9-abcd-4fae-8018-5798d7e9441f.root',
        '/store/data/Run2026A/HLTPhysics/RAW/v1/000/401/693/00000/c120e71d-e5cc-413c-b996-32ca45164de9.root',
        '/store/data/Run2026A/HLTPhysics/RAW/v1/000/401/693/00000/c9864a94-a81a-432a-95b5-0c4fdfbce5a4.root',
    ],
    401669: [
        '/store/data/Run2026A/HLTPhysics/RAW/v1/000/401/669/00000/07cc3f2b-1579-4466-b6f0-68b1030f5964.root',
        '/store/data/Run2026A/HLTPhysics/RAW/v1/000/401/669/00000/16dea94d-defb-48fd-b5d6-db10dc9cfea4.root',
        '/store/data/Run2026A/HLTPhysics/RAW/v1/000/401/669/00000/2299fa61-ffd9-4b09-9ba8-09cbdf416aee.root',
        '/store/data/Run2026A/HLTPhysics/RAW/v1/000/401/669/00000/43d2d946-2669-4e42-95a7-b704288d350d.root',
        '/store/data/Run2026A/HLTPhysics/RAW/v1/000/401/669/00000/5118436a-df34-4030-8720-8b9a87c15640.root',
        '/store/data/Run2026A/HLTPhysics/RAW/v1/000/401/669/00000/5fc9a73b-f573-4030-9e56-5945bad51747.root',
        '/store/data/Run2026A/HLTPhysics/RAW/v1/000/401/669/00000/80fb0fef-976e-40a6-9319-d4498ecbd39a.root',
        '/store/data/Run2026A/HLTPhysics/RAW/v1/000/401/669/00000/89fec21f-a1a3-465e-8938-42cda4f0bfab.root'
    ],
    401642: [ # test for BSRT fill, CMSHLT-3773
        #'/store/data/Run2026A/HLTPhysics/RAW/v1/000/401/642/00000/af895d48-58aa-4ce7-ade1-d64629254051.root',
        #'/store/data/Run2026A/HLTPhysics/RAW/v1/000/401/642/00000/fe3f314c-add9-451e-a999-5bdcec6f6bd9.root'
        '/store/data/Run2026A/ZeroBias/RAW/v1/000/401/642/00000/b0c6c02b-1902-4a48-8ab3-555a85f1609a.root',
        '/store/data/Run2026A/ZeroBias/RAW/v1/000/401/642/00000/b1b3c586-ad82-4ff7-86c8-47a7e00ca8ae.root',
        '/store/data/Run2026A/ZeroBias/RAW/v1/000/401/642/00000/b1df2de9-fea2-4d4d-88d3-b993b5fbb5a7.root',
        '/store/data/Run2026A/ZeroBias/RAW/v1/000/401/642/00000/b216821b-37c8-4223-993d-c7a9b6766bd3.root',
        '/store/data/Run2026A/ZeroBias/RAW/v1/000/401/642/00000/b24aa9e6-d413-459d-910f-b6c058501c1e.root',
        '/store/data/Run2026A/ZeroBias/RAW/v1/000/401/642/00000/b2b270cf-7448-4faa-a345-928b4cb929cd.root',
        '/store/data/Run2026A/ZeroBias/RAW/v1/000/401/642/00000/b35fc480-9676-4743-8425-104b2204f12d.root',
        '/store/data/Run2026A/ZeroBias/RAW/v1/000/401/642/00000/b36cb44c-69ee-4b42-b516-c7c7b62ce4a2.root',
        '/store/data/Run2026A/ZeroBias/RAW/v1/000/401/642/00000/b39a1347-0840-483d-b0f0-211008d7db49.root',
        '/store/data/Run2026A/ZeroBias/RAW/v1/000/401/642/00000/b3da9440-ebfc-4709-8df7-c0799fc938e7.root',
        '/store/data/Run2026A/ZeroBias/RAW/v1/000/401/642/00000/b4173b36-0e13-4a96-a73a-7bd91960991b.root',
        '/store/data/Run2026A/ZeroBias/RAW/v1/000/401/642/00000/b50438c9-2710-4719-8745-add64fea6bf0.root',
        '/store/data/Run2026A/ZeroBias/RAW/v1/000/401/642/00000/b508e824-5b0d-4bc0-ab14-93adb19fc164.root',
        '/store/data/Run2026A/ZeroBias/RAW/v1/000/401/642/00000/b5bc4b97-04d6-408b-83e5-18f61b710d4c.root',
        '/store/data/Run2026A/ZeroBias/RAW/v1/000/401/642/00000/b603191b-8884-45ad-a451-76e29fac7102.root',
        '/store/data/Run2026A/ZeroBias/RAW/v1/000/401/642/00000/b627629d-98bd-41f6-aa91-d460ae2c9b3a.root',
    ],
    401628: [ #Cosmics, Run2026A, run 401628 (LS = 17-31, all detectors IN and with HV ON)
       '/store/data/Run2026A/Cosmics/RAW/v1/000/401/628/00000/cadc68ba-b807-4548-a4fb-509babe06ba1.root',
    ],
    401420: [ #MiniDAQ (EcalCalibration), Commissioning2026, run 401420 (to test EcalCalibration MiniDAQ menu)
       '/store/data/Commissioning2026/MiniDaq/RAW/v1/000/401/420/00000/bfa68be5-7ac4-4d80-a3da-3a386faae421.root',
    ],
    401411: [
        '/store/data/Commissioning2026/HLTPhysics/RAW/v1/000/401/411/00000/9a7ac0d9-c8a6-445a-84ac-50eff0dab0a2.root',
        '/store/data/Commissioning2026/HLTPhysics/RAW/v1/000/401/411/00000/ce73f96f-7b59-425d-a4f2-599e66fc4d41.root',
    ],
    401382: [
        '/store/data/Commissioning2026/HLTPhysics/RAW/v1/000/401/382/00000/7c7b2024-6962-4528-b0c7-42ff4d9ec55d.root',
    ],
    401368: [
        '/store/data/Commissioning2026/HLTPhysics/RAW/v1/000/401/368/00000/3e38725d-1765-40f8-ab71-44969f624799.root',
        '/store/data/Commissioning2026/HLTPhysics/RAW/v1/000/401/368/00000/8a1c7ebf-f4f5-4e21-8ced-72d3ee16c125.root',
    ],
    401311: [
        '/store/data/Commissioning2026/HLTPhysics/RAW/v1/000/401/311/00000/78fd6524-bea9-4b66-9f7d-104835470efe.root',
        '/store/data/Commissioning2026/HLTPhysics/RAW/v1/000/401/311/00000/99b5790a-eeb4-4157-bee2-faba237b91ae.root',
        '/store/data/Commissioning2026/HLTPhysics/RAW/v1/000/401/311/00000/ce94ba24-7dd8-4085-b75d-9b0e292a5471.root',
        '/store/data/Commissioning2026/HLTPhysics/RAW/v1/000/401/311/00000/f988631d-e16e-469c-86e9-d65786c5b295.root',
    ],
    401302: [
        '/store/data/Commissioning2026/HLTPhysics/RAW/v1/000/401/302/00000/24660da1-f364-4a09-bf4f-0927a057b833.root',
        '/store/data/Commissioning2026/HLTPhysics/RAW/v1/000/401/302/00000/3043e813-531c-49df-846a-27631f05f2fb.root',
        '/store/data/Commissioning2026/HLTPhysics/RAW/v1/000/401/302/00000/3bc949d8-9bf6-435d-9950-40ba621f787b.root',
        '/store/data/Commissioning2026/HLTPhysics/RAW/v1/000/401/302/00000/3c3caf34-26d1-49ad-a3e2-bf305e6df32f.root',
        '/store/data/Commissioning2026/HLTPhysics/RAW/v1/000/401/302/00000/416a7468-f13d-4551-9cfd-07cf2516eed2.root',
        '/store/data/Commissioning2026/HLTPhysics/RAW/v1/000/401/302/00000/50e97ff0-0619-427d-9c67-fc060c262b92.root',
    ],
    401201: [ # Commissioning 2026 Cosmics
        '/store/data/Commissioning2026/Cosmics/RAW/v1/000/401/201/00000/00748ee6-be29-45ea-a57a-51d730948afd.root',
        '/store/data/Commissioning2026/Cosmics/RAW/v1/000/401/201/00000/01346f92-2f49-484a-b76e-e127de9a7c79.root',
        '/store/data/Commissioning2026/Cosmics/RAW/v1/000/401/201/00000/02999cf5-e8a6-4531-b9bd-876cd2a1fa68.root',
    ],
    400839: [
        '/store/data/Commissioning2026/Cosmics/RAW/v1/000/400/839/00000/4c19758e-d498-4ce3-a498-08c4c673f0cc.root',
        '/store/data/Commissioning2026/Cosmics/RAW/v1/000/400/839/00000/89272025-a831-4fa7-b53b-c44cf502fe21.root',
    ],
    400813: [
        '/store/data/Commissioning2026/Cosmics/RAW/v1/000/400/813/00000/13890ac3-2223-4c75-9397-b662bae20ae0.root',
        '/store/data/Commissioning2026/Cosmics/RAW/v1/000/400/813/00000/21239d10-33f7-4a71-88ad-595a9b63103a.root',
    ],
    399970: [
        '/store/hidata/HIRun2025A/HIForward0/RAW/v1/000/399/970/00000/f59aa223-a9dd-4884-8678-303f1b0d4daa.root',
        '/store/hidata/HIRun2025A/HIForward0/RAW/v1/000/399/970/00000/61d8f943-1ece-450f-9d50-36fc830e27ff.root',
        '/store/hidata/HIRun2025A/HIForward0/RAW/v1/000/399/970/00000/6db899c6-b37f-4ddb-a31e-c9825e1c5f23.root',
        '/store/hidata/HIRun2025A/HIForward0/RAW/v1/000/399/970/00000/9a1ffe79-7154-4f8d-9224-edda6adb5ee2.root',
        '/store/hidata/HIRun2025A/HIForward0/RAW/v1/000/399/970/00000/acb9885d-aea2-4514-a5ce-fe68eb444ae3.root',
        '/store/hidata/HIRun2025A/HIForward0/RAW/v1/000/399/970/00000/baaeccfd-9c13-4591-8513-e9b3de1832da.root',
    ],
    399925: [
        '/store/hidata/HIRun2025A/HIEphemeralHLTPhysics/RAW/v1/000/399/925/00000/8312eab3-84cd-4853-a715-4dd176be5d7c.root',
        '/store/hidata/HIRun2025A/HIEphemeralHLTPhysics/RAW/v1/000/399/925/00000/850bbf35-cf6b-4d3f-951c-42c8b88c6cbb.root',
        '/store/hidata/HIRun2025A/HIEphemeralHLTPhysics/RAW/v1/000/399/925/00000/a2711cd1-5581-4f1e-a17e-058bf9dae205.root',
    ],
    399720: [ #HIPhysicsRawPrime HIRun2025A
       '/store/hidata/HIRun2025A/HIPhysicsRawPrime0/RAW/v1/000/399/720/00000/62c474b8-48f2-4ad9-ad27-fb509eca1ce3.root',
    ],
    398861: [
        '/store/data/Run2025G/VRRandom0/RAW/v1/000/398/861/00000/21214190-92e6-458f-9611-ce09e57d1522.root',
    ],
    398803: [ # 2025G LowPU 7 run
        '/store/data/Run2025G/HLTPhysics/RAW/v1/000/398/803/00000/07c0e6ef-5301-47f9-bfb9-a2517d609f2b.root',
        '/store/data/Run2025G/HLTPhysics/RAW/v1/000/398/803/00000/d4282346-4667-4761-9c19-284130d339aa.root',
#        '/store/data/Run2025G/SpecialZeroBias0/RAW/v1/000/398/803/00000/f1c2c8f6-94f5-4e26-857f-57246b15007c.root',
#        '/store/data/Run2025G/SpecialZeroBias0/RAW/v1/000/398/803/00000/72c5c646-bee6-4f11-a6e4-29ab675781c7.root',
#        '/store/data/Run2025G/SpecialZeroBias0/RAW/v1/000/398/803/00000/b9e2115a-94b1-4381-b00d-9a0b538eb19a.root',
#        '/store/data/Run2025G/SpecialZeroBias0/RAW/v1/000/398/803/00000/5e75b23a-d222-41b7-af93-985e2b37bea2.root',
    ],
    398802: [
        '/store/data/Run2025G/HLTPhysics/RAW/v1/000/398/802/00000/5a5fe9f4-d355-46dd-bb12-89adb062bcff.root',
        '/store/data/Run2025G/HLTPhysics/RAW/v1/000/398/802/00000/b25f854d-17e6-4673-ae64-68a2c3c8286e.root',
        '/store/data/Run2025G/HLTPhysics/RAW/v1/000/398/802/00000/aaaa2a2c-991a-43fa-983c-b11da3ce3c13.root',
    ],
    398600: [ #HLTPhysics, Run2025G, run 398600
        '/store/data/Run2025G/HLTPhysics/RAW/v1/000/398/600/00000/a42d22a8-b180-4e56-bd4e-a59acf392027.root',
        '/store/data/Run2025G/HLTPhysics/RAW/v1/000/398/600/00000/a47a594e-d447-44c8-b3b4-f63c655a3dce.root',
        '/store/data/Run2025G/HLTPhysics/RAW/v1/000/398/600/00000/a58aee7c-3b9f-4f34-81bc-ebad8cc03895.root',
        '/store/data/Run2025G/HLTPhysics/RAW/v1/000/398/600/00000/a64deaf4-ff4e-41d4-a089-2a3afeece56c.root',
        '/store/data/Run2025G/HLTPhysics/RAW/v1/000/398/600/00000/a918ff9a-36cb-4870-99a1-e74a3ac36ea5.root',
    ],
    398558: [
        '/store/data/Run2025G/HLTPhysics/RAW/v1/000/398/558/00000/031554aa-9094-4301-b259-88efa113f97b.root',
    ],
    398342: [ # Cosmics, Run2025G, run 398342, LS = [224, 228], 42701 events (RUCIO rule created)
       '/store/data/Run2025G/Cosmics/RAW/v1/000/398/342/00000/cce317da-17e9-4465-9ba5-4bc9eb207317.root',
    ],
    398335: [ # HLTPhysics, Run2025G, run 398335, LS = [], 17037 events
       '/store/data/Run2025G/HLTPhysics/RAW/v1/000/398/335/00000/033dbf5e-d09a-4b8a-944e-3d337428ffeb.root',
       '/store/data/Run2025G/HLTPhysics/RAW/v1/000/398/335/00000/055907eb-a34b-4cfe-aaf0-8a446bbebd36.root',
       '/store/data/Run2025G/HLTPhysics/RAW/v1/000/398/335/00000/0684d03d-61a9-4f35-98a8-576674b77b54.root',
       '/store/data/Run2025G/HLTPhysics/RAW/v1/000/398/335/00000/07b1b55f-64e5-4e2a-9493-b1b2cc46b8d8.root',
    ],
    398308: [ # HLTPhysics, Run2025G, run 398308, LS = [], 17236 events
       '/store/data/Run2025G/HLTPhysics/RAW/v1/000/398/308/00000/0055e4bd-e956-4030-a717-ecc7ff1fd49d.root',
       '/store/data/Run2025G/HLTPhysics/RAW/v1/000/398/308/00000/04e189c7-cee8-451b-be97-0cd586636cfd.root',
       '/store/data/Run2025G/HLTPhysics/RAW/v1/000/398/308/00000/08d12008-0a22-4e7c-aa6d-c6421f8f6057.root',
       '/store/data/Run2025G/HLTPhysics/RAW/v1/000/398/308/00000/0fd1f5f9-ebe8-4095-b2a9-f8f650702fb1.root',
    ],
    398226: [
        '/store/data/Run2025G/Cosmics/RAW/v1/000/398/226/00000/a348aa0d-f9ef-4693-9ecb-d071763863a3.root',
    ],
    398121: [
        '/store/data/Run2025G/EphemeralZeroBias0/RAW/v1/000/398/121/00000/753d0b50-92a0-43dd-8b4e-b8cfd414df35.root',
        '/store/data/Run2025G/EphemeralZeroBias0/RAW/v1/000/398/121/00000/b5ee237d-82b2-468d-a900-c10ee1cb59c6.root',
        '/store/data/Run2025G/EphemeralZeroBias0/RAW/v1/000/398/121/00000/0912d16d-2bd6-4387-b4cd-0a6343f9309d.root',
        '/store/data/Run2025G/EphemeralZeroBias0/RAW/v1/000/398/121/00000/b1bb6ed5-d4c7-4771-b13d-5001996648ae.root',
        '/store/data/Run2025G/EphemeralZeroBias0/RAW/v1/000/398/121/00000/8ca34d00-5ccf-4e6c-84ee-0d74a4d28a9f.root',
    ],
    398040: [ # HLTPhysics, Run2025G, run 398040, LS = [14, 23], 4241 events (RUCIO rule created)
        '/store/data/Run2025G/HLTPhysics/RAW/v1/000/398/040/00000/0994ecc9-5975-49bf-b078-f943d4248860.root',
    ],
    397817: [
        '/store/data/Run2025F/HLTPhysics/RAW/v1/000/397/817/00000/7d8e25fb-6161-4874-a441-caf0ba655e6e.root',
#        '/store/data/Run2025F/EGamma0/RAW/v1/000/397/817/00000/fa90bf6c-b987-4c69-87c8-b9cfe1641df7.root',
    ],
    397764: [ # JetMET
        '/store/data/Run2025F/JetMET0/RAW/v1/000/397/764/00000/c5cdce7c-ad3c-497b-879a-09e00150a6b3.root',
        '/store/data/Run2025F/JetMET0/RAW/v1/000/397/764/00000/d65bccf4-6ddb-455a-9041-408109f11afb.root',
        '/store/data/Run2025F/JetMET0/RAW/v1/000/397/764/00000/d9f8fb80-98cf-4a5b-9f31-42e635a05f48.root',
        '/store/data/Run2025F/JetMET0/RAW/v1/000/397/764/00000/e00fc104-8816-4cec-aeeb-c4eb4bf5af84.root',
    ],
    397729: [
        '/store/data/Run2025F/HLTPhysics/RAW/v1/000/397/729/00000/0669abbe-13da-4666-a914-eaa9799257dd.root',
    ],
    397698: [ # Cosmics 2025F
        '/store/data/Run2025F/Cosmics/RAW/v1/000/397/698/00000/0208d8a5-7bb2-4daf-9d22-6c2d566f7305.root',
        '/store/data/Run2025F/Cosmics/RAW/v1/000/397/698/00000/3fcb1176-396b-4c70-965c-4828a74739ca.root',
        '/store/data/Run2025F/Cosmics/RAW/v1/000/397/698/00000/4572a4f2-409e-44fd-b78e-057b336e55f6.root',
        '/store/data/Run2025F/Cosmics/RAW/v1/000/397/698/00000/5781c668-9437-4a2f-9468-96a7f16948fd.root',
        '/store/data/Run2025F/Cosmics/RAW/v1/000/397/698/00000/5a8654f8-fdce-41a7-8ff5-6ffbface7b81.root',
    ],
    397492: [
        '/store/data/Run2025F/HLTPhysics/RAW/v1/000/397/492/00000/02a80049-15c9-4c41-ae91-9ed221a4338a.root',
        '/store/data/Run2025F/HLTPhysics/RAW/v1/000/397/492/00000/aad4745b-b6f9-435a-bfdd-83b06cc2ccf6.root',
        '/store/data/Run2025F/HLTPhysics/RAW/v1/000/397/492/00000/30db2cea-e3b1-461a-aff2-bb60c3674b65.root',
        '/store/data/Run2025F/HLTPhysics/RAW/v1/000/397/492/00000/7ae6601b-9a63-451b-900a-6436f601fb25.root',
        '/store/data/Run2025F/HLTPhysics/RAW/v1/000/397/492/00000/a23e2d45-89b1-4592-897b-1378785a9961.root',
        '/store/data/Run2025F/HLTPhysics/RAW/v1/000/397/492/00000/379c4d56-f31a-4d54-a19e-f06d7b43b71f.root',
    ],
    397456: [
        '/store/data/Run2025F/HLTPhysics/RAW/v1/000/397/456/00000/0ff7606f-23bb-4cdc-9ea7-d9909ff003ee.root',
        '/store/data/Run2025F/HLTPhysics/RAW/v1/000/397/456/00000/12a7c233-b7fb-4136-bfa7-51c6d5547f44.root',
        '/store/data/Run2025F/HLTPhysics/RAW/v1/000/397/456/00000/19e0bf26-b46e-47ba-a6fc-03791bc515dc.root',
        '/store/data/Run2025F/HLTPhysics/RAW/v1/000/397/456/00000/1dc3f36d-b211-4a57-91a9-bbad1727ee45.root',
        '/store/data/Run2025F/HLTPhysics/RAW/v1/000/397/456/00000/219ba8c9-01bb-485d-b6d1-282ae0d79079.root',
    ],
    397414: [
        '/store/data/Run2025F/Cosmics/RAW/v1/000/397/414/00000/7f3bc5e9-0ebe-4b44-aea3-1ab1c3a77898.root',
    ],
    397050: [
        '/store/data/Run2025F/HLTPhysics/RAW/v1/000/397/050/00000/7263a9c3-e6b6-4e8d-b4bd-8d09222a01b1.root',
        '/store/data/Run2025F/HLTPhysics/RAW/v1/000/397/050/00000/3f6743a4-eade-4927-8414-e2334878187a.root',
        '/store/data/Run2025F/HLTPhysics/RAW/v1/000/397/050/00000/e3b5bc23-5d6b-4dc4-9431-2a1910f78967.root',
        '/store/data/Run2025F/HLTPhysics/RAW/v1/000/397/050/00000/1ea3fa97-0116-4f39-80cc-ea708ee599e2.root',
        '/store/data/Run2025F/HLTPhysics/RAW/v1/000/397/050/00000/9f55cf55-5eae-44fb-9aaa-7f088a2787ae.root',
    ],
    396805: [ # Collisions 2025, era Run2025F, 2460b fill, PD HLTPhysics, Run 396805, LS = 607-615, 948-956, 966-974, L1Menu_Collisions2025_v1_3_0
        '/store/data/Run2025F/HLTPhysics/RAW/v1/000/396/805/00000/53e9e1aa-30d0-4683-870e-7ceda767b46a.root',
        '/store/data/Run2025F/HLTPhysics/RAW/v1/000/396/805/00000/18e43e08-688a-40d0-970b-c889d4f16ed4.root',
        '/store/data/Run2025F/HLTPhysics/RAW/v1/000/396/805/00000/4e20363a-4ec9-40cc-ad29-2f117d59e15c.root',
    ],
    395817: [
        '/store/data/Run2025D/HLTPhysics/RAW/v1/000/395/817/00000/91edd6fc-3ac6-431e-8a56-84d4d0b2638d.root',
        '/store/data/Run2025D/HLTPhysics/RAW/v1/000/395/817/00000/87249617-1e7a-410b-b43f-a504ee155a31.root',
        '/store/data/Run2025D/HLTPhysics/RAW/v1/000/395/817/00000/55832d5f-c5fd-4804-8b35-2872b5fa8050.root',
        '/store/data/Run2025D/HLTPhysics/RAW/v1/000/395/817/00000/8c41c19c-9ef0-465a-b9ab-393f3ec28503.root',
    ],
    395751: [
        '/store/data/Run2025D/MinimumBias/RAW/v1/000/395/751/00000/8ec56bad-670d-48a6-9362-ad634e4cef56.root',
        '/store/data/Run2025D/MinimumBias/RAW/v1/000/395/751/00000/c1b0db0e-9561-4ad1-b7d8-9ef979645294.root',
        '/store/data/Run2025D/MinimumBias/RAW/v1/000/395/751/00000/f44d2a9f-d626-4668-bd79-adbea7109d31.root',
    ],
    395729: [ # HLTPhysics
        '/store/data/Run2025D/HLTPhysics/RAW/v1/000/395/729/00000/fdd51874-a138-442a-af70-ce509385524e.root',
        '/store/data/Run2025D/HLTPhysics/RAW/v1/000/395/729/00000/fb96066f-f881-4306-8021-7d12f50339e6.root',
        '/store/data/Run2025D/HLTPhysics/RAW/v1/000/395/729/00000/fa346702-97b0-466a-a5bd-12fe8dfe06a5.root',
    ],
    394886: [
        '/store/data/Run2025D/HLTPhysics/RAW/v1/000/394/886/00000/01fa6993-35de-4523-b1ee-4ab0cd4bada8.root',
    ],
    394748: [
        '/store/data/Run2025D/Cosmics/RAW/v1/000/394/748/00000/6df1b290-bac8-49aa-8b31-4671c0b5005d.root',
    ],
    394663: [
        '/store/data/Run2025D/HLTPhysics/RAW/v1/000/394/663/00000/4d80b9a6-d648-48c6-9a4c-9a63778c08e9.root',
    ],
    394635: [
        '/store/data/Run2025D/HLTPhysics/RAW/v1/000/394/635/00000/82f3e333-26c7-4714-9a8a-b294163372db.root',
        '/store/data/Run2025D/HLTPhysics/RAW/v1/000/394/635/00000/b59507eb-0118-4522-9fa1-de30c92ef13f.root',
        '/store/data/Run2025D/HLTPhysics/RAW/v1/000/394/635/00000/70b68534-6a1a-4255-a65c-8112712d1afd.root',
        '/store/data/Run2025D/HLTPhysics/RAW/v1/000/394/635/00000/22c287d2-1156-4abf-9729-28faa0962925.root',
    ],
    394615: [
        '/store/data/Run2025D/Cosmics/RAW/v1/000/394/615/00000/3ece40eb-14d4-4df4-b922-155062951f80.root',
    ],
    393952: [
        '/store/data/pORun2025/HLTPhysics/RAW/v1/000/393/952/00000/2b00ba7f-2cd3-4fd3-9b78-9d9e3b1df0f2.root',
    ],
    393918: [
        '/store/data/pORun2025/HLTPhysics/RAW/v1/000/393/918/00000/3cf0658a-5ad7-47b5-9d82-557c3de4077a.root',
    ],
    393861: [
        '/store/data/pORun2025/HLTPhysics/RAW/v1/000/393/861/00000/457597e5-e0c5-40ce-af94-5399b492270a.root',
    ],
    393767: [
        '/store/data/pORun2025/HLTPhysics/RAW/v1/000/393/767/00000/de30233a-7895-450c-a986-67995abcef82.root',
        '/store/data/pORun2025/HLTPhysics/RAW/v1/000/393/767/00000/cdca5c29-4314-4e53-9301-23c0ded06637.root',
    ],
    393765: [
        '/store/data/pORun2025/IonPhysics41/RAW/v1/000/393/765/00000/ed863683-cbdb-490f-98de-5ae30a63e34a.root',
    ],
    393747: [
        '/store/data/pORun2025/HLTPhysics/RAW/v1/000/393/747/00000/946b82b6-bd3c-44c8-bf89-a43352a3563f.root',
    ],
    393516: [ # ZeroBias with high PU 2025 June
        '/store/data/Run2025C/ZeroBias/RAW/v1/000/393/516/00000/01231e26-8050-4353-8591-a423f601d0ee.root',
    ],
    393376: [
        '/store/data/Run2025C/HLTPhysics/RAW/v1/000/393/376/00000/00773c15-cce5-4a51-86d5-c7158e7a3da4.root',
        '/store/data/Run2025C/HLTPhysics/RAW/v1/000/393/376/00000/030b4768-07fb-4ea2-b6a6-af4d79710190.root',
        '/store/data/Run2025C/HLTPhysics/RAW/v1/000/393/376/00000/03694a51-2890-4dc1-86ae-e2e0026c3a02.root',
    ],
    393276: [
        '/store/data/Run2025C/HLTPhysics/RAW/v1/000/393/276/00000/b56a0566-372e-4c14-95f2-f814fd6887e9.root',
        '/store/data/Run2025C/HLTPhysics/RAW/v1/000/393/276/00000/b76b586f-cb22-4609-8f3a-e431fb20bd04.root',
        '/store/data/Run2025C/HLTPhysics/RAW/v1/000/393/276/00000/bf74c217-5ce5-432d-b548-640fc27404f3.root',
    ],
    393145: [
        '/store/data/Run2025C/HLTPhysics/RAW/v1/000/393/145/00000/1634917a-28d1-46fb-90f0-6bde91dd1b3e.root',
        '/store/data/Run2025C/HLTPhysics/RAW/v1/000/393/145/00000/a6cf4fe5-f4af-4870-a204-1b91579d35f3.root',
    ],
    393111: [
        '/store/data/Run2025C/HLTPhysics/RAW/v1/000/393/111/00000/aa4fbcd1-a6ff-4343-bc5e-d6a8540f024a.root',
    ],
    392733: [
        '/store/data/Run2025C/HLTPhysics/RAW/v1/000/392/733/00000/01b628d2-cf6e-47f2-a253-4e71d562f7c4.root',
        '/store/data/Run2025C/HLTPhysics/RAW/v1/000/392/733/00000/02d11e2e-5035-4618-beb6-3ac06ebc428f.root',
        '/store/data/Run2025C/HLTPhysics/RAW/v1/000/392/733/00000/02f38ae4-d8b8-4089-b77d-7f8010696011.root',
    ],
    392642: [
        '/store/data/Run2025C/HLTPhysics/RAW/v1/000/392/642/00000/5e5dfc77-dda6-47f6-a261-e8b9600d2157.root'
    ],
    392477: [
        '/store/data/Run2025C/HLTPhysics/RAW/v1/000/392/477/00000/039247e3-345e-4637-9359-25ec7515ce21.root',
        '/store/data/Run2025C/HLTPhysics/RAW/v1/000/392/477/00000/0786c0bf-f716-4955-b2ee-6594a21e8ae4.root',
        '/store/data/Run2025C/HLTPhysics/RAW/v1/000/392/477/00000/179fff9b-44a3-4dfa-8a02-5134268c98e3.root',
    ],
    392382: [
        '/store/data/Run2025C/Muon0/RAW/v1/000/392/382/00000/aa76351f-f62d-4ade-a0b2-5394f6572487.root',
    ],
    392363: [
        '/store/data/Run2025C/HLTPhysics/RAW/v1/000/392/363/00000/04a16d1b-5c0e-4f83-a446-52acddd9b865.root',
        '/store/data/Run2025C/HLTPhysics/RAW/v1/000/392/363/00000/05315ef7-c8bd-49bd-bbe5-731852daca39.root',
        '/store/data/Run2025C/HLTPhysics/RAW/v1/000/392/363/00000/0ea7dc9a-87b4-4e84-9e60-b80b0c54e9b9.root',
    ],
    392071: [
       '/store/data/Run2025B/EphemeralZeroBias7/RAW/v1/000/392/071/00000/5a7dcdbd-bf13-4e02-a1ab-de023381da3b.root'
       '/store/data/Run2025B/EGamma0/RAW/v1/000/392/071/00000/465e97de-4e61-4303-96a1-236f442fff1e.root'
       '/store/data/Run2025B/Muon0/RAW/v1/000/392/071/00000/ab3697bc-82d4-4a34-93ff-bd9b019d942d.root'
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
    386951: [ # Muon 2024 for CSC FT validation CMSALCA-315
        '/store/data/Run2024I/Muon0/RAW/v1/000/386/951/00000/0009d0c6-9bab-40cf-9598-f2922c20ef72.root',
    ],
    386674: [ # Cosmics 2024, Run 386674, LS 1 (L1Menu_Collisions2024_v1_3_0)
        '/store/group/tsg/FOG/Cosmics2024/run386674/run386674_ls0006_streamPhysicsCommissioning_StorageManager.root',
    ],
}
