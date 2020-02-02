import numpy as np

positions = np.array([[17., -7., -11.], [1., 4., -1.],
                      [6., -2., -6.], [19., 11., 9.]])
# positions = np.array([[-1., 0., 2.], [2., -10., -7.],
#                       [4., -8., 8.], [3., 5., -1.]])
velocities = np.zeros((4, 3))

repeated = False
for i in range(1000):
    for j, moon in enumerate(positions):
        diff = np.sum(np.sign(positions - moon), axis=0)
        velocities[j] += diff
    positions += velocities

potential = np.sum(np.abs(positions), axis=1)
kinetic = np.sum(np.abs(velocities), axis=1)
energy = np.sum(potential*kinetic)
print(energy)
