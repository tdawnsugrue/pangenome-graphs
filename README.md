# Getting More out of the Graph

Working repo for hons dissertation 2024. Please mind the dust.  

## GraphViewer

An interface for working with `odgi viz`, which generates 1D representations of pangenomes from `.og` files.  

### How to run GraphViewer

NOTE: Due to the limitations of odgi, this currently only works on linux.  

You'll need the following python packages:

```
pip install Pillow customtkinter
```

The easiest way to run odgi is to set up a conda environment. Once you have an environment set up, install odgi with the following command, then verify you have the latest version of odgi.

```
conda install bioconda::odgi
odgi version
```

You can also compile odgi from source - refer to [their repo](https://github.com/pangenome/odgi) for details on how to do this.

Then, run the app from the source directory of this repo:  
```
python scripts\odgi_app.py
```

#### Alternative: Running with the prebuilt binary

This works on Ubuntu - I'm not sure of its compatibility with other linux distros. 

To run with the prebuilt binary, simply uncomment line 25 in `scripts\odgi_app.py`.

## Missing regions

Currently working on this - check back later :)