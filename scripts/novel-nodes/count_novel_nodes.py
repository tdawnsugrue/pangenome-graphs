import subprocess
import os

# grab all relevant files
# run cat | wc -l --> decode --> int
# sum them all up

chroms = [i for i in range(1, 23)]

count = 0

for c in chroms:
    file = open(f"nonref_files/chr{c}-filt-1k-10-50.txt").readlines()

    count += len(file)

    print(file[-1])

print("Total nodes:", count)
    