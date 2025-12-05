import re
import os
currentDir = os.path.dirname(os.path.abspath(__file__))
# filePath = os.path.join(currentDir, "sample2.txt")
filePath = os.path.join(currentDir, "input1.txt")

print(filePath)
with open(filePath, "r") as file:
   content = file.read()

pattern = re.compile(r"mul\(\d+,\d+\)|do\(\)|don't\(\)")
digitPattern = re.compile(r"\d+")

muls = pattern.findall(content)

sum = 0
enabled = True
for match in muls:
   if match == "do()":
      enabled = True
   elif match == "don't()":
      enabled = False
   elif enabled:
      first, second = digitPattern.findall(match)
      sum += int(first) * int(second)

print(sum)