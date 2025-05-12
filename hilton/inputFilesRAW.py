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
}
