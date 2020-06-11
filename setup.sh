#!/bin/bash

# defaults
showHelpMsg=false
defScramArch=slc7_amd64_gcc820
defCmssetDefault=/opt/offline/cmsset_default.sh

usage(){
  cat <<@EOF
Usage: this script sets up the SCRAM_ARCH and sources cmsset_default.sh.
       If the name of a CMSSW release is specified (option: -r),
       cmsenv is done in this release.

Options:
  -h, --help      Show this help message
  -a, --arch      Value of SCRAM_ARCH                [Default: ${defScramArch}]
  -c, --cmsset    Path to cmsset_default.sh script   [Default: ${defCmssetDefault}]
  -r, --release   Name of CMSSW release              [Optional]
@EOF
}

# command-line interface
scramArch=${defScramArch}
cmssetDefault=${defCmssetDefault}

while [[ $# -gt 0 ]]; do
  case "$1" in
    -h|--help) showHelpMsg=true; shift ;;
    -a|--arch) scramArch=$2; shift; shift ;;
    -c|--cmsset) cmssetDefault=$2; shift; shift ;;
    -r|--release) cmsswRelease=$2; shift; shift ;;
    *) shift;;
  esac
done

# print help message
if [ ${showHelpMsg} == true ]; then
  usage
  return 0
fi

# set up environment
printf "\033[1m%s\033[0m%s\n" "SCRAM Architecture" "       : ${scramArch}"
printf "\033[1m%s\033[0m%s\n" "cmsset_default.sh script" " : ${cmssetDefault}"

if [ ! -f "${cmssetDefault}" ]; then
  printf "\n\033[31m\033[1m%s\033[0m%s\n\n" ">> ERROR" ": invalid path to cmsset_default.sh script [-c]: ${cmssetDefault}"
  usage
  return 1
fi

export http_proxy="http://cmsproxy.cms:3128/"
export https_proxy="http://cmsproxy.cms:3128/"
export NO_PROXY=".cms,localhost"

export SCRAM_ARCH=${scramArch}
source ${cmssetDefault}

export TZ='-01:00'

# do cmsenv in the release installation directory
if [ ! -z "${cmsswRelease}" ]; then
    printf "\033[1m%s\033[0m%s\n" "CMSSW Release" "            : ${cmsswRelease}"
    BASE=`scram list -c CMSSW | grep "\<$cmsswRelease\>" | awk '{ print $3; }'`
    if ! [ "${BASE}" ]; then
        echo "CMSSW release ${cmsswRelease} is not installed for the architecture ${SCRAM_ARCH}."
        scram list CMSSW
    elif ! [ -d "${BASE}" ]; then
        echo "The directory ${BASE} does not exist; the release installation is probably broken."
    else
        echo "Setting up the CMSSW environment from ${BASE}"
        cd ${BASE}
        eval `scram runtime -sh`
        cd ${OLDPWD}
    fi
    unset cmsswRelease BASE
fi
unset showHelpMsg defScramArch defCmssetDefault scramArch cmssetDefault
