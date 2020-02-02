from intcode import Intcode
import csv

with open('input13.txt') as file:
    instructions = list(csv.reader(file))
instructions = [int(inst) for inst in instructions[0]]

arcade = dict()

arcade_builder = Intcode(instructions)
results = arcade_builder.run([])
print(results)
outputs = results[1]

for i in range(0, len(results[1]), 3):
    arcade[(outputs[i], outputs[i+1])] = outputs[i+2]

print(sum([1 for x in arcade.values() if x == 2]))
