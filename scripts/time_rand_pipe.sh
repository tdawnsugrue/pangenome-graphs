odgi extract -i $1 -o tmp.og -E -t16 -r "GRCh38#chr$2:10-10000"
odgi sort -i $1 -o tmp.og -L
odgi viz -i tmp.og -o tmp.png -s "#"