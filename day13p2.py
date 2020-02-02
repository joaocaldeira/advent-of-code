from intcode import Intcode
import csv

with open('input13.txt') as file:
    instructions = list(csv.reader(file))
instructions = [int(inst) for inst in instructions[0]]

instructions[0] = 2

arcade = dict()

arcade_builder = Intcode(instructions)
movement = []
num_blocks = 100

while num_blocks:
    results = arcade_builder.run(movement)

    outputs = results[1]

    for i in range(0, len(results[1]), 3):
        arcade[(outputs[i], outputs[i+1])] = outputs[i+2]
    num_blocks = sum([1 for x in arcade.values() if x == 2])
    paddle_pos = [key for key in arcade if arcade[key] == 3]
    ball_pos = [key for key in arcade if arcade[key] == 4]
    if paddle_pos[0][0] > ball_pos[0][0]:
        movement = [-1]
    elif paddle_pos[0][0] < ball_pos[0][0]:
        movement = [1]
    else:
        movement = [0]

print(arcade[(-1, 0)])
