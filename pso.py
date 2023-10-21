import numpy as np
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

iterations = 1000
inertia = 1.0
correction_factor = 2.0
swarm_size = 27
swarm = np.zeros((swarm_size, 4, 3))
index = 0
for i in range(10, 31, 10):
    for j in range(60, 101, 20):
        for k in range(5, 16, 5):
            swarm[index, 0, 0] = i
            swarm[index, 0, 1] = j
            swarm[index, 0, 2] = k
            index += 1

swarm[:, 3, 0] = 200
swarm[:, 1, :] = 0
random.seed()

for iter in range(iterations):
    for i in range(swarm_size):
        for j in range(3):
            swarm[i, 0, j] += swarm[i, 1, j]

        l, s, t = swarm[i, 0, 0], swarm[i, 0, 1], swarm[i, 0, 2]

        wear = (7.23111 - 0.0958056 * l - 0.119831 * s + 0.415233 * t +
                0.003935 * l**2 + 0.00320625 * l * s + 0.00703333 * l * t +
                0.0005275 * s**2 + 0.00088 * s * t - 0.0140333 * t**2)

        if wear < swarm[i, 3, 0]:
            swarm[i, 2, :] = swarm[i, 0, :]
            swarm[i, 3, 0] = wear

    gbest_index = np.argmin(swarm[:, 3, 0])

    for i in range(swarm_size):
        for j in range(3):
            swarm[i, 1, j] = (random.random() * inertia * swarm[i, 1, j] +
                             correction_factor * random.random() * (swarm[i, 2, j] - swarm[i, 0, j]) +
                             correction_factor * random.random() * (swarm[gbest_index, 2, j] - swarm[i, 0, j]))
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
l, s, wear = swarm[:, 0, 0], swarm[:, 0, 1], swarm[:, 3, 0]
ax.scatter(l, s, wear, c='b', marker='o')
ax.set_xlabel('Load')
ax.set_ylabel('Speed')
ax.set_zlabel('Wear')
plt.show()
