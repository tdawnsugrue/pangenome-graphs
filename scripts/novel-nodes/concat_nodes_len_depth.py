import sys

if len(sys.argv) != 3:
    print("Error: Invalid arguments.\nUsage: python concat_nodes_len_depth.py [NODE_LENGTHS] [NODE DEPTHS]", file=sys.stderr)
    exit()

# NOTE: this filters off the nodes in the depth file

lengths = [line.split() for line in open(sys.argv[1]).readlines()]
depths = [line.split() for line in open(sys.argv[2]).readlines()]

# so we can find proper indices for nodes in lengths
l_nodes = [int(l[0]) for l in lengths]

for node in depths:
    n = int(node[0])
    l = lengths[l_nodes.index(int(node[0]))] # get correct node
    for i in node : print(i, end='\t') 
    for i in l : print(i, end='\t')
    print()