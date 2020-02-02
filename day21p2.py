from intcode import Intcode
import csv

with open('input21.txt') as file:
    instructions = list(csv.reader(file))
instructions = [int(inst) for inst in instructions[0]]

droid = Intcode(instructions)

spring_program = ('NOT A J\n'
                  'NOT B T\n'
                  'OR T J\n'
                  'NOT C T\n'
                  'OR T J\n'
                  'AND D J\n'
                  'NOT E T\n'
                  'NOT T T\n'
                  'OR H T\n'
                  'AND T J\n'
                  'RUN\n')

commands = [ord(char) for char in spring_program]

results = droid.run(commands)
print(results)
print(''.join([chr(code) for code in results[1][:-1]]))
