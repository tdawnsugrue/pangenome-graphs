#!/bin/sh

rm data/rand_times_raw.txt
touch data/rand_times_raw.txt

for file in ./graphs/random/*
do
    echo "${file}" >> data/rand_times_raw.txt
    time <(odgi extract -i $file -o _ -E -t16 && odgi sort -i $file -L && odgi viz -i ) >> data/rand_times_raw.txt