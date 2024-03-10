# -*- coding: utf-8 -*-

from vpython import *
import numpy as np

mu = 4 * pi * 1E-7
arrow_length = .5
dt = 0.01
I  = 10

scene = canvas(width = 1000, height = 600)

scene.camera.axis = vec(0, -2, -2)
wire = cylinder(pos = vec(0, -150, 0), axis = vec(0, 300, 0), radius = .2, opacity = .8, I = I)

current = arrow(pos = vec(0, -6, 0), axis = vec(0, 1, 0), color = color.green)

m = 0
for z in np.arange(-2, 4, 2) :
    for r in np.arange(1, 5, .5) :
        for theta in np.arange(0, -2 * pi, -pi/12) :
            B_pos = vec(r * cos(theta), z, r * sin(theta))
            B, n = vec(0, 0, 0), 600
            start = wire.pos.y
            stop = wire.pos.y + wire.axis.y
            step = mag(wire.axis) / n

            for y in np.arange(start, stop, step) :
                source = vec(0, y, 0)
                dl = vec(0, step, 0)
                B += mu * wire.I/4/pi * cross(dl, (B_pos-source))/(mag(B_pos-source)) ** 3
                if m <= 601 :
                    print(m, 'I=',I, 'dlxr=', mag(cross(dl,(B_pos-source))), 'r=', mag(B_pos-source), 'dB=', mag(B))
                    m += 1
            if z == 0 and r == 1.5 and theta == -pi/6 :
                print(m, 'source=', source, 'B-field=', mag(B))

            arrow(pos = source, length = step, color = color.red)

            arrow(pos = B_pos, axis = hat(B), length = arrow_length, color = vec(0.5, 0, log(3E6 * mag(B))))
