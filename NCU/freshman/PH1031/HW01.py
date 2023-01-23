# -*- coding: utf-8 -*-

from vpython import *
import numpy as np

#1 設定參數
m = 1               #設定重量
reach_floor = 0     #用來判斷是否到達地面
g = 9.8             #重力加速度 9.8 m/s^2
L, L2 = 4.9, 20     #板長度
size = 0.2          #球半徑 0.2m
th = 30 * pi / 180  #板斜度 30 度
dt = 0.001
uk=0.200            #動摩擦係數

#設定視窗
scene = canvas(title="1D Motion", width=900, height=600, x=0, y=0, center=vec(0, 0, 0), background=vec(240, 250, 250)/255)
scene.center = vector(L2/2,(L-2*size)*sin(th), 0) #設定視窗中心點
scene.forward = vector(-1, -0.5, -3) #設定視窗視角方向


#2 
#設定斜版
board = box(length=L, height=0.1, width=0.5+size*2, texture=textures.wood) #畫斜板
#board.pos = vector(-L*cos(th)/2 - size*sin(th) , L*sin(th)/2-size*cos(th), 0) #斜板的中心
board.pos = vector(-L*cos(th)/2 - size*sin(th) - board.height*sin(th)/2, L*sin(th)/2 - size*cos(th) - board.height*cos(th)/2, 0) #斜板的中心
#board.axis=vector((L)*cos(th), -L*sin(th),0) #斜板的方向
board.axis=vector(-(L)*cos(th), L*sin(th),0) #斜板的方向
board.color = vec(193, 192, 192)/255
#設定地板
floor = box(length=L2, height=0.1, width=0.5+size*2, texture=textures.wood) #畫地板
floor.pos = vector(L2/2-size , -floor.height/2-size, 0) #地板的中心
floor.axis=vector(L2+2*size, 0, 0) #地板方向
floor.color = vec(193, 192, 192)/255
#設定球
ball = sphere(radius = size, color = vector(255, 100, 100)/255) #球
ball.pos = vector(-L*cos(th), L*sin(th), 0) #球初始位置
ball.v = vector(0.0, 0.0, 0.0) #球初速

#3 畫出x-t圖, v-t圖, 動能位能圖
gr1 = graph(title="x-t plot", width=400, height=300, x=0, y=400, xtitle="t(s)", ytitle="x(m)")
gr2 = graph(title="v-t plot", width=400, height=300, x=0, y=400, xtitle="t(s)", ytitle="v(m)")
gr3 = graph(title="energy plot", width=400, height=300, x=0, y=400, xtitle="t(s)", ytitle="blue: Ek, Green: U, Red: Mechanical Energy")
xt = gcurve(graph=gr1, color=vec(0, 0, 0))
vt = gcurve(graph=gr2, color=vec(0, 0, 0))
Ek_t = gcurve(graph=gr3, color=vec(0, 0, 1))
U_t  = gcurve(graph=gr3, color=vec(0, 1, 0))
ME_t = gcurve(graph=gr3, color=vec(1, 0, 0))

#4 程式運行代碼
t, n_round = 0, 0
while True:
    t, n_round = 0, n_round + 1
    ball.pos = vector(-L*cos(th), L*sin(th), 0) #球初始位置
    ball.v = vector(0.0, 0.0, 0.0) #球初速
    reach_floor = 0
    while ball.pos.x < L2:
        rate(1000)
        t = t+dt #時間每次增加量
        if ball.pos.x < 0.0 :
            a = vector(g * sin(th) * cos(th), - g * sin (th) * sin(th), 0) #加速度
            ball.v += a * dt
            ball.pos += ball.v * dt
            
        if ball.pos.x > 0.0 :
            
            ball.v = vector(mag(ball.v), 0, 0)
            reach_floor = 1
            a2 = vector(uk*m*g, 0, 0)
            ball.v -= a2 * dt
            ball.pos += ball.v * dt
            #print (fk*dt, mag(ball.v))
        
        if ( mag(ball.v) < 0.01 and reach_floor == 1 ):
            break
        
        if n_round == 1:
            Ek = 0.5*m*np.square(mag(ball.v))
            U  = m*g*ball.pos.y
            ME = Ek + U
            xt.plot(pos=(t, ball.pos.x))
            vt.plot(pos=(t, mag(ball.v)))
            Ek_t.plot(pos=(t, Ek))
            U_t.plot(pos=(t, U))
            ME_t.plot(pos=(t, ME))
            
            
    print (n_round, 'times')
    
