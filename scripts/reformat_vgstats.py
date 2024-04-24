import re
import sys

regx = re.compile(r"Total ([a-zA-Z]+)[ \(\)a-zA-z]*: (\d+)")
rel = ['alignments', 'aligned', 'perfect', 'gapless']


def extract_vals(lines):
    vals = []
    if type(lines) == str:
        f = open(lines)
        lines = [i.strip() for i in f.readlines()]
        f.close()

    for line in lines:
        x = re.match(regx, line)
        if x:
            if x.group(1) in rel:
                vals.append(x.group(2))
    
    depth = lines[-1].split()
    vals += depth

    return vals

def single(line: str):
    x = re.match(regx, line)
    if x:
        if x.group(1) in rel:
            return x.group(2)
    return None


def testrun():
    f = open("vgstatex.txt")
    v = extract_vals(f.readlines())
    f.close()
    f = open("test.out", "w")
    for i, n in enumerate(v):
        w = str(n) + "," if i != len(v)-1 else str(n)
        f.write(w)
    f.close()

if __name__ == "__main__":
    start = True
    for line in sys.stdin:
        val = single(line)
        if val:
            print(val if start else "," + val, end="")
            start = False
    print()