import os
currentDir = os.path.dirname(os.path.abspath(__file__))
# filePath = os.path.join(currentDir, "sample.txt")
filePath = os.path.join(currentDir, "input1.txt")

print(filePath)
with open(filePath, "r") as file:
   content = file.read()

row1 = []
row2 = []

for line in content.split("\n"):
   inputs = line.split()
   row1.append(int(inputs[0]))
   row2.append(int(inputs[-1]))

row1.sort()
row2.sort()

sum = 0
for i in range(len(row1)):
   sum += max(row1[i], row2[i]) - min(row1[i], row2[i])

print(sum)