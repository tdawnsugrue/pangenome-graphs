# I mucked up :))))
# rename nodes and put them where they belong
import os

b = "nonref_files/"
dirs = [b + f"chr{c}-1k-10-50/" for c in range(1, 23)]
skiplist = [b + "chr5-1k-10-50/"]
#files = [f for f in os.listdir("nonref_files") if f.endswith(".txt")]


for d in dirs[:]:
    if d in skiplist : continue
    prefix = d[:-1]
    print("fixing",d)
    try:
        os.system(f"mv {prefix}*.txt {d}")
    except:
        pass
    files = [f for f in os.listdir(f"{d}")]
    for fl in files:
        os.system(f"mv {d}{fl} {d}{fl[fl.find("10-50")+5:]}")
