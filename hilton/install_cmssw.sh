#!/bin/bash

# boostrap a new CMSSW area
function bootstrap_and_install_cmssw() {
  test -n "$1" || return 1

  if [ ! -z "${CMSSW_BASE}" ]; then
    echo "Bootstrap failed: a CMSSW area is already set up, will not bootstrap a new software area --> start from a clean session"
    return 1
  fi

  # set the environment
  export http_proxy="http://cmsproxy.cms:3128/"
  export https_proxy="http://cmsproxy.cms:3128/"
  export NO_PROXY=".cms"
  export VO_CMS_SW_DIR="$(readlink -m $1)"
  export LANG="C"

  test -n "$SCRAM_ARCH" || SCRAM_ARCH=el8_amd64_gcc10
  export SCRAM_ARCH

  # if necessary, bootstrap the area
  if ! [ -d "$VO_CMS_SW_DIR"/"$SCRAM_ARCH" ] || ! [ -f "$VO_CMS_SW_DIR"/"$SCRAM_ARCH"/external/rpm/*/etc/profile.d/init.sh ]; then
    mkdir -p "$VO_CMS_SW_DIR"
    rc=$?; if [[ $rc != 0 ]]; then return $rc; fi
    echo "Downloading bootstrap script"
    curl -s -S -o $VO_CMS_SW_DIR/bootstrap.sh https://cmsrep.cern.ch/cmssw/bootstrap.sh
    echo "Bootstrapping software area at $VO_CMS_SW_DIR (SCRAM_ARCH=${SCRAM_ARCH})"
    bash -ex $VO_CMS_SW_DIR/bootstrap.sh setup -path $VO_CMS_SW_DIR -arch $SCRAM_ARCH >& $VO_CMS_SW_DIR/bootstrap_$SCRAM_ARCH.log
    if (( $? )); then
      printf "\n%s\n" "Bootstrap failed (dir=${VO_CMS_SW_DIR}, SCRAM_ARCH=${SCRAM_ARCH})"
      return 1
    fi
    # configure the newly bootstrapped area: link to the official area, and disable the production release checks
    (
      source $VO_CMS_SW_DIR/cmsset_default.sh
      scram db --link /opt/offline
      scram config release-checks=0
    )
  fi

  # optionally, install a CMSSW release
  test -n "$2" || return 0

  echo "Updating package database"
  $VO_CMS_SW_DIR/common/cmspkg -a $SCRAM_ARCH update

  if echo $2 | grep -q patch; then
    echo "Installing patch release $2"
    $VO_CMS_SW_DIR/common/cmspkg -a $SCRAM_ARCH install -y cms+cmssw-patch+$2
  else
    echo "Installing release $2"
    $VO_CMS_SW_DIR/common/cmspkg -a $SCRAM_ARCH install -y cms+cmssw+$2
  fi

  echo "Cleaning package database"
  $VO_CMS_SW_DIR/common/cmspkg -a $SCRAM_ARCH clean
}

if [ "$1" = "-a" ]; then
  export SCRAM_ARCH="$2"
  shift 2
fi

bootstrap_and_install_cmssw "/opt/hilton/cmssw" "$@"
