# inputFile = "sample.txt"
inputFile = "input1.txt"
with open(inputFile, "r") as file:
    content = file.read()

def tryCombination(goalValue, nums, combo):
    combo = bin(combo)[2:].zfill(30)
    total = nums[0]
    for i in range(1, len(nums)):
        if combo[i * -1] == "1":
            total += nums[i]
        else:
            total *= nums[i]
        if total > goalValue:
            return False
    return total == goalValue

def checkEquation(equation):
    goalValue, nums = equation.split(":")
    goalValue = int(goalValue)
    nums = list(map(int, nums.split()))
    for i in range(2 ** (len(nums) - 1)):
        if tryCombination(goalValue, nums, i):
            return goalValue
    return 0

sum = 0
for equation in content.split('\n'):
    sum += checkEquation(equation)

print(sum)