#!/bin/bash

#Usage: This script takes two inputs: The HLT menu python file and the L1 menu XML file.
#       It then checks that every instance of "L1SeedsLogicalExpression" in the HLT menu
#       matches to an algorithm name in the L1 XML. If the HLTL1TSeed module L1Seed
#       parameter name changes or the L1 XML format changes, the script will need to be
#       updated.

if [ "$#" -ne 2 ]; then
    printf "%s\n" "[L1MenuCheck.sh] Need exactly two arguments: (1) the HLT menu python file and (2) the L1 menu XML"
    exit 1
fi

menu=$1
xml=$2

xmllines=`grep "<algorithm>" -A 1 $xml| grep -v "<algorithm>" | sed 's/^.*<name>\(.*\)<\/name>*$/\1/g' | sed '/--/d'`
menulines=`grep "L1SeedsLogicalExpression" $menu | sed 's/^.*"\(.*\)".*$/\1/g'`

count=0

for line in $menulines ; do
    if [[ $line == L1* ]]; then
        chk=0
        for seed in $xmllines ; do
            if [ $line == $seed ]; then
                chk=1
                break
            fi
        done
        if [ $chk -eq 0 ]; then
            printf "%s\n" "[L1MenuCheck.sh] --> !! L1 seed does not exist in the L1-menu .xml file: ${line}"
            ((count++))
        fi
    fi
done

printf "%s\n" "[L1MenuCheck.sh] Found ${count} instances in ${menu} of an L1 seed which is not present in ${xml}"
