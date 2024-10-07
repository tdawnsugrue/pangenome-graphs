
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
odgi extract -i [graph] -o [tmp] -E -r GRCh#chr[chrom]:[arbirtrary]-[arb2]
odgi sort
odgi viz
"""

# and then record info (length/nodes) and time (system time) for graphing purposes

# so the whole pipeline would be something like "time <(odgi extract && odgi sort && odgi viz)"
import random
import subprocess

# each line has id, length, nodes
random_graphs_data = []

lengths = [32500, 150000, 2000000]

with open("data/chroms_max_coords.tsv") as file:
    max_coords = [i[1] for i in file.read().split("\n") if len(i) > 1]

for length in lengths:
    for i in range(5):
        chrom = random.randint(1, 22)

        start = random.randint(1, max_coords[chrom-1] - length - 1)
        end = start + length

        print(f"Extracting graph {i} of length {length}...")

        gname = f"graphs/random/rand-chr{chrom}-{length}-{start}.og"

        # we do -E to prevent "problems"
        subprocess.run(["odgi", "extract", "-i", f"graphs/chroms/chr{chrom}.full.og", "-t8", "-E",
                        "-r", f"GRCh38#chr{chrom}:{start}-{end}", "-o", gname])
        
        # run odgi stats
        stats = subprocess.run(["odgi", "stats", "-i", gname, "-S", "-t8"], capture_output=True).stdout.decode().split("\n")[1].split("\t")

        random_graphs_data.append([gname, stats[0], stats[1]])