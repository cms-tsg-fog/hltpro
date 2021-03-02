#!/bin/env python3
import json
import os,sys

with open(os.path.join('/fff/ramdisk/appliance/boxes', os.uname()[1]), 'r') as fp:
    js = json.load(fp)
    if js['quarantined'] > 0 and js['used'] == 0:
        print(1)
        sys.exit(1)

print(0)
sys.exit(0)
