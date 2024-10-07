
# set of 3 lengths
# load in max coords (need to get these)
# generate 5 graphs for each length with start coord between 1- (max coord - length)
# odgi stats for each of these graphs with -S

# (run time [PIPELINE])

# note: get what each flag does...? for methods..?
# coords are zero (or possibly 1) based. "Early tests indicated extraction time dependent on initial graph size"
# so just do something silly like 10-10000 since it doesnt really matter

# Pipeline is as follows:
"""
odgi extract -i [graph] -o [tmp] -P -E -r GRCh#chr[chrom]:[arbirtrary]-[arb2]
odgi sort
odgi viz
"""

# and then record info (length/nodes) and time (system time) for graphing purposes

# so the whole pipeline would be something like "time <(odgi extract && odgi sort && odgi viz)"
import random

lengths = [32500, 150000, 2000000]

max_coords = 

for length in lengths:
    for i in range(5):
        chrom = random.randint(1, 22)