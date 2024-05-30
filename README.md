# pangenome-graphs

Currently serving as a stream-of-consciousness/etc until I can get something more organised

## TODO

 [ ] visualise subgraph with bandage to check lengths/etc  
 [ ] map with 1kg data  
 [ ] sim with fastq instead of gam?  
 [ ] move this to its own `notes.md` and cleanup the readme to be more useful

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

## Mapping

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

Running with the .og file direct from hprc (vs building) results in the exact same error...  
it may also be possible to do this with `vg chunk` but the wording of the documentation is opaque.

May be able to extract specific regions with coordinates as op74,2.03775posed to a bed file.

### HOW TO EXTRACT SUBGRAPHS (sort of... see below)

trying:  
`odgi extract -i [hprcv1.1...og] -o [test.og] [threads] -P -E -r GRCh38#chr1:161505457-161678654 -L1000000`

turns out the tag is **case sensitive**. My bad.
The above code worked - converted it to gfa using `odgi view`. Not sure where to look for genome annotations... skipping over that for now & visualising via bandage.

#### mapping (again)

The code below was executed to do the following:
 1. generate an index for mapping
 2. simulate reads from the graph containing the fcgr genes
 3. map the simulated reads to the graph
 4. get statistics on mapping

```
vg autoindex --workflow giraffe -g fcgr-subgraph.gfa -p fcgr-giraffe
vg sim -x fcgr-giraffe.giraffe.gbz -n 1000 -l 150 -a > fcgr.sim.gam
vg giraffe -Z fcgr-giraffe.giraffe.gbz -m fcgr-giraffe.min -d fcgr-giraffe.dist  -G fcgr.sim.gam > sim_fcgr_mapped.gam
vg stats -a sim_fcgr_mapped.gam
```

Results for simulated data were as follows:  
| total alignments | total aligned | total perfect | total gapless |
| --- | --- | --- | --- |
| 1000 | 1000 | 747 | 991 |

reads from the 1k genomes project were then pulled and converted to fastq using samtools; using hg00096 (each gene for fcgr2/3 was pulled separately). They were then run through `vg giraffe` as above (though -f was used in -G as we are working with fastq files.)  
Alignment stats for these genes (and the simulated reads) are in `fcgr-h0096-mapped.csv`.

```
samtools view -b [file] > output.bam
samtools fastq output.bam > output.fastq
```

FCGR2B was particularly in terms of number aligned; it sits on the edge of the graph so possibly why? Though the graph (should) be extended by 1MB in either direction.

I think (possibly) that odgi extract did *not* grab 1MB in either direction (based on bandage specifically; reports a length of ~250k bases). Side note - bandage is *old* (zip said last modified ~2016.)

---
### Looking at FCGR variants

Now I want to look at reads across different duplication/deletion events (CNVs in fcgr; across different 1kg genomes.)  

First, to get the depth from the HG we run:  
```
vg depth -g [mapped gam file] fcgr-giraffe.giraffe.gbz
```

...which will output 2 numbers. Presumably the first is an estimation of the read depth; not sure of the second. The read depth for hg96 genes can be found in [the data folder](data/)

NOW: doing the same for the following genes ( see [the relevant csv](data/fcgr3b-aln-data.csv) for results.)

Alignments seem to be mostly fine. Depth numbers are a little wacky. I can't seem to find any documentation for what the outputs of `vg depth` are supposed to mean - is it max & min possible depth? Not entirely sure.

---

## Visualisation

Most visualisation tools that exist are A.) made to work with specific types of graphs and B.) rather outdated (last update being 3 or more years ago.)

3 Tools standout as still being in (seemingly) regular use.  

1.) GraphViz  
    - this is a general graphing tool; not designed with genome graphs in mind  
    - hard to find information on how it's being used with pangenome graphs in particular. the vgtools suite  mentions it can be used but doesn't provide information beyond generating a `.dot` file for it.  
2.) Bandage  
    - Made for genome graphs; an older tool  hprcv1.1...  
3.) sequenceTubeMap  
    - JS tool for visualising pangenome graphs; by vgteam  
    - updated recently  
    - finicky at getting to specific regions in the graph...  
        - region is necessary to show. Can't just look at the whole thing (possibly because this breaks in-browser)  
        - for some reason queries starting with GRCh38# don't work  
    - I'm having issues getting this running. Could seemingly get it to work initially (using the gbz subgraph as both graph & haplotype + fcgr2a as read data) - but upon trying to change anything I get a popup message of `vg view failed`..  
        - see the one working graph [here](img/seqtubegraph-fcgr2a-hg96-mapped.svg)  

possibly relevant papers for visualisation specifically (talks about tools generically, not specific to graphs)  
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6876635/  


---
hprcv1.1...
- extract the subgraph using `odgi extract`
- convert to gfa using `odgi view` (or `vg view`) (not sure how to use the latter)


**Then**
- make a template file to pull out reads based on `get_fastqs.py` *NOTE: update this script to do base-level coverage on pack data (see `pack-depths.py`)
- make some cool graphs

#### x

Original graph used is `hprc-v1.1-mc-grch38.full.og`, run through `odgi sort` (Hprc minigraph-cactus pangenome, in .og form)

ran the following exact command/s:  
(odgi run in the singularity container)  

`odgi extract -i graphs/hprc-sorted-mc.og -o graphs/GENE315-fcgr.og