import os
import subprocess
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

chroms = [i for i in range(1, 23)]

# Population info for samples
sample_data = pd.read_csv("nonref_files/20130606_g1k_3202_samples_ped_population.txt", delimiter=" ")
sample_data["SampleID"] = sample_data["SampleID"].astype(str)

# Code > actual pop data
populations = pd.read_csv("data/20131219.populations.tsv", delimiter="\t").dropna()


chroms_node_data = {}


# TODO: encapsulate forea chrom

node_dir = "nonref_files/chr5-1k-10-50/"
nodes = os.listdir(node_dir)

node_data = {}
pop_counts = {}

for node in nodes[:]:
    if not node.endswith(".txt") : continue # skip irrelevant files

    nid = node[:node.find(".")]
    paths = open(node_dir + node).read().split('\n')[:-2]

    counts = []

    for path in sorted(list(set(paths))):
        counts.append((path, paths.count(path)))

    df = pd.DataFrame(counts, columns=["SampleID", "count"])
    df["SampleID"] = df["SampleID"].astype(str)
    df = df.merge(sample_data[["SampleID", "Population", "Superpopulation"]],
                  on="SampleID")
    
    node_data[nid] = df
    pop_counts[nid] = df["Superpopulation"].value_counts()

# convert data into list of superpops and their counts
pop_df = pd.DataFrame.from_dict(pop_counts)
pop_df = pd.pivot_table(pop_df, columns="Superpopulation").reset_index().fillna(0)
pop_df = pop_df.melt(id_vars="index")
pop_df = pop_df.pivot(index="index", columns="Superpopulation")

#sns.heatmap(data=pop_df)
sns.heatmap(pop_df, annot=True)
plt.show()