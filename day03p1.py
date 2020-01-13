import csv
import numpy as np

with open('input3.txt') as file:
    wire_paths = list(csv.reader(file))

first_wire = wire_paths[0]
second_wire = wire_paths[1]

start = 15000
wire_pos = np.zeros((2, 2*start, 2*start))

for i, wire in enumerate(wire_paths):
    curr_x = start
    curr_y = start
    for instruction in wire:
        if instruction.startswith('U'):
            end_y = curr_y + int(instruction[1:])
            wire_pos[i, curr_x, (curr_y+1):(end_y+1)] = 1
            curr_y = end_y
        elif instruction.startswith('D'):
            end_y = curr_y - int(instruction[1:])
            wire_pos[i, curr_x, (curr_y-1):(end_y-1):-1] = 1
            curr_y = end_y
        elif instruction.startswith('L'):
            end_x = curr_x - int(instruction[1:])
            wire_pos[i, (curr_x-1):(end_x-1):-1, curr_y] = 1
            curr_x = end_x
        elif instruction.startswith('R'):
            end_x = curr_x + int(instruction[1:])
            wire_pos[i, (curr_x+1):(end_x+1), curr_y] = 1
            curr_x = end_x
        # print(curr_x, curr_y)

idxs = np.where(np.logical_and(wire_pos[0], wire_pos[1]))
dists_x = np.abs(idxs[0] - start)
dists_y = np.abs(idxs[1] - start)
dists = dists_x + dists_y
print(np.amin(dists))
