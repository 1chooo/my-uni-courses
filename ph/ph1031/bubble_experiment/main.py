# -*- coding: utf-8 -*-

from vpython import *
from random import *
import numpy as np
from matplotlib import pylab as plt

""" parameter """

h, r, dt, v, T, H = 0.5, 0.3, 0.001, 500, 0, 0

""" canvas """

scene = canvas(title="Bubble Probability Experiment", background=vec(0, 0.6, 0.6))
scene.forward = vec(-7, -6, 0)

floor = box(pos=vec(0, 0, 0), size=vec(16, h, 20), texture=textures.metal)

""" objects """

mainBall = sphere(radius=r, color=color.red, pos=vec(0, h / 2 + r, -8))

stillBall1 = sphere(radius=r, color=color.green, pos=vec(-4.5, h / 2 + r, 8))
stillBall2 = sphere(radius=r, color=color.green, pos=vec(-1.5, h / 2 + r, 8))
stillBall3 = sphere(radius=r, color=color.green, pos=vec(1.5, h / 2 + r, 8))
stillBall4 = sphere(radius=r, color=color.green, pos=vec(4.5, h / 2 + r, 8))

""" visualize the staus. """

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
b = []
c = [0, 2]
d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

plt.ion()

fig = plt.figure()

ax1 = fig.add_subplot(1, 2, 1)
ax1.set_title('Distribution ratio')

ax2 = fig.add_subplot(1, 2, 2)
ax2.set_title("hit status")

ax1.hist(b, bins=a, color=(0, 0, 1))
ax2.hist(c, bins=d, color='#FF8800')
plt.pause(0.01)

""" exercise """


mainBall.pos.x = (randint(-800, 800)) / 100
theta = (randint(100, 200)) * np.pi / 300

while True:

    rate(500)
    mainBall.pos.z += v * np.sin(theta) * dt
    mainBall.pos.x += v * np.cos(theta) * dt

    if mag(mainBall.pos - stillBall1.pos) < 2 * r or mag(mainBall.pos - stillBall2.pos) < 2 * r or mag(
            mainBall.pos - stillBall3.pos) < 2 * r or mag(mainBall.pos - stillBall4.pos) < 2 * r:

        ax2.set_title("hit status")
        mainBall.pos = vec((randint(-800, 800)) / 100, h / 2 + r, -8)
        theta = (randint(100, 200)) * np.pi / 300
        T += 1
        H += 1
        b.append(H)
        ax2.hist([T, T], bins=d, color='#0055FF')
        ax2.hist([T], bins=d, color=(1, 1, 1))
        plt.pause(0.001)


    elif mainBall.pos.z >= 8 or mainBall.pos.x >= 8 or mainBall.pos.x <= -8:

        ax2.set_title("hit status")
        mainBall.pos = vec((randint(-800, 800)) / 100, h / 2 + r, -8)
        theta = (randint(100, 200)) * np.pi / 300
        T += 1
        ax2.hist([T], bins=d, color='#FF8800')
        plt.pause(0.001)

    if T == 10:
        print("Hit times:", H)
        ax1.hist(b, bins=a, color=(0, 0, 1))
        T = 0
        H = 0
        plt.pause(0.001)
        plt.cla()