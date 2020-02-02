import csv
from intcode import Intcode
from collections import defaultdict

with open('input11.txt') as file:
    instructions = list(csv.reader(file))
instructions = [int(inst) for inst in instructions[0]]

hull = defaultdict(lambda: 0)
painted_pixels = set()
robot = Intcode(instructions)
position = 0
direction = 1
robot_on = 1
while robot_on:
    painted_pixels.add(position)
    current_color = hull[position]
    robot_on, results = robot.run([current_color])
    hull[position] = results[0]
    direction *= (1 - 2 * results[1]) * 1j
    position += direction

print(len(painted_pixels))
