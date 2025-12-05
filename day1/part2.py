import os
currentDir = os.path.dirname(os.path.abspath(__file__))
# filePath = os.path.join(currentDir, "sample.txt")
filePath = os.path.join(currentDir, "input1.txt")

print(filePath)
with open(filePath, "r") as file:
   content = file.read()

row1 = []
row2 = {}

for line in content.split("\n"):
   inputs = line.split()
   row1.append(int(inputs[0]))
   curCount = row2.get(int(inputs[-1]), 0)
   row2[int(inputs[-1])] = curCount + 1

sum = 0
for id in row1:
   sum += id * row2.get(id, 0)

print(sum)
