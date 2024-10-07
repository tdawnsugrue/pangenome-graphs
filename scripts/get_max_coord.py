# foreach chrom:

# odgi stats -p -s -t8
# grab third line (check b4 run on all), second to last coord (length)
# print to a tsv with chrom \t max_coord

import os
import subprocess

cdir = "graphs/chroms"
chrom_graphs = os.listdir(cdir)

# 1

for i in range(len(chrom_graphs))[:1]:
    stats = subprocess.run(["odgi", "stats", "-i", cdir + "/" + chrom_graphs[i], "-S", "-t8"], capture_output=True).stdout.decode().split("\n")
    print(stats)
    pass