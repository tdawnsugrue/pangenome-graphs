# seaborn, pandas
import sys, os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

try:
    filt = sys.argv[1]
    files = [f for f in os.listdir(f"data/depths/") if filt in f]
    for f in files:
        data = pd.read_csv("data/depths/"+f, sep='\t', header=None,
                           names=["Path","Position","Depth"])
        paths = data["Path"].unique()
        # this should only be 1 long.. gives the whole path that was grabbed
        path = [s for s in paths if s.startswith("GRCh38")][0]
        data = data[data["Path"] == path]
        sns.lineplot(data = data, x = "Position", y = "Depth")
        #plt.axvspan(, color='red', alpha=0.5)
        plt.show()
except:
    print("Error! Usage: python graph_depth_files.py <filter>")