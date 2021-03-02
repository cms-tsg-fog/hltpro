#!/bin/bash

# Usage: ./cleanGenerateAndRun.sh <run #> <# of cores (optional)> <skipRepack (optional)>
# If no argument for the number of cores is provided, will run with `grep -c processor /proc/cpuinfo`/2 
# See ./nCoresOnly.sh for details.
# Repack check is now run by default after hltd jobs finish. If "skipRepack" is given as 2nd or 3rd arg,
# the repack check will be skipped.

if [[ $# -ge 2 && $2 =~ [0-9]+$ ]]; then
    nCores=$2
fi

run=$1
if [[ $# -ge 1 && $run =~ [0-9]+$ ]]; then
    ./cleanRun.sh $run
    cmsRun genTestFakeBuFromRAW_cfg.py runNumber=$run
    ./startHiltonRun.sh $run $nCores
else
    echo "Need at least one positive integer argument: the run number"
    exit
fi

# This loop looks for running cmsRun jobs and waits until there are no longer any
sleep 10 #<-- this is needed here or else the rest will be skipped
while [ $(ps -u daqlocal | grep "cmsRun" | grep -v "grep" | wc -l) -gt 0 ]; do
    echo "jobs still running ..."
    sleep 10
done

SCRIPTDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
while [ $(ps -u daqlocal | grep "anelastic" | grep -v "grep" | wc -l) -gt 0 ]; do
    ret=`${SCRIPTDIR}/is_quarantined.py`
    if [[ $ret -eq 1 ]]; then
        break
    fi
    echo "merging still running ..."
    sleep 10
done

while [ $(ps -u daqlocal | grep "valgrind" | grep -v "grep" | wc -l) -gt 0 ]; do
    echo "valgrind jobs still running ..."
    sleep 10
done
echo "jobs finished."

# Skip repack check if specified:
if [[ $# -ge 2 && ($2 == "skipRepack" || $3 == "skipRepack") ]]; then
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
