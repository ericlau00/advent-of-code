system = open("input.txt").read().split("\n")

relationships = dict()

total = 0

for orbit in system:
    in_out = orbit.split(")")
    inner = in_out[0]
    outer = in_out[1]
    relationships[outer] = list()
    relationships[outer].append(inner)
    total += 1
    if inner in relationships:
        for planet in relationships[inner]:
            total += 1
            relationships[outer].append(planet)
    else:
        # for inner planets that have not yet been inserted into the dictionary, you need to make a second pass
