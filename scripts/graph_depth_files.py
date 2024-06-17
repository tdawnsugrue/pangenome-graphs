# seaborn, pandas
import sys, os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

try:
    labs = []
    filt = sys.argv[1]
    files = [f for f in os.listdir(f"data/depths/") if filt in f]
    for i, f in enumerate(files[:2]):
        data = pd.read_csv("data/depths/"+f, sep='\t', header=None,
                           names=["Path","Position","Depth"])
        paths = data["Path"].unique()
        # this should only be 1 long.. gives the whole path that was grabbed
        path = [s for s in paths if s.startswith("GRCh38")][0]
        print(path)
        data = data[data["Path"] == path]
        ax = sns.lineplot(data = data, x = "Position", y = "Depth")
        ax.set_title("Read depth for mapped samples")
        labs.append(f[:f.find("-")])
        # specific to irgm region
    plt.axvspan(150846521-150796142, 150900736-150796142, color='black', alpha=0.5)
    plt.legend(labels=[labs[0],'IRGM region?',labs[1]], loc="upper right")
    plt.show()
except:
    print("Error! Usage: python graph_depth_files.py <filter>")