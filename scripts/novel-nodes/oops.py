# I mucked up :))))
# rename nodes and put them where they belong
import os

b = "nonref_files/"
dirs = [b + f"chr{c}-1k-10-50/" for c in range(1, 23)]
skiplist = [b + "chr5-1k-10-50/"]
#files = [f for f in os.listdir("nonref_files") if f.endswith(".txt")]


for d in dirs:
    if d in skiplist : continue
    prefix = d[:-1]
    #os.system(f"mv {b}{prefix}*.txt {b}{d}")
    files = [f for f in os.listdir(f"{b}{d}")]
    for fl in files[:2]:
        print(f"mv {fl} {fl[fl.find("10-50")+5:]}")