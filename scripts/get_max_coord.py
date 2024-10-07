# foreach chrom:

# odgi stats -p -s -t8
# grab third line (check b4 run on all), second to last coord (length)
# print to a tsv with chrom \t max_coord

import os
import subprocess

chrom_graphs = os.listdir("graphs/chroms")

# 1

for i in range(len(chrom_graphs))[:1]:
    stats = subprocess.run(["odgi", "stats", "-i", chrom_graphs[i], "-S", "-t8"], capture_output=True).stdout.decode().split("\n")[1]
    print(stats)
    pass