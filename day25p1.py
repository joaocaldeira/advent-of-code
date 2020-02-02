from intcode import Intcode
import csv

with open('input25.txt') as file:
    instructions = list(csv.reader(file))
instructions = [int(inst) for inst in instructions[0]]

droid = Intcode(instructions)
next_input = []

while True:
    results = droid.run(next_input)
    print(''.join([chr(ascii_code) for ascii_code in results[1]]))

    next_input = input()

    if next_input == 'restart':
        droid = Intcode(instructions)
        next_input = []
    else:
        next_input = [ord(char) for char in next_input] + [10]
