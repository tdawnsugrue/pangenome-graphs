import os
from sys import stderr

chrom_dir = "graphs/chroms/"

chroms = [i for i in range(1,23)] # + ["X", "Y"]

# doing this the lazy way
for chrom in chroms:
    print("Getting chromosome", chrom, file=stderr)
    os.system(f"./bin/odgi depth --threads=48 -i {chrom_dir}chr{chrom}.full.og -d > nonref_files/chr{chrom}-full-node-depth.txt")

print("Done.", file=stderr)