from fractions import Fraction
import math
# inputFile = "sample.txt"
inputFile = "input1.txt"
with open(inputFile, "r") as file:
    content = file.read()

lines = content.split('\n')
width = len(lines[0])
height = len(lines)

frequencies = {}

for x in range(width):
    for y in range(height):
        val = lines[y][x]
        if val != '.':
            if not val in frequencies:
                frequencies[val] = []
            frequencies[val].append((x, y))

antinodes = set()

def isInMap(node):
    x, y = node
    return 0 <= x < width and 0 <= y < height

def addAntinodes(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    slope = Fraction(y1 - y2, x1 - x2)
    rise = slope.numerator
    run = slope.denominator

    i = 0
    out1 = False
    out2 = False
    while True:
        node1 = (x1 + (run * i), y1 + (rise * i))
        if isInMap(node1):
            antinodes.add(node1)
        else:
            out1 = True
        node2 = (x1 - (run * i), y1 - (rise * i))
        if isInMap(node2):
            antinodes.add(node2)
        else:
            out2 = True
        i += 1
        if out1 and out2:
            break

for points in list(frequencies.values()):
    for i in range(len(points) - 1):
        for j in range(i + 1, len(points)):
            addAntinodes(points[i], points[j])

print(len(antinodes))