#!/bin/bash

#Usage: This script takes two inputs: The HLT menu python file and a payload hash for the corresponding L1 XML.
#       It then checks that every instance of "L1SeedsLogicalExpression" in the HLT menu
#       matches to an algorithm name in the L1 XML.
#       If the HLTL1TSeed module L1Seed parameter name changes or the L1 XML format changes,
#       the script will need to be updated.

if [ "$#" -ne 2 ]; then
    printf "%s\n" "[L1MenuCheck_FromPayload.sh] Need exactly two arguments: (1) the HLT menu python and (2) a payload hash for the L1 XML"
    exit 1
fi

if [[ -z "$CMSSW_VERSION" ]]; then
    printf "%s\n" "[L1MenuCheck_FromPayload.sh] You need to do cmsenv first"
    exit 1
fi

menu=$1
xmlhash=$2

#All this is to get around the fact that conddb dump tries to modify the release base
#I have tried to make this robust, but I am not very confident. I have no doubt that this will break sometime in the future...
srcpath=`echo $CMSSW_SEARCH_PATH | sed '0,/:.*$/s/:.*$//'`
scram project CMSSW $CMSSW_VERSION 2> /dev/null
cd $CMSSW_VERSION/src
eval `scram runtime -sh`
mkdir -p ../bin/$SCRAM_ARCH
cp $srcpath/../bin/$SCRAM_ARCH/conddb ../bin/$SCRAM_ARCH/
../bin/$SCRAM_ARCH/conddb --db "oracle+frontier://@frontier%3A%2F%2F%28proxyurl%3Dhttp%3A%2F%2Flocalhost%3A3128%29%28serverurl%3Dhttp%3A%2F%2Flocalhost%3A8000%2FFrontierOnProd%29%28serverurl%3Dhttp%3A%2F%2Flocalhost%3A8000%2FFrontierOnProd%29%28retrieve%2Dziplevel%3D0%29/CMS_CONDITIONS" dump $xmlhash >& ../../tmp.xml 2> /dev/null
cd ../..
rm -r $CMSSW_VERSION
#You can run this script offline, just change the line above this one and up to "^srcpath" to the following line:
#conddb dump $xmlhash >& tmp.xml

xmllines=`grep "<first>" tmp.xml | sed 's/^.*<first>\(.*\)<\/first>*$/\1/g' | sed '/--/d'`
rm -f tmp.xml

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
            printf "%s\n" "[L1MenuCheck_FromPayload.sh] --> !! L1 seed does not exist in the L1-menu payload: ${line}"
            ((count++))
        fi
    fi
done

printf "%s\n" "[L1MenuCheck_FromPayload.sh] Found ${count} instances in ${menu} of an L1 seed which is not present in L1 XML from payload hash ${xmlhash}"
