#!/bin/bash

usage() {
  cat <<@EOF
Usage:
  ./cleanGenerateAndRun.sh --run RUN_NUMBER --nCores NUM_CORES --skipRepack --maxEvents NUM_EVENTS

If no argument for the number of cores is provided, `grep -c processor /proc/cpuinfo`/2 will be used (see ./nCoresOnly.sh for details)

Repack check is now run by default after hltd jobs finish.
  - If "--skipRepack" is specified, the repack check will be skipped.

Options:
  --run           Run number
  --nCores        Number of cores           [Optional]
  --maxEvents     Maximum number of events  [Optional]
  --skipRepack    Skip data re-packing step [Optional]
  -h, --help      Show this help message
@EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    -h|--help) showHelpMsg=true ;;
    --run) run="${2}"; shift ;;
    --nCores) if [[ $2 =~ ^[0-9]+$ ]]; then nCores="${2}"; shift; fi ;;
    --maxEvents) if [[ $2 =~ ^[0-9]+$ ]]; then maxEventsStr="maxEvents=${2}"; shift; fi ;;
    --skipRepack) skipRepack=true ;;
    *) echo "[cleanGenerateAndRun.sh] !!! INVALID ARGUMENT --> ${1}" ;;
  esac
  shift
done

if [ "${showHelpMsg}" = true ]; then
    usage
    exit 0
fi

if [ -z $run ]; then
    echo -e "\n[cleanGenerateAndRun.sh] ERROR --> Need to specify a run number with \"--run RUN_NUMBER\"\n"
    usage
    exit 1
elif ! [[ $run =~ ^[0-9]+$ ]]; then
    echo -e "\n[cleanGenerateAndRun.sh] ERROR --> Specified Run number is invalid (must be a positive integer): ${run}\n"
    usage
    exit 1
fi

./cleanRun.sh $run
cmsRun genTestFakeBuFromRAW_cfg.py runNumber=$run ${maxEventsStr}
./startHiltonRun.sh $run $nCores

# This loop looks for running cmsRun jobs and waits until there are no longer any
sleep 10 #<-- this is needed here or else the rest will be skipped
while [ $(ps -u daqlocal | grep "cmsRun" | grep -v "grep" | wc -l) -gt 0 ]; do
    echo "Jobs still running ..."
    sleep 10
done

SCRIPTDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
while [ $(ps -u daqlocal | grep "anelastic" | grep -v "grep" | wc -l) -gt 0 ]; do
    ret=`${SCRIPTDIR}/is_quarantined.py`
    if [[ $ret -eq 1 ]]; then
        break
    fi
    echo "Merging still running ..."
    sleep 10
done

while [ $(ps -u daqlocal | grep "valgrind" | grep -v "grep" | wc -l) -gt 0 ]; do
    echo "Valgrind jobs still running ..."
    sleep 10
done
echo "Jobs finished."

# Skip repack check if specified
if [ "${skipRepack}" = true ] ; then
    exit
fi

# Now actually run check
echo "Running repack check..."
streamFindCommand='find /fff/BU0/output/run'$run'/ -maxdepth 1 -mindepth 1 -type d'
streamList=($($streamFindCommand))

outputbasedir=/cmsnfsscratch/globalscratch/hltpro

if [ -d "${outputbasedir}/testRepack/input" ]; then
  rm -r "${outputbasedir}/testRepack/input"
fi

if [ -d "${outputbasedir}/testRepack/output" ]; then
  rm -r "${outputbasedir}/testRepack/output"
fi

mkdir -p $outputbasedir/testRepack/input
mkdir -p $outputbasedir/testRepack/output

for streamdir in "${streamList[@]}"; do

    stream=$(basename $streamdir)

    if [[ ${stream} == streamDQMHistograms ]] ||
       [[ ${stream} == streamHLTRates ]] ||
       [[ ${stream} == streamL1Rates ]]; then

      continue
    fi

    inpfiles=$(find ${streamdir}/data -maxdepth 1 -mindepth 1 -type f | sort)

    if ! [ "${inpfiles}" ]; then continue; fi;

    newfile=$outputbasedir/testRepack/input/$stream.dat

    cat ${inpfiles} > ${newfile}

    cmsRun RunRepackCfg.py ${newfile} #> testRepack/output/$stream.log
done
