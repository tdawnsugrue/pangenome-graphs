import sys
import subprocess

chroms_dir = "" # directory for full chrom og files
exclude_list = [5] # chroms to skip
chromosomes = [i for i in range(1, 23)] + ["X", "Y"]


# autogen a paths file based on chromosome number
print(chromosomes)