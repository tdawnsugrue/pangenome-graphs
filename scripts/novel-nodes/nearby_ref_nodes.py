from sys import stderr
node = 1030533


def get_nearby_nodes(tgt: int):
    with open("chr5-depths.txt") as file:
        nodes = [int(i.split("\t")[0]) for i in file.read().split("\n")[1:-1] if i.split("\t")[1] != "0"]

    upper = tgt
    lower = tgt

    found = [False, False]

    while sum(found) != 2:
        if not found[0]:
            if upper in nodes:
                found[0] = True
            else:
                upper += 1
        if not found[1]:
            if lower in nodes:
                found[1] = True
            else:
                lower -= 1

    print(f"Flanks for {tgt}\n{upper}\n{lower}", file = stderr)
    return (upper, lower)