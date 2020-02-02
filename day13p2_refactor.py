from intcode import Intcode
import csv

with open('input13.txt') as file:
    instructions = list(csv.reader(file))
instructions = [int(inst) for inst in instructions[0]]

instructions[0] = 2

arcade_builder = Intcode(instructions)
movement = []
still_on = True
score = 0

while still_on:
    results = arcade_builder.run(movement)
    still_on = results[0]
    outputs = results[1]

    for i in range(0, len(results[1]), 3):
        if outputs[i+2] == 3:
            paddle_pos = outputs[i]
        elif outputs[i+2] == 4:
            ball_pos = outputs[i]
        if (outputs[i], outputs[i+1]) == (-1, 0):
            score = outputs[i+2]
    if paddle_pos > ball_pos:
        movement = [-1]
    elif paddle_pos < ball_pos:
        movement = [1]
    else:
        movement = [0]

print(score)
