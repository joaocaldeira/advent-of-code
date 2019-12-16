import csv
import numpy as np

with open('input16.txt') as file:
    fft_input = list(csv.reader(file))

offset = int(fft_input[0][0][:7])
fft_input = np.array(10000*[int(char) for char in fft_input[0][0]])
fft_input = fft_input[offset:]
# fft_input = np.array([int(char) for char in '12345678'])

steps = 100

for i in range(steps):
    cumsums = np.cumsum(fft_input)
    fft_input = cumsums[-1] - np.concatenate(([0], cumsums[:-1]))
    fft_input = np.abs(fft_input) % 10

print(fft_input[:8])
