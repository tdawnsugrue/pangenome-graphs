import os
import sys
from reformat_vgstats import extract_vals

def checks():
    if "data" not in os.listdir():
        print("data directory not found! Are you running this from the correct folder?", file=sys.stderr)
        exit()
    if len(sys.argv) < 2:
        print("error! Usage: python get_fastqs.py [URL-FILE]", file=sys.stderr)
        exit()

def get_bam(dat: list):
    url = dat[-1]
    prefix = f"{dat[0]}-{dat[1]}-{dat[2]}"
    os.system(f"samtools view -b {url} {dat[3]}:{dat[4]} | samtools fastq > fastq/{prefix}.fq")

graphs = {"1" : "fcgr-giraffe", "2" : "irgm-315", "3" : "irgm-wider-region"}

if __name__ == "__main__":
    checks()

    outfile = open(input("Enter path for output stats file: "), "w")
    outfile.write("genome,population,gene,total_alignments,n_aligned,n_perfect,n_gapless,vgdepth_a,vgdepth_b\n")

    download = input("Download BAM files?Y/[N]")
    download = download in "YesyesYES"
    print("downloading set to", download, file=sys.stderr)
    prefixes = []

    graph = graphs[input("""Which graph to map to?\n
                      1\tfcgr-giraffe\tfcgr(old)\n
                      2\tirgm-315\tirgm subgraph from GENE315 lab
                      3\tirgm-wider-region\t proper irgm region...""")]


    file = open(sys.argv[1])
    for line in file.readlines():
        dat = [d.strip() for d in line.split(",")]
        #print(dat)
        if dat[0] == "id" : continue # skip header line

        prefix = f"{dat[0]}-{dat[1]}-{dat[2]}"
        prefixes.append(prefix)

        
        if download:
            print(f"downloading {prefix}...", file=sys.stderr)
            get_bam(dat)

        
        print(f"running vg tools on {prefix}", file=sys.stderr)
        os.system(f"vg giraffe -g graphs/{graph}.giraffe.gbz -d graphs/{graph}.dist -m graphs/{graph}.min -f fastq/{prefix}.fq > mapped/{prefix}-mapped.gam")
        os.system(f"vg stats -a mapped/{prefix}-mapped.gam > tmp.txt")
        #os.system(f"vg depth -g mapped/{prefix}-mapped.gam graphs/fcgr-giraffe.giraffe.gbz >> tmp.txt")
        
        aln_stats = extract_vals("tmp.txt")
        x = f"{dat[0]},{dat[1]},{dat[2]}"
        for v in aln_stats:
            x += "," + v
        x += "\n"
        outfile.write(x)

    outfile.close()
    file.close()
    print("\ndone.")