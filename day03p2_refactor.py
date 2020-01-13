import csv

with open('input3.txt') as file:
    wire_paths = list(csv.reader(file))

wire_pos = [dict(), dict()]

for i, wire in enumerate(wire_paths):
    curr_x = 0
    curr_y = 0
    wire_length = 0
    for instruction in wire:
        steps = int(instruction[1:])
        if instruction.startswith('U'):
            positions = {(curr_x, curr_y + j): wire_length + j for j in range(1, steps + 1)}
            curr_y += steps
        elif instruction.startswith('D'):
            positions = {(curr_x, curr_y - j): wire_length + j for j in range(1, steps + 1)}
            curr_y -= steps
        elif instruction.startswith('L'):
            positions = {(curr_x - j, curr_y): wire_length + j for j in range(1, steps + 1)}
            curr_x -= steps
        elif instruction.startswith('R'):
            positions = {(curr_x + j, curr_y): wire_length + j for j in range(1, steps + 1)}
            curr_x += steps

        # cannot just update wire_pos[i] so distances are not overwritten
        for pos in positions:
            if pos not in wire_pos[i]:
                wire_pos[i][pos] = positions[pos]
        wire_length += steps
        # print(curr_x, curr_y)

sets_of_pos = [set(wire.keys()) for wire in wire_pos]
idxs = sets_of_pos[0].intersection(sets_of_pos[1])
dists = [wire_pos[0][i] + wire_pos[1][i] for i in idxs]
print(min(dists))
