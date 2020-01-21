#! /bin/bash

# boostrap a new CMSSW area
function bootstrap_cmssw() {
  test -n "$1" || return 1

  # set the environment
  export http_proxy="http://cmsproxy.cms:3128/"
  export https_proxy="https://cmsproxy.cms:3128/"
  export NO_PROXY=".cms"
  export VO_CMS_SW_DIR="$(readlink -f $1)"
  export LANG="C"

  test -n "$SCRAM_ARCH" || SCRAM_ARCH=slc7_amd64_gcc820
  export SCRAM_ARCH

  # if necessary, bootstrap the area
  if ! [ -f "$VO_CMS_SW_DIR"/"$SCRAM_ARCH"/external/rpm/*/etc/profile.d/init.sh ]; then
    mkdir -p "$VO_CMS_SW_DIR"
    echo "Downloading bootstrap script"
    wget -O $VO_CMS_SW_DIR/bootstrap.sh http://cmsrep.cern.ch/cmssw/bootstrap.sh
    echo "Bootstrapping software area at $VO_CMS_SW_DIR"
    sh -ex $VO_CMS_SW_DIR/bootstrap.sh setup -path $VO_CMS_SW_DIR -arch $SCRAM_ARCH >& $VO_CMS_SW_DIR/bootstrap_$SCRAM_ARCH.log
    if (( $? )); then
      echo
      echo "Bootstrap failed"
      return 1
    fi
  fi

  # optionally, remove a CMSSW release
  test -n "$2" || return 0

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

bootstrap_cmssw "$@"
