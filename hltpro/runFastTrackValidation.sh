#!/bin/bash

# Need to run setup.sh first, and of course make sure fffParameters.jsn is configured correctly.
# Also, need to make sure genTestFakeBuFromRAW_cfg.py is configured the way you want for 
# this test. For the fast track validation, usually you want to run over an HLTPhysics 
# sample and a sample related to the conditions change you are validating. For example, for 
# a change in ECal conditions, you might run over an EGamma sample.

if [ -z "${CMSSW_BASE}" ]; then
  printf "\n%s\n\n" "[runFastTrackValidation] environment variable CMSSW_BASE is not set --> you need to first set up CMSSW (for example with \"source setup.sh -r CMSSW_X_Y_Z\")"
  exit 1
fi

printf "%s\n\n" "Running automated fast-track validation script. Will compare rates and timing of menus using reference and test global tags."
sleep 5

######### user params #########

# Cosmics
testMenu=/cdaq/cosmic/commissioning2020/MWGR3/HLT/V1
runNumber=338717
testGT=111X_dataRun3_HLT_v2

# # VirginRaw
# testMenu=/cdaq/special/2020/MWGR1/VirginRaw/VR_Random_TS2/HLT/V14
# runNumber=334518
# testGT=111X_dataRun3_HLT_v1

#testMenu=/cdaq/test/gennai/2020/MWGR_September/HLT_GPU/V8
#runNumber=334393
#testGT=111X_dataRun3_HLT_Candidate_2020_08_21_13_26_45

###############################

outputbasedir=/cmsnfsscratch/globalscratch/hltpro/fastTrack
mkdir -p $outputbasedir

## reference trial:
./newHiltonMenu.py $testMenu
./cleanGenerateAndRun.sh $runNumber skipRepack

if [ -d "${outputbasedir}/reference_run${runNumber}" ]; then

  printf "%s\n" "[runFastTrackValidation] removing directory ${outputbasedir}/reference_run${runNumber} .."
  rm -r "${outputbasedir}/reference_run${runNumber}"
fi

printf "%s\n" "[runFastTrackValidation] copying /fff/BU0/output/run$runNumber to $outputbasedir/reference_run$runNumber .."
cp -r /fff/BU0/output/run$runNumber $outputbasedir/reference_run$runNumber

## test trial:
./newHiltonMenu.py --GT $testGT $testMenu
./cleanGenerateAndRun.sh $runNumber # don't skip repack for test GT

if [ -d "${outputbasedir}/test_run${runNumber}" ]; then

  printf "%s\n" "[runFastTrackValidation] removing directory ${outputbasedir}/test_run${runNumber} .."
  rm -r "${outputbasedir}/test_run${runNumber}"
fi

printf "%s\n" "[runFastTrackValidation] copying /fff/BU0/output/run$runNumber to $outputbasedir/test_run$runNumber .."
cp -r /fff/BU0/output/run$runNumber $outputbasedir/test_run$runNumber

echo " "
echo "hltd jobs for both test and reference configuration completed. Check the following for correct output:"
echo "$outputbasedir/reference_run$runNumber"
echo "$outputbasedir/test_run$runNumber"
echo " "
echo "dumping rates..."
sleep 3
echo " "

./monitorRatesMultiLumi.py $outputbasedir/reference_run$runNumber/streamHLTRates/data/run$runNumber*jsndata > ref_HLT_rates.txt
./monitorRatesMultiLumi.py $outputbasedir/test_run$runNumber/streamHLTRates/data/run$runNumber*jsndata > test_HLT_rates.txt

echo "HLT Rates of menu $testMenu using test GT $testGT dumped to test_HLT_rates.txt"
echo "Reference rates dumped to ref_HLT_rates.txt"
echo " "
echo "getting timing results..."
sleep 3

if [ -d $outputbasedir/reference_run$runNumber/streamDQMHistograms/data ]; then
  if [ $(ls $outputbasedir/reference_run$runNumber/streamDQMHistograms/data/*.pb 2> /dev/null | wc -l) -gt 0 ]; then
    fastHadd add -o $outputbasedir/reference_run$runNumber/ref_DQM_hists.pb $outputbasedir/reference_run$runNumber/streamDQMHistograms/data/*.pb
    fastHadd convert -o ref_DQM_hists.root $outputbasedir/reference_run$runNumber/ref_DQM_hists.pb
    printf "\n%s\n" "[reference] DQM histograms (including timing) dumped to: ref_DQM_hists.root (copy to lxplus and open in TBrowser to examine timing plots)"
  else
    printf "\n%s\n" "[reference] DQM histograms not produced (no matches for $outputbasedir/reference_run$runNumber/streamDQMHistograms/data/*.pb)"
  fi
else
  printf "\n%s\n" "[reference] DQM histograms not produced (directory $outputbasedir/reference_run$runNumber/streamDQMHistograms/data/ does not exist)"
fi

if [ -d $outputbasedir/test_run$runNumber/streamDQMHistograms/data ]; then
  if [ $(ls $outputbasedir/test_run$runNumber/streamDQMHistograms/data/*.pb 2> /dev/null | wc -l) -gt 0 ]; then
    fastHadd add -o $outputbasedir/test_run$runNumber/test_DQM_hists.pb $outputbasedir/test_run$runNumber/streamDQMHistograms/data/*.pb
    fastHadd convert -o test_DQM_hists.root $outputbasedir/test_run$runNumber/test_DQM_hists.pb
    printf "\n%s\n" "[test, GT=${testGT}] DQM histograms (including timing) dumped to: test_DQM_hists.root (copy to lxplus and open in TBrowser to examine timing plots)"
  else
    printf "\n%s\n" "[test, GT=${testGT}] DQM histograms not produced (no matches for $outputbasedir/test_run$runNumber/streamDQMHistograms/data/*.pb)"
  fi
else
  printf "\n%s\n" "[test, GT=${testGT}] DQM histograms not produced (directory $outputbasedir/test_run$runNumber/streamDQMHistograms/data/ does not exist)"
fi

printf "\n%s\n" "End of script."
