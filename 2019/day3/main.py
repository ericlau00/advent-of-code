import os


def step(path, start, plane, distance, step):
    for i in range(distance):
        start[plane] += step
        path.append(f"{start[0]}, {start[1]}")
    return start, path


def move(path, start, direction, distance):
    if direction == 'R':
        start, path = step(path, start, 0, distance, 1)
    if direction == 'U':
        start, path = step(path, start, 1, distance, 1)
    if direction == 'L':
        start, path = step(path, start, 0, distance, -1)
    if direction == 'D':
        start, path = step(path, start, 1, distance, -1)
    return start, path


def findDistance(wires):
    start = [0, 0]
    first = wires[0].split(',')
    firstpath = list()
    print('Generating first path...')
    for step in first:
        direction = step[0]
        movement = int(step[1:])
        start, firstpath = move(firstpath, start, direction, movement)

    start = [0, 0]
    second = wires[1].split(',')
    secondpath = list()
    print('Generating second path...')
    for step in second:
        direction = step[0]
        movement = int(step[1:])
        start, secondpath = move(secondpath, start, direction, movement)

    crosses = list()
    print('Finding cross points...')
    if len(firstpath) < len(secondpath):
        for point in firstpath:
            if point in secondpath:
                crosses.append(point)
    else:
        for point in secondpath:
            if point in firstpath:
                crosses.append(point)

    distances = list()
    print('Finding distances...')
    for point in crosses:
        point = point.split(',')
        distances.append(abs(int(point[0])) + abs(int(point[1])))

    return min(distances)



testPaths = [
    ['R8,U5,L5,D3', 'U7,R6,D4,L4'],
    ['R75,D30,R83,U83,L12,D49,R71,U7,L72', 'U62,R66,U55,R34,D71,R55,D58,R83'],
    ['R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51',
        'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7']
]

# for test in testPaths:
#     print(findDistance(test))

paths = open(os.path.dirname(__file__) + '/input.txt').read().split('\n')

print(findDistance(paths))