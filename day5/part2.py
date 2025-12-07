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
        pageDict = {}
        for i in range(len(pages)):
            pageDict[pages[i]] = i
        pageOrders.append(pageDict)

def checkRule(pages, rule):
    start, end = rule
    return not start in pages or not end in pages or int(pages[start]) - int(pages[end]) <= 0

def isInOrder(pages):
    for rule in rules:
        if not checkRule(pages, rule):
            return False
    return True

def sortPages(pages):
    while not isInOrder(pages):
        for rule in rules:
            if not checkRule(pages, rule):
                start, end = rule
                temp = pages[start]
                pages[start] = pages[end]
                pages[end] = temp
                break

sum = 0
unordered = [pages for pages in pageOrders if not isInOrder(pages)]

for pages in unordered:
    sortPages(pages)

for pages in unordered:
    midIndex = len(pages)//2
    for page, order in list(pages.items()):
        if order == midIndex:
            sum += int(page)
            break

print(sum)

