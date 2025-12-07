import os
# inputFile = "sample.txt"
inputFile = "input1.txt"
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), inputFile), "r") as file:
   content = file.read()

doingRules = True
rules = []
pageOrders = []
for row in content.split('\n'):
    if row == "":
        doingRules = False
        continue
    
    if doingRules:
        rules.append(row.split('|'))
    else:
        pages = row.split(',')
        pageDict = {"mid": int(pages[len(pages)//2])}
        for i in range(len(pages)):
            pageDict[pages[i]] = i
        pageOrders.append(pageDict)

def isInOrder(pages):
    for start, end in rules:
        # if start == '97' and end == '75' and pages.get(start) and pages.get(end):
            # print(pages[start], pages[end])
        if start in pages and end in pages and int(pages[start]) - int(pages[end]) > 0:
            return False
    return True

print(rules)

sum = 0
for pages in pageOrders:
    # print(pages)
    if isInOrder(pages):
        # print(pages["mid"])
        sum += pages["mid"]

print(sum)

