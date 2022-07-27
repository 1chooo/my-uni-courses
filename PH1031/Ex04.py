# -*- coding: utf-8 -*-

from vpython import*

r = 1
h = 0.5
g = 9.8
g2 = 4.9

scene = canvas(title='free fall', width=500, height=500, center=vec(0,0,0), background=vec(0,0,0))

floor = box(pos=vec(0,0,0), length=10, height=h, width=10, color=color.blue)
ball  = sphere(pos=vec(0,4,0), radius=r, color=color.red)
ball.v = vec(0,-1,0)
ball2 = sphere(pos=vec(3,4,2), radius=r, color=color.green)
ball2.v = vec(0,-1,0)

t  = 0
dt = 0.001

while 1:
    rate (1000)
    ball.pos = ball.pos + ball.v*dt
    ball2.pos = ball2.pos + ball2.v*dt

    if ball2.pos.y < floor.pos.y+(r+h/2):
        ball2.v.y = fabs(ball2.v.y)
    else:
        ball2.v.y = ball2.v.y - g2*dt

    if ball.pos.y < floor.pos.y+(r+h/2):
        ball.v.y = fabs(ball.v.y)
    else:
        ball.v.y = ball.v.y - g*dt

    t += dt


