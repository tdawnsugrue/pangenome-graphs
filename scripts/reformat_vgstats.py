import re

regx = re.compile(r"Total ([a-zA-Z]+)[ \(\)a-zA-z]*: (\d+)")
rel = ['alignments', 'aligned', 'perfect', 'gapless']

vals = []
def extract_vals(lines: list):
    
    for line in lines:
        x = re.match(regx, line)
        if x:
            if x.group(1) in rel:
                vals.append(x.group(2))
    
    return vals

if __name__ == "__main__":
    f = open("vgstatex.txt")
    v = extract_vals(f.readlines())
    f.close()
    f = open("test.out", "w")
    for i, n in enumerate(v):
        w = str(n) + "," if i != len(v)-1 else str(n)
        f.write(w)
    f.close()