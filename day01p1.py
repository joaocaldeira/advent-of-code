import numpy as np

with open('input1.txt') as file:
    nums = np.loadtxt(file)

answer = np.sum(nums//3 - 2)
print(answer)
