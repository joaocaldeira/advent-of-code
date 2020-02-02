from intcode import Intcode
import csv
import numpy as np


def print_array(array):
    for row in array:
        print(''.join(row))


with open('input15.txt') as file:
    instructions = list(csv.reader(file))
instructions = [int(inst) for inst in instructions[0]]

droid = Intcode(instructions)

movement = {1: np.array([-1, 0]), 2: np.array([1, 0]), 3: np.array([0, -1]), 4: np.array([0, 1])}
key_to_input = {'w': 1, 's': 2, 'a': 3, 'd': 4}

size = 51
position = np.array([size//2, size//2])
section_map = np.full((size, size), '?')
section_map[tuple(position)] = 'D'

# move = input('Where should I go?')

for _ in range(500000):
    # direction = key_to_input[move]
    direction = np.random.randint(1, 5)
    new_info = droid.run([direction])[1][-1]
    new_position = position + movement[direction]

    if new_info == 0:
        section_map[tuple(new_position)] = '#'
    elif new_info == 1:
        section_map[tuple(new_position)] = 'D'
        if section_map[tuple(position)] == 'D':
            section_map[tuple(position)] = '.'
        elif section_map[tuple(position)] == '!':
            section_map[tuple(position)] = 'O'
        position = new_position
    elif new_info == 2:
        section_map[tuple(new_position)] = '!'
        section_map[tuple(position)] = '.'
        position = new_position
    # move = input('Where should I go?')

print_array(section_map)
