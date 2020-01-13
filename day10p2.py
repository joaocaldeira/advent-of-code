import csv
import numpy as np

with open('input10.txt') as file:
    image = list(csv.reader(file))

length = len(image)
width = len(image[0][0])

asteroid_field = np.zeros((length, width))

for i in range(length):
    for j in range(width):
        if image[i][0][j] == '#':
            asteroid_field[i, j] = 1

idx = np.transpose(np.where(asteroid_field == 1))

max_visible = 0
for address in idx:
    displacements = idx - address
    visible_asteroids = dict()
    for displ in displacements:
        if np.all(displ == np.array([0, 0])):
            continue
        angle = np.arctan2(displ[0], displ[1])
        if angle < -np.pi/2:
            angle += 2*np.pi
        if angle in visible_asteroids:
            if np.linalg.norm(displ) < np.linalg.norm(visible_asteroids[angle]):
                visible_asteroids[angle] = displ
        else:
            visible_asteroids[angle] = displ
    visible = len(visible_asteroids)
    if visible > max_visible:
        max_visible = visible
        station = address
        asteroids_from_station = visible_asteroids

# using the fact that 200 < number of visible asteroids
ordinal = 200
angles = list(asteroids_from_station.keys())
angles.sort()
relative_position = asteroids_from_station[angles[ordinal - 1]]
print(100*(station[1] + relative_position[1]) + station[0] + relative_position[0])
