import sys
import subprocess
import os
# usage - python extract_etc.py [filt.txt]

odgi = "./bin/odgi"
#chrom = "chr5.full.og"
threads = "8"
folder = "graphs/chroms/"
chromosomes = [i for i in range(1, 23)]
# odgi = "odgi"

# if len(sys.argv) != 2:
#     print("Error - Usage: python extract_nodes_paths.py [NODES]")

# odgi extract -i [full chr] -n [node number] -o [out.og]
# odgi paths -i [out.og] -L --> capture stdout and cutoff the end of the ids
# then make a table like:
"""
 (do this later); just do a simple csv-like for each node; then do a join later

"""

d = os.listdir("nonref_files")

for chrom in chromosomes:
    nodes = [i.split()[0] for i in open(f"nonref_files/chr{chrom}-filt-1k-10-50.txt").readlines()]
    ch_dir = f"nonref_files/chr{chrom}-1k-10-50"
    
    try:
        os.mkdir(ch_dir)
    except:
        continue
    
    for node in nodes:
        print(f"Doing node {node}")
        subprocess.run([odgi, "extract", "-i", f"{folder}chr{chrom}.full.og", "-n", node, 
                        "-t", threads, "-o", "tmp.og"])
        paths = subprocess.run([odgi, "paths", "-i", "tmp.og", "-L"], capture_output=True).stdout.decode().split("\n")
        paths = [p[:p.find("#")] for p in paths]

        f = open(f"{ch_dir}{node}.txt", "w")
        for p in paths : f.write(p + "\n")
        f.close()
