import os
currentDir = os.path.dirname(os.path.abspath(__file__))
# filePath = os.path.join(currentDir, "sample.txt")
filePath = os.path.join(currentDir, "input1.txt")

print(filePath)
with open(filePath, "r") as file:
   content = file.read()

def isSafe(report):
    print(report)
    levels = list(map(int, report.split()))
    ascending = levels[0] - levels[-1] < 0
    for i in range(len(levels) - 1):
        diff = levels[i] - levels[i+1]
        print(diff)
        if (ascending and diff > 0) or (not ascending and diff < 0) or abs(diff) > 3 or diff == 0 :
            return False
    return True

safeReports = 0

for report in content.split("\n"):
    if isSafe(report):
        print("safe")
        safeReports += 1

print(safeReports)
