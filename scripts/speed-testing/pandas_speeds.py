import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("data/speed_stats.tsv", sep="\t",
                   names=["Graph", "cutLength", "trueLength", "Nodes", "Time"])

print(data)

plt.figure()
lengthplot = sns.scatterplot(data, x="trueLength", y="Time")

plt.figure()
nodeplot = sns.scatterplot(data, x="Nodes", y="Time")

plt.show()