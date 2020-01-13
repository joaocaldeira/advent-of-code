import csv
import numpy as np

with open('input3.txt') as file:
    wire_paths = list(csv.reader(file))

wire_pos = [set(), set()]

for i, wire in enumerate(wire_paths):
    curr_x = 0
    curr_y = 0
    for instruction in wire:
        steps = int(instruction[1:])
        if instruction.startswith('U'):
            positions = [(curr_x, curr_y + j) for j in range(1, steps+1)]
            curr_y += steps
        elif instruction.startswith('D'):
            positions = [(curr_x, curr_y - j) for j in range(1, steps+1)]
            curr_y -= steps
        elif instruction.startswith('L'):
            positions = [(curr_x - j, curr_y) for j in range(1, steps+1)]
            curr_x -= steps
        elif instruction.startswith('R'):
            positions = [(curr_x + j, curr_y) for j in range(1, steps + 1)]
            curr_x += steps
        wire_pos[i].update(positions)
        # print(curr_x, curr_y)

idxs = np.abs(np.array(list(wire_pos[0].intersection(wire_pos[1]))))
dists = idxs[:, 0] + idxs[:, 1]
print(np.amin(dists))
