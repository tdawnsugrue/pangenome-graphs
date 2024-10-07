

odgi extract -i $1 -o tmp.og -E -t16 -r "$2:10-10000"
odgi sort -i $1 -o tmp.og -L -t16
odgi viz -i tmp.og -o tmp.png -s "#" -t16
