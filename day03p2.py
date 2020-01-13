import csv
import numpy as np

with open('input3.txt') as file:
    wire_paths = list(csv.reader(file))

first_wire = wire_paths[0]
second_wire = wire_paths[1]

start = 15000
wire_pos = np.zeros((2, 2*start, 2*start))
wire_steps = np.zeros((2, 2*start, 2*start))

for i, wire in enumerate(wire_paths):
    curr_x = start
    curr_y = start
    steps = 1
    for instruction in wire:
        length = int(instruction[1:])
        if instruction.startswith('U'):
            end_y = curr_y + length
            wire_pos[i, curr_x, (curr_y+1):(end_y+1)] = 1
            wire_steps[i, curr_x, (curr_y + 1):(end_y + 1)] = np.arange(steps, steps+length)
            curr_y = end_y
        elif instruction.startswith('D'):
            end_y = curr_y - length
            wire_pos[i, curr_x, (curr_y-1):(end_y-1):-1] = 1
            wire_steps[i, curr_x, (curr_y - 1):(end_y - 1):-1] = np.arange(steps, steps+length)
            curr_y = end_y
        elif instruction.startswith('L'):
            end_x = curr_x - length
            wire_pos[i, (curr_x-1):(end_x-1):-1, curr_y] = 1
            wire_steps[i, (curr_x-1):(end_x-1):-1, curr_y] = np.arange(steps, steps + length)
            curr_x = end_x
        elif instruction.startswith('R'):
            end_x = curr_x + length
            wire_pos[i, (curr_x+1):(end_x+1), curr_y] = 1
            wire_steps[i, (curr_x + 1):(end_x + 1), curr_y] = np.arange(steps, steps + length)
            curr_x = end_x
        steps = steps + length
        # print(curr_x, curr_y)

idxs = np.where(np.logical_and(wire_pos[0], wire_pos[1]))
dists = wire_steps[0][idxs] + wire_steps[1][idxs]
print(np.amin(dists))
