from intcode import Intcode
import csv

with open('input19.txt') as file:
    instructions = list(csv.reader(file))
instructions = [int(inst) for inst in instructions[0]]

pulled = 0
for i in range(50):
    for j in range(50):
        ascii_robot = Intcode(instructions)
        results = ascii_robot.run([i, j])
        pulled += results[1][-1]

print(pulled)
