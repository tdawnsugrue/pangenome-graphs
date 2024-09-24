import sys

# Filters a depth file based on the total number of haplotypes

if len(sys.argv) < 3 or len(sys.argv) > 5:
    print("ERROR: invalid arguments.\nUsage: python filter_depths_info.py [DEPTH_FILE] [NODE_FILE]", file=sys.stderr)

nodes = [line.split() for line in open(sys.argv[2]).read().split('\n')][:-1]
depths = [line.split() for line in open(sys.argv[1]).read().split('\n')][:-1] # nodes are 1-indexed so leave the header in

depth_idx = [int(d[0]) for d in depths[1:]]

min_haps = sys.argv[3] if len(sys.argv) > 3 else 10
max_haps = sys.argv[4] if len(sys.argv) > 4 else 50

missing_nodes = 0 
# print depths for nodes in filtered nodes file
for node in nodes:
    n = int(node[0])
    if n > int(depths[-1][0]):
        print("Node greater than last node in 'full' depth list.", file=sys.stderr)
        break
    
    try:
        d = depths[depth_idx.index(n)+1]
    except:
        missing_nodes += 1
        continue
    depth = int(d[1])
    if depth >= min_haps and depth <= max_haps :
        print(node, d, file=sys.stderr)
        print(f"{d[0]}\t{d[1]}\t{d[2]}")

print(missing_nodes, "missing nodes", file=sys.stderr)