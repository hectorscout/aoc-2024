# inputFile = "sample.txt"
inputFile = "input1.txt"
with open(inputFile, "r") as file:
    content = file.read()

def ternary (n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))

def tryCombination(goalValue, nums, combo):
    combo = ternary(combo).zfill(30)

    total = nums[0]
    for i in range(1, len(nums)):
        if combo[i * -1] == "1":
            total += nums[i]
        elif combo[i * -1] == "0":
            total *= nums[i]
        else:
            total = int(str(total) + str(nums[i]))

        if total > goalValue:
            return False
    return total == goalValue

def checkEquation(equation):
    goalValue, nums = equation.split(":")
    goalValue = int(goalValue)
    nums = list(map(int, nums.split()))
    for i in range(3 ** (len(nums) - 1)):
        if tryCombination(goalValue, nums, i):
            return goalValue
    return 0

sum = 0
for equation in content.split('\n'):
    sum += checkEquation(equation)

print(sum)