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

#### IRGM test

using `chr5.full.og` direct from the hprc resources to extract the IRGM region as specified in Mik's [GENE315 project](https://github.com/mikblack/GENE315-CNVlab/blob/master/GENE315-CNV_lab-week1.md).  
Used the following command: `odgi extract -i chr5.full.og -o irgm-subgraph-315.og -P -E -r GRCh38#chr5:150124000-150324000`  

Then made a list of some samples to grab based on known CN variants - see [PUT FILE LINK/s HERE](data/irgm-urls.csv).

| Sample/s (in order) | Population | [Copy number](https://github.com/mikblack/GENE315-CNVlab/blob/master/CNcalls.csv) |
| --- | --- | --- |
| NA06984 - 2 - CEU
| NA06986 - 1 - CEU
| NA18526 - 2 - CHB
| NA18528 - 0 - CHB
| NA18486 - 1 - YRI
| NA18499 - 0 - YRI

(Kicking myself... some files on my other (DEAD) laptop... hopefully they can be saved if the battery behaves tomorrow)
(it did not.)

NOTE: extracted the graph for positions in chr5 150124000 - 150324000  
    actual positions when mapped were 150123854 - 150324068 (i.e. slightly longer)md/.obsidian

150950736
### Step-by-step read mapping

1. Download relevant graph from the [hprc resources page](https://github.com/human-pangenomics/hpp_pangenome_resources)  
    - this should be in odgi (`.og`) format. Recommended to grab 1 chromosome as opposed to the full graph as it's faster
2. Run `odgi extract` with the correct ranges; can pass these as arguments or as a BED file.  
    - example: `odgi extract -i chr5.full.og -o irgm-wider-region.og -P -E -r GRCh38#chr5:150796521-150950736`
3. Run `odgi view` to convert the extracted file into gfa format, then use `vg autoindex` to generate gbz and other graph [stuff].
    - example: `odgi view -g -i irgm-wider-region.og > irgm-wider-region.gfa` followed by `vg autoindex --workflow
4. Get an appropriately formatted csv file with your samples and regions of interest (see [this file](/data/fcgr3b-urls.csv)) as an example.
5. Run `scripts/get_fastqs.py` from the base folder. (note this has some hardcoded values, may need to adjust as nessecary until I update this). This will produce a bunch of mapped gam files based on the reads you provided.
6. Run `depth_from_gam.py` to get base-level depths
7. Run `graph_depth_files.py` to get corresponding graphs; you may need to alter this file as of writing (17/6/24)


### Jul 16 - odgi notes

TODO: move paper notes here...

also maybe? refer odgi viz in [readthedocs](https://odgi.readthedocs.io)

also refer to `odgi bin`. Apparently viz only takes the *concept* of binning, however (as may be obvious from the fact it consists of a single, 1500+ line-long function...)

 Note this mentions a software called `Pantograph` which supposedly does this interactively - this can be sort of seen on its site at [computomics](https://computomics.com/services/pangenomes.html). Pretty sure this is proprietary >:/

 ### Jul 31 - ODGI viz notes

    - you can specify path intervals *directly* in the source version of odgi - this clearly hasn't been included in the version/s they distribute (yet)
    - 1. going to test whether the default version works for the hpgp examples:

Odgi extract from chr5 - took 2min on lab computer (read: 3nr gen i7)

Running odgi sort | odgi viz on the subgraph takes ~1.7s
Running *without* doing sort first takes slightly shorter.

Running on the *whole* chr5 takes approx 2min (realistically almost no one is going to do this but funny)

The problem with running odgi like this is that we need to run odgi extract for each subgraph. Can we run odgi viz directly 

HOWEVER we can run the following command (requires building from source)
```
odgi viz -i chr5.full.og -o irgm_region.png -s '#'-rGRCh38#chr5:150796521-150950736
```
...Unfortunately, this takes around 2min to run, and produces a graph that looks absolutely nasty.

As such, it's probably not super feasible to implement something that allows you to look at different regions of the graph (at least not from a whole chromosome).

> Note: may try making a docker image of this version of viz so other people (and I) can play around with it some more

Other things to check:
    - possibly run timings on a whole range of sizes? If we need to
    - Changing binning options
    - sorting (and filtering?) paths.
        - See if there's any options for this in the source version
        - See if there's anywhere in the code that may be modified to make this an option
        - `--paths-to-dispay` is one option but requires you to *specify* paths, so not great for auto-filter
    - Changing binning options
        - i.e. seeing smaller changes
        - Pretty sure I located the function for this; see if I can re-enable (if there's a useful setting and they don't have it hardcoded.)
        - test `-w[bp]` argument
    - Look at IGV code & see what it's doing
        - as an example of a responsive genome viewer
        - how would we do this with something pangenomic
            - especially if we map reads to it - maybe collapsing/expanding sections as necessary?

---

### Aug 2

- Tested the bin width argument of odgi viz (provided with `-w[bp]`)
    - lower values of `bp` result in a much longer image, but it seems to pick up smaller variation/more detail.
    - note that along the bottom there are a number of small 'bumps' - do these represent smaller changes?
    - **NOTE** running with bin_width = 1 creates a *very* long image, but (presumably) captures everything

### Aug 6

#### Notes on ODGI

- `odgi sort` may have alternate options for sorting. Need to look into this and then play around with the subcommand and odgi viz to test this
- "sgd" stands for Stochastic Gradient Descent.
- they talk about sorting paths [here](https://odgi.readthedocs.io/en/latest/rst/tutorials/sort_layout.html). Presumably viz then displays them in the given optimised order. Means if we wanted to sort on the fly we'd want to pass the original graph through `odgi sort`.
- so if we were to build a gui on top of the odgi subcommands, we'd have to implement multiple. Presumably would be better to run this directly rather than e.g. routing bash through python (if that makes sense.)  
    - You *can* run C code through python so this should be doable, if that's the direction we want to go in.
- note that odgi sort sorts the *nodes* in each path. It doesn't *reorder* paths [Based on this](https://odgi.readthedocs.io/en/latest/rst/tutorials/sort_layout.html)
    - there is an interactive ***2D***  viewer, as seen at the bottom of the article above.
    - While you can't sort the order of the paths with the sort subcommand, you can use different paths as a reference. Not sure what kind of effect this has (should probably test this...)

What if we run with these options?

```
      [ Path Sorting Options ]
        -L, --paths-min                   Sort paths by their lowest contained
                                          node identifier.
        -M, --paths-max                   Sort paths by their highest contained
                                          node identifier.
        -A, --paths-avg                   Sort paths by their average contained
                                          node identifier.
        -R, --paths-avg-rev               Sort paths in reverse by their average
                                          contained node identifier.
```

So:

`./bin/odgi sort -i irgm-region-chr5.og -o - -O -[LMAR] | ./bin/odgi viz -i - -o irgm_sort_[LMAR].png -s '#`  

Results sort the paths - nice!  
*note that apparently this is (probably) not deterministic


#### Notes on IGV

- while the *web* application is written in js (framework?), the desktop version of IGV is a java application. 
- [source is available here](https://github.com/igvteam/igv/tree/main)
- TODO also look at the web app

#### !Important! TODO

- talks are end of Aug, abstract for talk due ~mid-august (get exact date for this).
- Need to have a 'narrative' in mind
    - for the process of a writeup, do we want to apply what we've done to a particular example? (I.e. this has benefits e.g in [this region]... etc.)
    - main motivation for this would be to make sure there's enough biochemistry in this biochem thesis...

### Aug 13

Wrote the bare bones of an app to run odgi under the hood and display graphs. Currently this requires a working version of odgi built from source (which for various reasons is not ideal), however you *can* run sort. Currently other options are a work in progress.

#### How to run:

You should have `Pillow` and `customtkinter` installed:
```pip install Pillow customtkinter```

You'll also need a version of odgi (preferably built from source) in the `bin` directory. Alternately, you can alter line 81 to run with just `odgi` instead of `.bin/odgi` (sorry.)

Finally, you'll need a .og graph in the source directory of the repo. This works best if you're looking at a region - an entire chromosome is probably a bad idea.

run the app from the source directory with the following command:
```python scripts/odgi_app.py```

### Sep 10

...should probably be writing/updating more often...

Path coords for grch38: 
150796142
150951030

testing 150800000 - 150900000

*HEY SO REMEMBER WHEN ODGI EXTRACT WASN'T WORKING? I FOUND OUT WHY*

#### IMPORTANT

`odgi extract` *appends coordinates* to the original pathnames, which is what causes the area if you try use odgi extract again...

*and* if you use *absolute* coords you'll get a seg fault, you have to account for offset!