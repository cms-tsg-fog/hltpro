from cosmics import process as process_cosmics
from lowPU import process as process_lowPU

#print process_cosmics

for prod in process_cosmics._Process__producers:
    if hasattr(process_lowPU,prod):
        print prod

