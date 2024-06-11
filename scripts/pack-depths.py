import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

coverages = pd.read_csv("data/packed-fcgr-depth-thing.tsv", delimiter="\t", header=None)
coverages = coverages.rename(columns={0 : 'path-maybe', 1 : 'position', 2 : 'coverage'})

#grch = "GRCh38#chr1:161505240-161678751"

coverages = coverages[coverages['path-maybe']==grch]
print(coverages.tail())
subsetted = coverages[coverages['position'] > 161623196 -161505240 - 20000]
print("start pos", 161623196 -161505240)

sns.lineplot(x="position", y="coverage", data=subsetted)
plt.show()