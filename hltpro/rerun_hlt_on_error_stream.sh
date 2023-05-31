#!/bin/bash

# defaults
showHelpMsg=false
runNumKeyword=-1
numThreadsDefault=32
numThreads="${numThreadsDefault}"
errDirPathDefault=/store/error_stream
errDirPath="${errDirPathDefault}"
outDirPathDefault=tmp
outDirPath="${outDirPathDefault}"

# help message
usage() {
  cat <<@EOF
Usage:
  This script reruns the HLT menu of a given run on the corresponding error-stream files.

  > ./rerun_hlt_on_error_stream.sh -r 367666 -t 32 -i /store/error_stream -o tmp

Options:
  -h, --help         Show this help message

  -r, --runNumber    Run number (a wildcard is appended: for example,
                     if "-r 123" is used, all runs matching "123*" will be considered)

  -t, --threads      Number of threads and CMSSW streams   [Optional] [Default: ${numThreadsDefault}]

  -i, --input-dir    Path to error-stream directory        [Optional] [Default: ${errDirPathDefault}]
                     containing one sub-folder per run

  -o, --output-dir   Path to output directory              [Optional] [Default: ${outDirPathDefault}]

  If optional arguments are not specified, the corresponding default values will be used.
@EOF
}

# command-line interface
while [[ $# -gt 0 ]]; do
  case "$1" in
    -h|--help) showHelpMsg=true; shift;;
    -r|--runNumber) runNumKeyword=$2; shift; shift;;
    -t|--threads) numThreads=$2; shift; shift;;
    -i|--input-dir) errDirPath=$2; shift; shift;;
    -o|--output-dir) outDirPath=$2; shift; shift;;
    *) shift;;
  esac
done

# print help message
if [ "${showHelpMsg}" == true ]; then
  usage
  exit 0
fi

runNumRegex='^[0-9]+$'
if ! [[ "${runNumKeyword}" =~ ${runNumRegex} ]] ; then
  printf "\n\033[31m\033[1m%s\033[0m%s\n\n" ">> ERROR" " -- invalid run number (must be a positive integer without sign) [-r]: ${runNumKeyword}"
  exit 1
fi

if [ "${runNumKeyword}" -le 0 ]; then
  printf "\n\033[31m\033[1m%s\033[0m%s\n\n" ">> ERROR" " -- invalid run number (must be a number higher than zero) [-r]: ${runNumKeyword}"
  exit 1
fi

if [ ! -d "${errDirPath}" ]; then
  printf "\n\033[31m\033[1m%s\033[0m%s\n\n" ">> ERROR" " -- target input directory does not exist [-i]: ${errDirPath}"
  exit 1
fi

if [ -d "${outDirPath}" ]; then
  printf "\n\033[31m\033[1m%s\033[0m%s\n\n" ">> ERROR" " -- target output directory already exists [-o]: ${outDirPath}"
  exit 1
fi

if [ -z "${CMSSW_BASE}" ]; then
  printf "\n\033[31m\033[1m%s\033[0m%s" ">> ERROR" " -- environment variable CMSSW_BASE not found"
  printf "%s\n" ": it is necessary to first set up the CMSSW environment"
  printf "%s\n\n" "            (for example via \"source setup.sh -r CMSSW_X_Y_Z\")"
  exit 1
fi

errDirAbsPath=$(readlink -e "${errDirPath}")
runDirPrePath="${errDirAbsPath}"/run"${runNumKeyword}"

if [ $(ls -d "${runDirPrePath}"* 2> /dev/null | wc -l) -eq 0 ]; then
  printf "\n\033[31m\033[1m%s\033[0m%s\n\n" ">> ERROR" " -- no input directories found: ${runDirPrePath}*"
  exit 1
fi

mkdir -p "${outDirPath}"
cd "${outDirPath}"

for dirPath in $(ls -d "${runDirPrePath}"*); do
  # require at least one non-empty FRD file
  [ $(cd "${dirPath}" ; find -maxdepth 1 -size +0 | grep .raw | wc -l) -gt 0 ] || continue
  runNumber="${dirPath: -6}"
  JOBTAG=test_run"${runNumber}"
  HLTMENU="--runNumber ${runNumber}"
  hltConfigFromDB --runNumber "${runNumber}" > "${JOBTAG}".py
  cat <<EOF >> "${JOBTAG}".py
process.options.numberOfThreads = ${numThreads}
process.options.numberOfStreams = 0
process.hltOnlineBeamSpotESProducer.timeThreshold = int(1e6)
del process.PrescaleService
del process.MessageLogger
process.load('FWCore.MessageService.MessageLogger_cfi')
import os
import glob
process.source.fileListMode = True
process.source.fileNames = sorted([foo for foo in glob.glob("${dirPath}/*raw") if os.path.getsize(foo) > 0])
process.EvFDaqDirector.buBaseDir = "${errDirAbsPath}"
process.EvFDaqDirector.runNumber = ${runNumber}
process.hltDQMFileSaverPB.runNumber = ${runNumber}
# remove paths containing OutputModules
streamPaths = [pathName for pathName in process.finalpaths_()]
for foo in streamPaths:
    process.__delattr__(foo)
EOF
  rm -rf run"${runNumber}"
  mkdir run"${runNumber}"
  echo "run${runNumber} .."
  cmsRun "${JOBTAG}".py &> "${JOBTAG}".log
  echo "run${runNumber} .. done (exit code: $?)"
  unset runNumber
done
unset dirPath
