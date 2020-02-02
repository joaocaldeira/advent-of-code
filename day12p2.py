import numpy as np


def compute_gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def compute_lcm(x, y):
    lcm = (x*y)//compute_gcd(x, y)
    return lcm


positions = np.array([[17., -7., -11.], [1., 4., -1.],
                           [6., -2., -6.], [19., 11., 9.]])
# positions = np.array([[-1., 0., 2.], [2., -10., -7.],
#                       [4., -8., 8.], [3., 5., -1.]])
# positions = np.array([[-8., -10., 0.], [5., 5., 10.],
#                            [2., -7., 3.], [9., -8., -3.]])
velocities = np.zeros((4, 3))

steps_to_repeat = [-1, -1, -1]

initial_state = [np.concatenate([positions[:, k], velocities[:, k]]) for k in range(3)]
repeated = [False, False, False]
steps = 0
while not all(repeated):
    steps += 1
    for j, moon in enumerate(positions):
        diff = np.sum(np.sign(positions - moon), axis=0)
        velocities[j] += diff
    positions += velocities
    for k in range(3):
        if repeated[k]:
            continue
        state = np.concatenate([positions[:, k], velocities[:, k]])
        if np.all(state == initial_state[k]):
            repeated[k] = True
            steps_to_repeat[k] = steps

print(steps_to_repeat)

x = compute_lcm(steps_to_repeat[0], steps_to_repeat[1])
y = compute_lcm(x, steps_to_repeat[2])
print(y)
