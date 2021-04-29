#! /bin/bash

# remove a CMSSW area
function remove_cmssw() {
  if [ $# -ne 2 ]; then
    echo "two command-line arguments required: (1) path to installation directory, (2) name of CMSSW release"
    return 1
  fi

  if [ ! -d $1 ]; then
    echo "target directory not found: $1"
    return 1
  fi

  # set the environment
  export http_proxy="http://cmsproxy.cms:3128/"
  export https_proxy="http://cmsproxy.cms:3128/"
  export NO_PROXY=".cms"
  export VO_CMS_SW_DIR="$(readlink -e $1)"
  export LANG="C"

  test -n "$SCRAM_ARCH" || SCRAM_ARCH=slc7_amd64_gcc900
  export SCRAM_ARCH

  if [ ! -d ${VO_CMS_SW_DIR}/${SCRAM_ARCH} ]; then
    echo "target directory not found: ${VO_CMS_SW_DIR}/${SCRAM_ARCH}"
    return 1
  fi

  echo "Updating package database"
  $VO_CMS_SW_DIR/common/cmspkg -a $SCRAM_ARCH update

  if echo $2 | grep -q patch; then
    echo "Removing patch release $2"
    $VO_CMS_SW_DIR/common/cmspkg -a $SCRAM_ARCH remove -y cms+cmssw-patch+$2
  elif echo $2 | grep -q ib; then
    echo "Removing IB release $2"
    $VO_CMS_SW_DIR/common/cmspkg -a $SCRAM_ARCH remove -y cms+cmssw-ib+$2
  else
    echo "Removing release $2"
    $VO_CMS_SW_DIR/common/cmspkg -a $SCRAM_ARCH remove -y cms+cmssw+$2
  fi

  echo "Cleaning package database"
  $VO_CMS_SW_DIR/common/cmspkg -a $SCRAM_ARCH clean
}

if [ "$1" = "-a" ]; then
  export SCRAM_ARCH="$2"
  shift 2
fi

remove_cmssw "/opt/hilton/cmssw" "$@"
