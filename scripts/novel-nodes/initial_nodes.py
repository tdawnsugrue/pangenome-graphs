import sys
import subprocess
import os
from time import time

# This file pulls from all chromosomes and gets length info for all nodes > 1kbp
# This is the first step in the "pipe"
# next step is to run odgi depth on each chromosome
# then filter based on min/max haplotypes

odgi = "./bin/odgi"
# odgi = "odgi"
chroms_dir = "graphs/chroms/" # directory for full chrom og files
exclude_list = ["5"] # chroms to skip
chromosomes = [str(i) for i in range(1, 23)] + ["X", "Y"]
min_node_length = 1000


# autogen a paths file based on chromosome number
for chrom in chromosomes[:]:
    if chrom in exclude_list : continue

    # FILTERING
    paths = open("paths.txt", "w")
    paths.write(f"GRCh38#chr{chrom}\nCHM13#chr{chrom}")
    paths.close()

    # then get node lengths (running odgi view and then filter based on length (1kbp))
    print("oview")
    start = time
    x = subprocess.run([odgi, "view", "-i", f"{chroms_dir}chr{chrom}.full.og", "-g"],
                             capture_output=True).stdout
    print("grep/awk")
    x = subprocess.run(["grep", "^S"], input=x, capture_output=True).stdout
    lengths = subprocess.run(["awk", "-v", "OFS=\t", r"{print($2,length($3))}"],
                              input=x, capture_output=True).stdout.decode().split("\n")
    

    # get depths for everything relative to ref
    x = subprocess.run([odgi, "depth", "-i", f"{chroms_dir}chr{chrom}.full.og", "-s", "paths.txt", "-d"], 
                       capture_output=True).stdout.decode().split("\n")
    
    # [node, len, node, depth, depth]
    all_nodes = [(a + "\t" + b).split("\t") for a, b in zip(lengths, x[1:])]
    filt_nodes = []
    depth_zero = 0
    over_100 = 0

    # filter only novel nodes, with specified min length
    for node in all_nodes[:-1]:
        if node[0] != node[2]:
            print("node mismatch!!")
            exit()
        

        if int(node[3]) == 0 and int(node[1]) >= min_node_length:
            filt_nodes.append(node[:2] + node[3:])

    filt_nodes = ["\t".join(node) for node in filt_nodes]

    printable = "\n".join(filt_nodes)

    f = open(f"nonref_files/chr{chrom}-novel-nodes-1k.txt", "w")
    f.write(printable)
    f.close()
    


os.system("rm paths.txt")