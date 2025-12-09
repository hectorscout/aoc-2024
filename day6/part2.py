import os
# inputFile = "sample.txt"
inputFile = "input1.txt"
with open(inputFile, "r") as file:
   content = file.read()

graph = [list(row) for row in content.split('\n')]
height = len(graph)
width = len(graph[0])

startPosition = (0, 0)
for i in range(height):
    for j in range(width):
        if graph[i][j] == "^":
            startPosition = (i, j)

def getForwardPosition(direction, i, j):
    if direction == 0:
        return i - 1, j
    if direction == 1:
        return i, j + 1
    if direction == 2:
        return i + 1, j
    else:
        return i, j - 1

def facingObstacle(direction, x, y, bonusI, bonusJ):
    i, j = getForwardPosition(direction, x, y)
    return (bonusI == i and bonusJ == j) or (height > i >= 0 and width > j >= 0 and graph[i][j] == "#")

position = startPosition
myDir = 0
while height > position[0] >= 0 and width > position[1] >= 0:
    x, y = position
    graph[x][y] = "X"
    if facingObstacle(myDir, x, y, -10, -10):
        myDir = (myDir + 1) % 4
    position = getForwardPosition(myDir, x, y)

def checkForLoop(i, j):
    if graph[i][j] != "X":
        return False
    position = startPosition
    directions = {}
    direction = 0
    while True:
        x, y = position
        if not position in directions:
            directions[position] = set()
        directions[position].add(direction)
        
        while facingObstacle(direction, x, y, i, j):
            direction = (direction + 1) % 4
        position = getForwardPosition(direction, x, y)

        if position[0] < 0 or position[0] >= height or position[1] >= width or position[1] < 0:
            return False
        if direction in directions.get(position, []):
            return True

sum = 0
for i in range(len(graph)):
    for j in range(len(graph[i])):
        if checkForLoop(i, j):
            sum += 1

print(sum)
