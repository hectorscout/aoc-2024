import os
currentDir = os.path.dirname(os.path.abspath(__file__))
# filePath = os.path.join(currentDir, "sample.txt")
filePath = os.path.join(currentDir, "input1.txt")

print(filePath)
with open(filePath, "r") as file:
   content = file.read()

def diffIsUnsafe(diff, ascending):
    return(ascending and diff > 0) or (not ascending and diff < 0) or abs(diff) > 3 or diff == 0

def isSafe(levels, secondChance = True):
    ascending = levels[0] - levels[-1] < 0
    for i in range(len(levels) - 1):
        diff = levels[i] - levels[i+1]
        print(diff, ascending)
        if diffIsUnsafe(diff, ascending):
            print('unsafe')
            return secondChance and (i == len(levels) - 2 or isSafe(levels[:i] + levels[i+1:], False) or isSafe(levels[:i+1] + levels[i+2:], False))
    
    return True

safeReports = 0

for report in content.split("\n"):
    print(report)
    levels = list(map(int, report.split()))
    if isSafe(levels):
        print("safe")
        safeReports += 1

print(safeReports)
