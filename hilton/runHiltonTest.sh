#!/bin/bash

# Need to run setup.sh first, and of course make sure fffParameters.jsn is configured correctly.
# Also, need to make sure genTestFakeBuFromRAW_cfg.py is configured the way you want for this test.

if [ -z "${CMSSW_BASE}" ]; then
  printf "\n%s" "[runHiltonTest] environment variable CMSSW_BASE is not set"
  printf "%s\n\n" " --> you need to first set up CMSSW (for example via \"source setup.sh -r CMSSW_X_Y_Z\")"
  exit 1
fi

######### user params #########

testMenu=/cdaq/test/missirol/test/2024/online/GRun/v1.0/HLT/V1
runNumber=370293
testGT=140X_dataRun3_HLT_v1
maxEvents=200

# no HLT prescales + re-emulation of Level-1 Global Trigger
testMenuOpts="-r ${runNumber} --no-prescale"
testMenuOpts+=" --l1-emu uGT --l1 L1Menu_Collisions2024_v1_0_0_xml"
testMenuOpts+=" --empty-output-files"
#testMenuOpts+=" --customise HLTrigger/Configuration/customizeHLTforCMSSW.customiseForOffline"
#testMenuOpts+=" --customise HLTrigger/Configuration/customizeHLTforAlpaka.customizeHLTforAlpaka"
testMenuOpts_customCmds="del process.MessageLogger\nprocess.load('FWCore.MessageLogger.MessageLogger_cfi')"

###############################

printf "%s\n  %s\n\n" "Running Hilton Test:" "--> will compare rates and timing of HLT menu using reference and test GlobalTags."
printf "%s\n\n%s\n%s\n%s\n%s\n\n" "CMSSW_BASE = ${CMSSW_BASE}" "HLT Menu   = ${testMenu}" "Run number = ${runNumber}" "Test GT    = ${testGT}" "maxEvents  = ${maxEvents}"
sleep 2

outputbasedir=/cmsnfsscratch/globalscratch/hltpro/hiltonTest
mkdir -p "${outputbasedir}"

## test trial (test GT for fast-track validation)
./newHiltonMenu.py "${testMenu}" -g "${testGT}" ${testMenuOpts} --customise_commands "${testMenuOpts_customCmds}" -c v3
[ $? -eq 0 ] || exit 1

./cleanGenerateAndRun.sh --run "${runNumber}" --maxEvents "${maxEvents}" # do not skip repack

if [ -d "${outputbasedir}/test_run${runNumber}" ]; then
  printf "%s\n" "[runHiltonTest] removing directory ${outputbasedir}/test_run${runNumber} .."
  rm -rf "${outputbasedir}"/test_run"${runNumber}"
fi

printf "%s\n" "[runHiltonTest] copying /fff/BU0/output/run$runNumber to ${outputbasedir}/test_run${runNumber} .."
cp -r /fff/BU0/output/run"${runNumber}" "${outputbasedir}"/test_run"${runNumber}"

## analysis of results
echo " "
echo "HLTD jobs for test configuration completed. Check the following output directory."
echo " ${outputbasedir}/test_run${runNumber}"
echo " "
sleep 1

./monitorRatesMultiLumi.py "${outputbasedir}"/test_run"${runNumber}"/streamHLTRates/data/run"${runNumber}"*jsndata > hiltonTest_HLT_rates.txt

echo "HLT Rates of menu ${testMenu} using test GT ${testGT} dumped to hiltonTest_HLT_rates.txt"
echo " "
sleep 1

if [ -d "${outputbasedir}"/test_run"${runNumber}"/streamDQMHistograms/data ]; then
  if [ $(ls "${outputbasedir}"/test_run"${runNumber}"/streamDQMHistograms/data/*.pb 2> /dev/null | wc -l) -gt 0 ]; then
    fastHadd add -o "${outputbasedir}"/test_run"${runNumber}"/test_DQM_hists.pb "${outputbasedir}"/test_run"${runNumber}"/streamDQMHistograms/data/*.pb
    fastHadd convert -o hiltonTest_DQM_hists.root "${outputbasedir}"/test_run"${runNumber}"/test_DQM_hists.pb
    printf "\n%s\n" "[runHiltonTest] DQM histograms (including timing) dumped to: hiltonTest_DQM_hists.root (copy to lxplus and open in TBrowser to examine timing plots)"
  else
    printf "\n%s\n" "[runHiltonTest] DQM histograms not produced (no matches for ${outputbasedir}/test_run${runNumber}/streamDQMHistograms/data/*.pb)"
  fi
else
  printf "\n%s\n" "[runHiltonTest] DQM histograms not produced (directory ${outputbasedir}/test_run$runNumber/streamDQMHistograms/data/ does not exist)"
fi

printf "\n%s\n" "End of script."
