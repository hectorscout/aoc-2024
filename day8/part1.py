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
    dx = x1 - x2
    dy = y1 - y2

    node1 = x1 + dx, y1 + dy
    node2 = x2 - dx, y2 - dy

    if isInMap(node1):
        antinodes.add(node1)
    if isInMap(node2):
        antinodes.add(node2)
    return

for points in list(frequencies.values()):
    for i in range(len(points) - 1):
        for j in range(i + 1, len(points)):
            addAntinodes(points[i], points[j])

print(len(antinodes))