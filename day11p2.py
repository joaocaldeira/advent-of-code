import csv
from intcode import Intcode
import numpy as np
import matplotlib.pyplot as plt

with open('input11.txt') as file:
    instructions = list(csv.reader(file))
instructions = [int(inst) for inst in instructions[0]]

size = 100
position = size//2 + 1j*(size//2)
hull_np = np.zeros((size, size))
hull_np[int(position.real), int(position.imag)] = 1
robot = Intcode(instructions)
direction = -1
robot_on = 1
while robot_on:
    current_color = hull_np[int(position.real), int(position.imag)]
    robot_on, results = robot.run([current_color])
    hull_np[int(position.real), int(position.imag)] = results[0]
    direction *= (1 - 2*results[1])*1j
    position += direction

plt.imshow(hull_np)
plt.show()
