#!/bin/sh

rm data/rand_times_raw.txt
touch data/rand_times_raw.txt

for file in ./graphs/random/*
do
    echo "doing ${file}"
    echo "${file}" >> data/rand_times_raw.txt
    time <(odgi extract -i $file -o _ -E -t16 && odgi sort -i $file -L &&
            odgi viz -i $file -o _ -s '#') >> data/rand_times_raw.txt