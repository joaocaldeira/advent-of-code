from intcode import Intcode
import csv

with open('input17.txt') as file:
    instructions = list(csv.reader(file))
instructions = [int(inst) for inst in instructions[0]]

instructions[0] = 2
ascii_robot = Intcode(instructions)

commands = '''B,B,A,C,B,C,B,A,C,A
R,12,L,6,R,6,R,8,R,6
R,12,L,8,R,6
L,8,R,8,R,6,R,12
n
'''

inputs = [ord(char) for char in commands]
results = ascii_robot.run(inputs)

print(results[1][-1])
