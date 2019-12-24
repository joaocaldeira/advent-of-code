import csv
import numpy as np

with open('input24.txt') as file:
    image = list(csv.reader(file))

n_side = len(image)
minutes = 200
bugs = np.zeros((2*minutes+1, n_side, n_side), dtype=int)
area = n_side*n_side
center = n_side//2

for i in range(n_side):
    for j in range(n_side):
        if image[i][0][j] == '#':
            bugs[minutes, i, j] = 1

for _ in range(minutes):
    bugs_sum = np.zeros(bugs.shape)

    bugs_sum += np.pad(bugs, ((0, 0), (0, 0), (1, 0)), mode='constant')[:, :, :-1]
    bugs_sum += np.pad(bugs, ((0, 0), (0, 0), (0, 1)), mode='constant')[:, :, 1:]
    bugs_sum += np.pad(bugs, ((0, 0), (1, 0), (0, 0)), mode='constant')[:, :-1, :]
    bugs_sum += np.pad(bugs, ((0, 0), (0, 1), (0, 0)), mode='constant')[:, 1:, :]

    bugs_sum[1:, center - 1, center] += np.sum(bugs[:-1, 0, :],  axis=1)
    bugs_sum[1:, center + 1, center] += np.sum(bugs[:-1, -1, :], axis=1)
    bugs_sum[1:, center, center - 1] += np.sum(bugs[:-1, :, 0],  axis=1)
    bugs_sum[1:, center, center + 1] += np.sum(bugs[:-1, :, -1], axis=1)

    bugs_sum[:-1, 0, :]  += np.repeat(bugs[1:, center - 1, center], n_side).reshape(2 * minutes, n_side)
    bugs_sum[:-1, -1, :] += np.repeat(bugs[1:, center + 1, center], n_side).reshape(2 * minutes, n_side)
    bugs_sum[:-1, :, 0]  += np.repeat(bugs[1:, center, center - 1], n_side).reshape(2 * minutes, n_side)
    bugs_sum[:-1, :, -1] += np.repeat(bugs[1:, center, center + 1], n_side).reshape(2 * minutes, n_side)

    bugs = np.logical_or(np.logical_and(bugs_sum == 2, bugs == 0), bugs_sum == 1).astype(int)
    bugs[:, center, center] = 0

print(np.sum(bugs))
