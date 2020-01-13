import csv

with open('input2.txt') as file:
    nums = list(csv.reader(file))[0]

n = len(nums)
nums[1] = 12
nums[2] = 2
for i in range(0, n, 4):
    if int(nums[i]) == 1:
        nums[int(nums[i + 3])] = int(nums[int(nums[i + 1])]) + int(nums[int(nums[i + 2])])
    elif int(nums[i]) == 2:
        nums[int(nums[i + 3])] = int(nums[int(nums[i + 1])]) * int(nums[int(nums[i + 2])])
    elif int(nums[i]) == 99:
        break

print(nums[0])
