#!/bin/sh

cat giraffedv.2504unrelated.chr5.vcf | grep ^chr | grep -m 1 -w $1 | sed 's/:[^\t]*//g' > nonref_files/chr5-genos/upper_$1.txt