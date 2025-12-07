import os
# inputFile = "sample1.txt"
inputFile = "input1.txt"
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), inputFile), "r") as file:
   content = file.read()

rows = content.split('\n')
rowCount = len(rows)
colCount = len(rows[0])

def isAnX(i, j):
    if rows[i][j] != "A":
        return False
    return ((rows[i-1][j-1] == "M" and rows[i+1][j+1] == "S") or (rows[i-1][j-1] == "S" and rows[i+1][j+1] == "M")) and ((rows[i+1][j-1] == "M" and rows[i-1][j+1] == "S") or (rows[i+1][j-1] == "S" and rows[i-1][j+1] == "M")) 

numMatches = 0
for i in range(1, len(rows) - 1):
    for j in range(1, len(rows[0]) - 1):
        if isAnX(i, j):
          numMatches += 1

print(numMatches)