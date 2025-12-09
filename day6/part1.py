import os
# inputFile = "sample.txt"
inputFile = "input1.txt"
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), inputFile), "r") as file:
   content = file.read()

graph = [list(row) for row in content.split('\n')]
height = len(graph)
width = len(graph[0])

position = (0, 0)
direction = 0
for i in range(len(graph)):
    for j in range(len(graph)):
        if graph[i][j] == "^":
            position = (i, j)

def getForwardPosition(i, j):
    if direction == 0:
        return i - 1, j
    if direction == 1:
        return i, j + 1
    if direction == 2:
        return i + 1, j
    else:
        return i, j - 1

def facingObstacle(x, y):
    i, j = getForwardPosition(x, y)
    return height > i >= 0 and width > j >= 0 and graph[i][j] == "#"

def printGraph():
    for row in graph:
        print(row)

while height > position[0] >= 0 and width > position[1] >= 0:
    x, y = position
    # printGraph()
    # print(direction)

    # print(x, y)
    graph[x][y] = "X"
    while facingObstacle(x, y):
        direction = (direction + 1) % 4
    position = getForwardPosition(x, y)

sum = 0
for row in graph:
    # print(row)
    for col in row:
        if col == "X":
            sum += 1

print(sum)
    
