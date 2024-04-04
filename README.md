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