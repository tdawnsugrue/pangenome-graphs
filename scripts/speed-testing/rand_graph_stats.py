# should've made this folder earlier. Oops!

# for file in graphs/random
# run odgi stats on it
# slurp length/n-nodes
# line: graphID length nodes
# write em all to a tsv
import subprocess
import os

graph_dir = "graphs/random/"

graphs = os.listdir(graph_dir)

for graph in graphs[:1]:
    # odgi paths to get first path name
    # run time on the bash script < args FILE_PATH GRAPH_PATH
    # get sys time
    # store graphID TIME
    path = subprocess.run(["odgi", "paths", "-i", graph_dir + graph, "-L"], capture_output=True).stdout.decode()
    path = path.split("\n")
    print(path)
    pass