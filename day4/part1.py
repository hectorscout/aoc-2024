import os
# inputFile = "sample1.txt"
inputFile = "input1.txt"
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), inputFile), "r") as file:
   content = file.read()

rows = content.split('\n')
rowCount = len(rows)
colCount = len(rows[0])

def forward(i,j):
    return j <= colCount - 4 and rows[i][j+1] == "M" and rows[i][j+2] == "A" and rows[i][j+3] == "S"

def backwards(i,j):
    return j >= 3 and rows[i][j-1] == "M" and rows[i][j-2] == "A" and rows[i][j-3] == "S"

def up(i,j):
    return i >= 3 and rows[i-1][j] == "M" and rows[i-2][j] == "A" and rows[i-3][j] == "S"

def down(i,j):
    return i <= rowCount - 4 and rows[i+1][j] == "M" and rows[i+2][j] == "A" and rows[i+3][j] == "S"

def forwardUp(i,j):
    return j <= colCount - 4 and i >= 3 and rows[i-1][j+1] == "M" and rows[i-2][j+2] == "A" and rows[i-3][j+3] == "S"

def forwardDown(i,j):
    return j <= colCount - 4 and i <= rowCount - 4 and rows[i+1][j+1] == "M" and rows[i+2][j+2] == "A" and rows[i+3][j+3] == "S"

def backwardsUp(i,j):
    return j >= 3 and i >= 3 and rows[i-1][j-1] == "M" and rows[i-2][j-2] == "A" and rows[i-3][j-3] == "S"

def backwardsDown(i,j):
    return j >= 3 and i <= colCount - 4 and rows[i+1][j-1] == "M" and rows[i+2][j-2] == "A" and rows[i+3][j-3] == "S"

def getNumMatches(i, j):
    matches = 0
    if rows[i][j] != "X":
        return matches
    if forward(i, j):
        matches += 1
    if backwards(i, j):
        matches += 1
    if up(i, j):
        matches += 1
    if down(i, j):
        matches += 1
    if forwardUp(i, j):
        matches += 1
    if forwardDown(i, j):
        matches += 1
    if backwardsUp(i, j):
        matches += 1
    if backwardsDown(i, j):
        matches += 1
    return matches
   

numMatches = 0
for i in range(len(rows)):
    for j in range(len(rows[0])):
        numMatches += getNumMatches(i, j)

print(numMatches)