import csv
from intcode import Intcode

with open('input9.txt') as file:
    instructions = list(csv.reader(file))
instructions = [int(inst) for inst in instructions[0]]

machine = Intcode(instructions)
results = machine.run([1])

print(results)