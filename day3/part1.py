import re
import os
currentDir = os.path.dirname(os.path.abspath(__file__))
# filePath = os.path.join(currentDir, "sample.txt")
filePath = os.path.join(currentDir, "input1.txt")

print(filePath)
with open(filePath, "r") as file:
   content = file.read()

pattern = re.compile(r"mul\(\d+,\d+\)")
digitPattern = re.compile(r"\d+")

muls = pattern.findall(content)

sum = 0
for mul in muls:
   first, second = digitPattern.findall(mul)
   sum += int(first) * int(second)

print(sum)