from intcode import Intcode
import csv
import numpy as np

with open('input17.txt') as file:
    instructions = list(csv.reader(file))
instructions = [int(inst) for inst in instructions[0]]

ascii_robot = Intcode(instructions)

results = ascii_robot.run([])

# scaffold_map = ''.join([chr(code) for code in results[1]])

scaffold_map = np.array([chr(code) for code in results[1]][:-1])
length = np.where(scaffold_map == '\n')[0][0] + 1
width = len(scaffold_map)//length
scaffold_map = scaffold_map.reshape((width, length))

scaffold_pos = np.where(scaffold_map == '#')

result = 0
for x, y in zip(*scaffold_pos):
    try:
        if (scaffold_map[x+1, y] == '#' and scaffold_map[x, y+1] == '#' and scaffold_map[x-1, y] == '#' and
                scaffold_map[x, y-1] == '#'):
            result += x*y
    except IndexError:
        pass

print(result)
