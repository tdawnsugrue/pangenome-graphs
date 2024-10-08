import os
import subprocess

ddd = "nonref_files/chr5-genos"
files = os.listdir(ddd)

count = 0
for f in files:
    wc = subprocess.run(["cat", ddd + "/" + f], stdout=subprocess.PIPE).stdout
    wc = subprocess.run(["wc", "-l"], capture_output=True, input=wc).stdout.decode()
    wc = int(wc)

    if wc > 0 : count += 1

print(f"{count} of {len(files)} non-empty.")
