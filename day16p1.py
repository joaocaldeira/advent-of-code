import csv
import numpy as np

with open('input16.txt') as file:
    fft_input = list(csv.reader(file))

fft_input = np.array([int(char) for char in fft_input[0][0]])
# fft_input = np.array([int(char) for char in '12345678'])

n = len(fft_input)
idxs = np.arange(n)
steps = 100

patterns = []
for j in range(n):
    pattern = np.zeros(n, dtype=int)
    pattern[np.logical_and(idxs % (4 * (j + 1)) >= j, idxs % (4 * (j + 1)) <= 2 * j)] = 1
    pattern[np.logical_and(idxs % (4 * (j + 1)) >= 3 * j + 2, idxs % (4 * (j + 1)) <= 4 * j + 2)] = -1
    patterns.append(pattern)
patterns = np.array(patterns)

for i in range(steps):
    fft_input = np.dot(patterns, fft_input)
    fft_input = np.abs(fft_input) % 10

print(fft_input[:8])
