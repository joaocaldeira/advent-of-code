import csv
import numpy as np

with open('input24.txt') as file:
    image = list(csv.reader(file))

n_side = len(image)
bugs = np.zeros((n_side, n_side), dtype=int)
area = n_side*n_side

for i in range(n_side):
    for j in range(n_side):
        if image[i][0][j] == '#':
            bugs[i, j] = 1

bio_converter = np.array([[2**(n_side*i+j) for j in range(n_side)] for i in range(n_side)])
bio = np.sum(bio_converter*bugs)
visited_indices = set([bio])
done = False

while not done:
    bugs_sum = np.zeros(bugs.shape)

    bugs_sum += np.pad(bugs, ((0, 0), (1, 0)), mode='constant')[:, :-1]
    bugs_sum += np.pad(bugs, ((0, 0), (0, 1)), mode='constant')[:, 1:]
    bugs_sum += np.pad(bugs, ((1, 0), (0, 0)), mode='constant')[:-1, :]
    bugs_sum += np.pad(bugs, ((0, 1), (0, 0)), mode='constant')[1:, :]

    bugs = np.logical_or(np.logical_and(bugs_sum == 2, bugs == 0), bugs_sum == 1).astype(int)
    bio = np.sum(bio_converter * bugs)

    if bio in visited_indices:
        done = True
        print(bio)
    visited_indices.add(bio)
