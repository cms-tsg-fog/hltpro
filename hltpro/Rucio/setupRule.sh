account=t2_ch_cern_local_users
lifetime=$((86400 * 150)) # Lifetime in seconds. Multiplication factor is days. 
comment="HLT Tests"
block="cms:/store/data/Run2022A/MinimumBias0/RAW/v1/000/352/568/00000/d4dcc6b1-0c5d-4b89-a117-d82fbceec7d1.root" # file name
#block="cms:/MinimumBias0/Run2022A-v1/RAW#fc8a2c55-b525-4052-b234-dcf48b9ec0f7" # block name
copies=1
rse_expression="T2_CH_CERN"
