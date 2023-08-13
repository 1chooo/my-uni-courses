# -*- coding: utf-8 -*-

from vpython import *
import numpy as np

def calculate_magnetic_field_at_position(wire, B_pos):
    mu = 4 * pi * 1E-7
    B, n = vec(0, 0, 0), 600
    start = wire.pos.y
    stop = wire.pos.y + wire.axis.y
    step = mag(wire.axis) / n

    for y in np.arange(start, stop, step):
        source = vec(0, y, 0)
        dl = vec(0, step, 0)
        B += mu * wire.I / (4 * pi) * cross(dl, (B_pos - source)) / (mag(B_pos - source)) ** 3

    return B

scene = canvas(width=1000, height=600)
scene.camera.axis = vec(0, -2, -2)

# Create the wire and current arrow
I = 10
wire = cylinder(pos=vec(0, -150, 0), axis=vec(0, 300, 0), radius=0.2, opacity=0.8, I=I)
current = arrow(pos=vec(0, -6, 0), axis=vec(0, 1, 0), color=color.green)

# Calculate and visualize magnetic fields
arrow_length = 0.5
m = 0
for z in np.arange(-2, 4, 2):
    for r in np.arange(1, 5, 0.5):
        for theta in np.arange(0, -2 * pi, -pi / 12):
            B_pos = vec(r * cos(theta), z, r * sin(theta))
            B = calculate_magnetic_field_at_position(wire, B_pos)

            if m <= 601:
                dlxr = mag(cross(vec(0, wire.axis.y / 600, 0), (B_pos - vec(0, start, 0))))
                r = mag(B_pos - vec(0, start, 0))
                dB = mag(B)
                print(m, 'I=', I, 'dlxr=', dlxr, 'r=', r, 'dB=', dB)
                m += 1

            if z == 0 and r == 1.5 and theta == -pi / 6:
                print(m, 'source=', vec(0, stop, 0), 'B-field=', mag(B))

            source = vec(0, stop, 0)
            arrow(pos=source, length=step, color=color.red)
            arrow(pos=B_pos, axis=hat(B), length=arrow_length, color=vec(0.5, 0, log(3E6 * mag(B))))
