# should've made this folder earlier. Oops!

# for file in graphs/random
# run odgi stats on it
# slurp length/n-nodes
# line: graphID length nodes
# write em all to a tsv
import subprocess
import os
from sys import stderr

graph_dir = "graphs/random/"

graphs = os.listdir(graph_dir)

all_stats = []

for graph in graphs:
    # odgi paths to get first path name
    # run time on the bash script < args FILE_PATH GRAPH_PATH
    # get sys time
    # store graphID TIME
    length = graph[graph.find("-")+1:graph.rfind("-")]
    length = length[length.find("-")+1:]
    
    path = subprocess.run(["odgi", "paths", "-i", graph_dir + graph, "-L"], capture_output=True).stdout.decode()
    path = path.split("\n")[0]
    
    time = subprocess.run(["time", "-p", "./scripts/time_rand_pipe.sh", graph_dir + graph, path], 
                          capture_output=True).stderr.decode().split("\n")[1:-1]

    a = 0
    for t in time:
        a += float(t[t.find(" ")+1:])
    time = f"{a:.3f}"

    stats = subprocess.run(["odgi", "stats", "-i", graph_dir + graph, "-S"], capture_output=True).stdout.decode().split("\n")
    stats = stats[1].split("\t")[:2]

    all_stats.append("\t".join([graph, length, *stats, time]))
    print(f"testing {graph}", file=stderr)

with open("data/speed_stats.tsv", "w") as file:
    file.write("\n".join(all_stats) + "\n")

print("done", file=stderr)
