#!/bin/bash

if [[ $# -ge 2 && $2 =~ [0-9]+$ ]]; then
    nCores=$2
fi

run=$1
if [[ $# -ge 1 && $run =~ [0-9]+$ ]]; then
    ./addMissingEoLS.sh $run
    sudo chmod -R 777 /fff
    sudo sh -c 'echo 1048576 > /proc/sys/fs/inotify/max_queued_events'
    sudo systemctl restart hltd
    sudo systemctl restart bufu_filebroker
    sleep 5
    ./nCoresOnly.sh $nCores
    sleep 5
    curl "http://localhost:9000/cgi-bin/start_cgi.py?run=${run}"
else
    echo "Need at least one positive integer argument: the run number"
fi
