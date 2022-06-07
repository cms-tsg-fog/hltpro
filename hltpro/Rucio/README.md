# Rucio Rules

Instructions on how to create Rucio rules for storing data for Hilton tests.

General reading: [Rucio Twiki](https://twiki.cern.ch/twiki/bin/viewauth/CMS/Rucio)

Note: Currently only the FOG conveners and Trigger Coordinators have permissions to create Rucio rules on `T2_CH_CERN`.

## Rucio Scripts

A few simple scripts were created to help create Rucio rules

- `setupRucio.sh` to set up the environment
- `findBlock.sh` to find the block name for a given file
- `setupRule.sh` to set up the Rucio rule
- `createRule.sh` to actually create the rule

Note: Some useful commands are listed in `usefulRucioCommands.txt`

## Creating a Rucio Rule

- Search for the file in DAS:
  - Dataset name `dasgoclient --query="dataset dataset=/MinimumBias0/Run2022*/RAW"`
  - Files of dataset: `dasgoclient --query="file dataset=/MinimumBias0/Run2022A-v1/RAW run=352568"`
- If you want to store the whole block, find the block name by updating and running `findBlock.sh`
- Update the `setupRule.sh` with the file name or block name and lifetime multiplication factor in days
- After setting everything up, to create the rule, simply run `createRule.sh` 
