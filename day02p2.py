import csv


def intcode(nums):
    n = len(nums)
    for ii in range(0, n, 4):
        if int(nums[ii]) == 1:
            nums[int(nums[ii + 3])] = int(nums[int(nums[ii + 1])]) + int(nums[int(nums[ii + 2])])
        elif int(nums[ii]) == 2:
            nums[int(nums[ii + 3])] = int(nums[int(nums[ii + 1])]) * int(nums[int(nums[ii + 2])])
        elif int(nums[ii]) == 99:
            break
    return nums[0]


with open('input2.txt') as file:
    original_nums = list(csv.reader(file))[0]

gotit = False

for i in range(100):
    for j in range(100):
        nums = original_nums.copy()
        nums[1] = i
        nums[2] = j
        result = intcode(nums)
        if result == 19690720:
            print(i, j)
            gotit = True
            break
    if gotit:
        break
