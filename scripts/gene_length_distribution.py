# reads in the gff3 annot file and collates gene lengths into a graph.
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

count = 0
all = 0

gene_lengths = []
genes = []

with open("data/gencode.v38.basic.annotation.gff3") as annots:
    for line in annots:
        all += 1
        line = line.split("\t")
        if len(line) < 3 : continue
        if line[2] == "gene":
            chrom = line[0]
            start = line[3]
            end = line[4]

            # some are on reverse
            length = int(max(end,start)) - int(min(start, end))
            gene_lengths.append(length)

            x = line[8]
            id = x[x.find("=") + 1:x.find(";")]

            genes.append((chrom, id, start, end, length))

        if all % 1000 == 0:
            print(all)


print(f"Median: {np.median(gene_lengths)}\tMean: {np.mean(gene_lengths)}\t"+
      f"25: {np.percentile(gene_lengths, 25)}\t75: {np.percentile(gene_lengths, 75)}"+
      f"\n95: {np.percentile(gene_lengths, 95)}\tMax: {max(gene_lengths)}\n",
      f"Min: {min(gene_lengths)}")

# this has a really long tail; set max as no more than 1e6
# fig = sns.histplot(x = gene_lengths).get_figure()

# fig.savefig("img/gene_length_distributions_hist.png", dpi=300)

fig = sns.histplot(x = [i for i in gene_lengths if i < 152024]).get_figure()

fig.savefig("img/gene_length_distributions_hist_trunc.png", dpi=300)


# get col
# get length with end - start
# get id: col 8 from = (+ 1) to ;
# add line to list as: CHROM ID START END LENGTH

genes = pd.DataFrame(genes, columns=["chromosome", "geneID", "start", "end", "length"])
genes.to_csv("data/all-gene-coords.tsv", sep="\t")

#print(genes.head())

# do odgi stats on region and chr5
# gene sizes:
"""
Med: 3609
Mean: 32409
25%: 557
75%: 25297
95%: 152024
Max: 2473538
"""