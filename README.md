# pangenome-graphs

Currently serving as a stream-of-consciousness/etc until I can get something more organised

### (Attempted) Mapping to workshop graphs

#### pggb

All relevant files can be found in the `hprc-workshop` folder.

Graphs were generated using the following command, with the [HLA-zoo](#) repo in the same directory:  
```
pggb -i [file.fa] -n [num-haplotypes] -t 8 -o [output folder]
```
Genes other than DRB1 also need to be run with the flag `-s 1k` to produce any draw output.


Stats can then be viewed with (.og files not included in the repo currently)
```
odgi stats -i *.smooth.final.og
```

Note that genes other than DRB1 don't seem to have a  proper *.draw_multiqc.png output.

#### mapping

After retrieving the 1k genomes files using samtools, the following were run to attempt mapping:
```
samtools fastq [FILE.bam] > [File.fastq] #convert
vg autoindex --workflow giraffe -g [GFA file] -p [prefix] # creates .gbz, .min and .dist files
vg giraffe -Z [FILE.gbz] -m [FILE.min] -d [FILE.dist] > mapped.gam
vg stats -a mapped.gam # get stats on mapping
```

Of the 505 alignments in the HLA-DRB1 region of HG00096, only 6 managed to align.

---

### Mapping to prebuilt graphs

This was done using the minigraph-cactus pangenome ([here](https://github.com/human-pangenomics/hpp_pangenome_resources?tab=readme-ov-file)), doing the following

```
wget -c https://s3-us-west-2.amazonaws.com/human-pangenomics/pangenomes/freeze/freeze1/minigraph-cactus/hprc-v1.1-mc-grch38/hprc-v1.1-mc-grch38.gfa.gz
gunzip hprc-v1.1-mc-grch38.gfa.gz
```

Unfortunately getting the correct version of odgi was somewhat problematic. Conda appears to install the *earliest* version of odgi by default - this could be an issue with odgi itself, but may be caused by conflicts with vg or pggb (I know at the very least pggb uses odgi as part of its workflow). This is an issue because `odgi extract` is missing from v0.2.0 along with a lot of other functions (vs. current newest 0.8.6)
 Conda wouldn't stop complaining about libc and python (no matter the version I tried to use). This issue can be replicated on the server by creating a new conda environment, and then running:

```
conda install bioconda::odgi=0.8.6
```
adding conda-forge and/or other channels doesn't seem to help. Nor does installing on a local machine on conda. Attempting to build from source seems to cause other issues (I've only tried this locally.)

Building with docker/singularity appears to work though I'd prefer I didn't need containers to run this stuff. I installed and ran the image with:
```
singularity pull odgi.sif docker://quay.io/biocontainers/odgi:0.8.6--py310h6cc9453_0
singularity run --bind $(pwd):/root odgi.sif
```

> running build took ? minutes. 

`odgi extract -i [input.og] -o [output.og] -b [genes.bed] -L1000000 -E --threads 2 -P`  
^ odgi complains about not optimised, so:  
`odgi sort -i [iput.og] -o [sorted.og] -O -P`, which takes ~2.5min

Then extract as before. odgi complains *again* because a certain grch38 path (if not multiple) doesn't exist.

