import csv
import numpy as np
from fractions import Fraction

with open('input10.txt') as file:
    image = list(csv.reader(file))

height = len(image)
width = len(image[0][0])

asteroid_field = np.zeros((height, width))

for i in range(height):
    for j in range(width):
        if image[i][0][j] == '#':
            asteroid_field[i, j] = 1

idx = np.transpose(np.where(asteroid_field == 1))

max_visible = 0
for address in idx:
    displacements = idx - address
    visible_asteroids = set()
    for displ in displacements:
        if np.all(displ == np.array([0, 0])):
            continue
        try:
            fr = Fraction(displ[0], displ[1])
        except ZeroDivisionError:
            sign = displ[0] > 0
            visible_asteroids.add(sign)
        if displ[0] != 0:
            sign = displ[0] > 0
        else:
            sign = displ[1] > 0
        visible_asteroids.add((fr.numerator, fr.denominator, sign))
    visible = len(visible_asteroids)
    if visible > max_visible:
        max_visible = visible

print(max_visible)