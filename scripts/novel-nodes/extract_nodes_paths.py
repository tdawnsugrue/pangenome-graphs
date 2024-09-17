import sys
import subprocess
# usage - python extract_etc.py [filt.txt]

odgi = "./bin/odgi"
chrom = "chr5.full.og"
threads = "4"
folder = "nonref_files/chr5-1k-10-50/"
# odgi = "odgi"

if len(sys.argv) != 2:
    print("Error - Usage: python extract_nodes_paths.py [NODES]")

# odgi extract -i [full chr] -n [node number] -o [out.og]
# odgi paths -i [out.og] -L --> capture stdout and cutoff the end of the ids
# then make a table like:
"""
 (do this later); just do a simple csv-like for each node; then do a join later

"""

nodes = [i.split()[0] for i in open(sys.argv[1]).readlines()]

for node in nodes:
    print(f"Doing node {node}")
    subprocess.run([odgi, "extract", "-i", chrom, "-n", node, 
                    "-t", threads, "-o", "tmp.og"])
    paths = subprocess.run([odgi, "paths", "-i", "tmp.og", "-L"], capture_output=True).stdout
    paths = [p[:p.find("#")] for p in paths]

    f = open(f"{folder}{node}.txt", "w")
    for p in paths : f.write(p + "\n")
    f.close()