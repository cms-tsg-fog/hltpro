#!/bin/bash

if [ $# -eq 1 ]; then

  run=$1
  rm -rf /fff/BU0/ramdisk/run${run} /fff/BU0/data/sm/run${run} /fff/data/run${run} /fff/BU0/output/run${run}

else

  printf "\n%s\n\n" "[cleanRun.sh] ERROR: one command-line argument required -> specify run number (example: ./cleanRun.sh [RUN])"
  exit
fi
