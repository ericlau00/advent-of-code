system = open("input.txt").read().split("\n")

relationships, second_pass, total = dict(), dict(), 0

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
    if not 'COM' in relationships[outer]:
        second_pass[outer] = list()

while len(second_pass.keys()) > 0:
    for planet in list(second_pass.keys()):
        fill_rest = relationships[planet][-1]
        for n in relationships[fill_rest]:
            total += 1
            relationships[planet].append(n)
        if 'COM' in relationships[planet]:
            second_pass.pop(planet)

print("Answer to part 1:", total)

for planet in relationships['YOU']:
    if planet in relationships['SAN']:
        print("Answer to part 2:", relationships['YOU'].index(planet) + relationships['SAN'].index(planet))
        break
