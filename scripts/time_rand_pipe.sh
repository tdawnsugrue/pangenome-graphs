

odgi extract -i $1 -o tmp.og -E -r "$2:10-10000" -t16
odgi sort -i $1 -o tmp.og -L -t16
odgi viz -i tmp.og -o tmp.png -s "#" -t16
