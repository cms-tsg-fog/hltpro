#!/bin/bash

# Need to run setup.sh first, and of course make sure fffParameters.jsn is configured correctly.
# Also, need to make sure genTestFakeBuFromRAW_cfg.py is configured the way you want for
# this test. For the fast-track validation, usually you want to run over an HLTPhysics
# sample and a sample related to the conditions change you are validating. For example, for
# a change in ECAL conditions, you may want to run over an EGamma sample.

if [ -z "${CMSSW_BASE}" ]; then
  printf "\n%s" "[runFastTrackValidation] environment variable CMSSW_BASE is not set"
  printf "%s\n\n" " --> you need to first set up CMSSW (for example via \"source setup.sh -r CMSSW_X_Y_Z\")"
  exit 1
fi

######### user params #########

testMenu=/cdaq/physics/Run2023/2e34/v1.1.0/HLT/V4
runNumber=367262
testGT=130X_dataRun3_HLT_Candidate_2023_05_15_13_34_33
maxEvents=100

# no HLT prescales + re-emulation of Level-1 Global Trigger
testMenuOpts="--l1-emu uGT --l1 L1Menu_Collisions2023_v1_1_0-v2_xml --prescale 2p0E34+HLTPhysics"

###############################

printf "%s\n  %s\n\n" "Running Fast-Track Validation:" "--> will compare rates and timing of HLT menu using reference and test GlobalTags."
printf "%s\n\n%s\n%s\n%s\n%s\n\n" "CMSSW_BASE  = ${CMSSW_BASE}" "HLT Menu  = ${testMenu}" "Run       = ${runNumber}" "Test GT   = ${testGT}" "maxEvents = ${maxEvents}"
sleep 2

outputbasedir=/cmsnfsscratch/globalscratch/hltpro/fastTrack
mkdir -p $outputbasedir

## reference trial (GT in HLT menu)
#./newHiltonMenu.py $testMenu
./newHiltonMenu.py $testMenu ${testMenuOpts}
./cleanGenerateAndRun.sh --run $runNumber --maxEvents ${maxEvents} --skipRepack

if [ -d "${outputbasedir}/reference_run${runNumber}" ]; then
  printf "%s\n" "[runFastTrackValidation] removing directory ${outputbasedir}/reference_run${runNumber} .."
  rm -rf "${outputbasedir}"/reference_run"${runNumber}"
fi

printf "%s\n" "[runFastTrackValidation] copying /fff/BU0/output/run$runNumber to $outputbasedir/reference_run$runNumber .."
cp -r /fff/BU0/output/run$runNumber $outputbasedir/reference_run$runNumber

## test trial (test GT for fast-track validation)
./newHiltonMenu.py $testMenu ${testMenuOpts} --GT $testGT
./cleanGenerateAndRun.sh --run $runNumber --maxEvents ${maxEvents} # don't skip repack for test GT

if [ -d "${outputbasedir}/test_run${runNumber}" ]; then
  printf "%s\n" "[runFastTrackValidation] removing directory ${outputbasedir}/test_run${runNumber} .."
  rm -rf "${outputbasedir}"/test_run"${runNumber}"
fi

printf "%s\n" "[runFastTrackValidation] copying /fff/BU0/output/run$runNumber to $outputbasedir/test_run$runNumber .."
cp -r /fff/BU0/output/run$runNumber $outputbasedir/test_run$runNumber

## analysis of reference and test results
echo " "
echo "HLTD jobs for both test and reference configuration completed. Check the following output directories:"
echo " ${outputbasedir}/reference_run${runNumber}"
echo " ${outputbasedir}/test_run${runNumber}"
echo " "
echo "dumping rates..."
sleep 2
echo " "

./monitorRatesMultiLumi.py $outputbasedir/reference_run$runNumber/streamHLTRates/data/run$runNumber*jsndata > ref_HLT_rates.txt
./monitorRatesMultiLumi.py $outputbasedir/test_run$runNumber/streamHLTRates/data/run$runNumber*jsndata > test_HLT_rates.txt

echo "HLT Rates of menu ${testMenu} using test GT ${testGT} dumped to test_HLT_rates.txt"
echo "Reference rates dumped to ref_HLT_rates.txt"
echo " "
echo "getting timing results..."
sleep 2

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
