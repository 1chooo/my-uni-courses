# -*- coding: utf-8 -*-

from vpython import *
from random import *
import numpy as np
from matplotlib import pylab as plt

""" parameter """

h, r, dt, v, T, H = 0.5, 0.3, 0.001, 50, 0, 0

""" canvas """

scene = canvas(title="109601003-林群賀-期末作業", background=vec(0, 0.6, 0.6))
scene.forward = vec(-7, -6, 0)

floor = box(pos=vec(0, 0, 0), size=vec(16, h, 20), texture=textures.metal)

""" objects """

b_ball = sphere(radius=r, color=color.red, pos=vec(0, h / 2 + r, -8))
b1_ball = sphere(radius=r, color=color.green, pos=vec(-4.5, h / 2 + r, 8))
b2_ball = sphere(radius=r, color=color.green, pos=vec(-1.5, h / 2 + r, 8))
b3_ball = sphere(radius=r, color=color.green, pos=vec(1.5, h / 2 + r, 8))
b4_ball = sphere(radius=r, color=color.green, pos=vec(4.5, h / 2 + r, 8))

# visualize

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
b = []
c = [0, 2]
d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

plt.ion()

fig = plt.figure()

ax1 = fig.add_subplot(1, 2, 1)
ax1.set_title('1')

ax2 = fig.add_subplot(1, 2, 2)
ax2.set_title("interactive test")

ax1.hist(b, bins=a, color=(0, 0, 1))
ax2.hist(c, bins=d, color='#FF8800')
plt.pause(0.01)

""" exercise """


b_ball.pos.x = (randint(-800, 800)) / 100
theta = (randint(100, 200)) * np.pi / 300

while True:

    rate(500)
    b_ball.pos.z += v * np.sin(theta) * dt
    b_ball.pos.x += v * np.cos(theta) * dt

    if mag(b_ball.pos - b1_ball.pos) < 2 * r or mag(b_ball.pos - b2_ball.pos) < 2 * r or mag(
            b_ball.pos - b3_ball.pos) < 2 * r or mag(b_ball.pos - b4_ball.pos) < 2 * r:

        b_ball.pos = vec((randint(-800, 800)) / 100, h / 2 + r, -8)
        theta = (randint(100, 200)) * np.pi / 300
        T += 1
        H += 1
        b.append(H)
        ax2.hist([T, T], bins=d, color='#0055FF')
        ax2.hist([T], bins=d, color=(1, 1, 1))
        plt.pause(0.001)


    elif b_ball.pos.z >= 8 or b_ball.pos.x >= 8 or b_ball.pos.x <= -8:

        b_ball.pos = vec((randint(-800, 800)) / 100, h / 2 + r, -8)
        theta = (randint(100, 200)) * np.pi / 300
        T += 1
        ax2.hist([T], bins=d, color='#FF8800')
        plt.pause(0.001)

    if T == 10:
        print(H)
        ax1.hist(b, bins=a, color=(0, 0, 1))
        T = 0
        H = 0
        plt.pause(0.001)
        plt.cla()