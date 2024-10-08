
# doing this on chr5 only
from nearby_ref_nodes import get_nearby_nodes
import subprocess
import os
# NOTE: create genotype
# cat header of giraffemcshitty

# foreach node:
# get upper..? flank
# odgi extract that node
# grab start coord from paths
# do grep/awk shit to get genotypes

ndir = "nonref_files/chr5-1k-10-50/"
nodes = os.listdir(ndir)
already_extracted = os.listdir("nonref_files/chr5-wider/")
#already_extracted = []

prev = []
skipping = 0

for node in nodes[:]:
    node = int(node[:node.find(".")])

    print("flanking", node)

    flanks = get_nearby_nodes(node)

    # some nodes have identical "flanks" so multiple nodes are covered by a single coord...
    # worth looking into in a fantasy land where I have the time to do so
    if flanks in prev:
        skipping += 1
        continue
    
    prev.append(flanks)

    newgraph = f"nonref_files/chr5-wider/{node}.og"
    if newgraph not in already_extracted:
        print("extracting...")
        subprocess.run(["odgi", "extract", "-i", "graphs/chroms/chr5.full.og", "-t16", "-n", str(flanks[0]),
                    "-o", newgraph])
    
    print("grabbing paths")
    ref_path = subprocess.run(["odgi", "paths", "-L", "-t16", "-i", newgraph], capture_output=True).stdout.decode().split("\n")[0]
    coord = ref_path[ref_path.find(":")+1:ref_path.find("-")]

    # throw this into a shell script:
    # cat giraffewhatever | grep ^chr | grep -m 1 [COORD] | sed 's/:[^\t]*//g'
    # ok you have to use the LOWER coord
    print("doing the annoying shell bit\n")
    test = subprocess.run(["./scripts/novel-nodes/genotype_coord.sh", coord], capture_output=True)


print("done I hope!")
print("Skipped", skipping)

