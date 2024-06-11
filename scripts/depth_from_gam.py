import os
import sys

if __name__ == "__main__":
    try:
        file = open(sys.argv[1])
        for line in file.readlines():
            dat = [d.strip() for d in line.split(",")]
            print(dat)
            if dat[0] == "id" : continue # skip header line

            prefix = f"{dat[0]}-{dat[1]}-{dat[2]}"

            print(f"running vg on {prefix}...", file=sys.stderr)

            os.system(f"vg pack -x graphs/fcgr-giraffe.giraffe.gbz -g mapped/{prefix}-mapped.gam -o tmp.pack")
            os.system(f"vg depth -k tmp.pack graphs/fcgr-giraffe.giraffe.gbz > data/depths/{prefix}-depth.tsv")
        os.system(f"rm tmp.pack")
    except:
        print("Invalid csv! Usage: python depth_from_gam.py <genes.csv>")