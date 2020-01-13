import csv
import itertools
from intcode import Intcode


with open('input7.txt') as file:
    instructions = list(csv.reader(file))
instructions = [int(inst) for inst in instructions[0]]

max_result = 0
for perm in itertools.permutations([5, 6, 7, 8, 9]):
    amps = [Intcode(instructions, [perm[i]]) for i in range(5)]
    current_amp = 0
    next_input = [0]
    while True:
        still_on, next_input = amps[current_amp].run(next_input)
        if not still_on and current_amp == 4:
            output = next_input[-1]
            break
        current_amp = (current_amp + 1) % 5

    if output > max_result:
        max_result = output

print(max_result)
