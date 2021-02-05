#!/bin/bash

x=0
while [ $x -le 4320 ]; do
    let x=x+1
    /bin/ps -o rss --pid $1 >> memlog.txt
    sleep 10
done
