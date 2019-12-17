import csv
import numpy as np

with open('input16.txt') as file:
    fft_input = list(csv.reader(file))

fft_input = np.array([int(char) for char in fft_input[0][0]])
# fft_input = np.array([int(char) for char in '12345678'])

n = len(fft_input)
idxs = np.arange(n)
steps = 100

patterns = np.zeros((n, n), dtype=int)
col, row = np.meshgrid(idxs, idxs)

patterns[np.logical_and(col % (4 * (row + 1)) >= row, col % (4 * (row + 1)) <= 2 * row)] = 1
patterns[np.logical_and(col % (4 * (row + 1)) >= 3 * row + 2, col % (4 * (row + 1)) <= 4 * row + 2)] = -1

for i in range(steps):
    fft_input = np.dot(patterns, fft_input)
    fft_input = np.abs(fft_input) % 10

print(fft_input[:8])
