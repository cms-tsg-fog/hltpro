source /cvmfs/cms.cern.ch/cmsset_default.sh &&
source /cvmfs/cms.cern.ch/rucio/setup-py3.sh &&
export RUCIO_ACCOUNT="t2_ch_cern_local_users" &&
voms-proxy-init -voms cms -rfc -valid 192:00
