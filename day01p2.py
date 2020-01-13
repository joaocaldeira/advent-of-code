import numpy as np

with open('input1.txt') as file:
    nums = np.loadtxt(file)

answer = 0
while np.any(nums > 0):
    nums = np.maximum(nums//3 - 2, 0)
    answer += np.sum(nums)

print(answer)
