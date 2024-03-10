# -*- coding: utf-8 -*-

from vpython import *
import numpy as np
from matplotlib import pylab as plt

""" parameter """

h, r, dt, v = 0.5, 0.3, 0.001, 500

""" canvas """

scene = canvas(title="Bubble Probability Experiment", background=vec(0, 0.6, 0.6))
scene.forward = vec(-7, -6, 0)

floor = box(pos=vec(0, 0, 0), size=vec(16, h, 20), texture=textures.metal)

""" objects """

mainBall = sphere(radius=r, color=color.red, pos=vec(0, h / 2 + r, -8))

stillBalls = [sphere(radius=r, color=color.green, pos=vec(-4.5 + 3 * i, h / 2 + r, 8)) for i in range(4)]

""" visualize the status. """

plt.ion()

fig = plt.figure()

ax1 = fig.add_subplot(1, 2, 1)
ax1.set_title('Distribution ratio')

ax2 = fig.add_subplot(1, 2, 2)
ax2.set_title("hit status")

# Initialize data
b = []

ax1.hist(b, bins=np.arange(0, 12, 1), color=(0, 0, 1))
hist2 = ax2.hist([], bins=np.arange(1, 12, 1), color='#FF8800')

plt.pause(0.01)

""" exercise """

def reset_main_ball():
    mainBall.pos = vec((randint(-800, 800)) / 100, h / 2 + r, -8)
    return (randint(100, 200)) * np.pi / 300

theta = reset_main_ball()
T = 0
H = 0

while True:
    rate(500)
    mainBall.pos.z += v * np.sin(theta) * dt
    mainBall.pos.x += v * np.cos(theta) * dt

    hit = False
    for ball in stillBalls:
        if mag(mainBall.pos - ball.pos) < 2 * r:
            hit = True
            break

    if hit or mainBall.pos.z >= 8 or mainBall.pos.x >= 8 or mainBall.pos.x <= -8:
        ax2.set_title("hit status")
        theta = reset_main_ball()
        T += 1
        if hit:
            H += 1
            b.append(H)
        hist2[0], _ = np.histogram(b, bins=np.arange(1, 12, 1))
        plt.pause(0.001)

    if T == 10:
        print("Hit times:", H)
        ax1.hist(b, bins=np.arange(0, 12, 1), color=(0, 0, 1))
        T = 0
        H = 0
        plt.pause(0.001)
        plt.cla()
