# -*- coding: utf-8 -*-

from vpython import *
import numpy as np

'''
1 參數
'''
m, R = 1., 1.       # 重物質量、大小
k, L = 3., 10.      # 彈簧係數k、原長
g = vec(0, -9.8, 0) # 重力加速度
thick = 0.1         # 木版厚度
size = 3            # 木板邊長
b = 0.1
t = 0.
dt = 0.001
corrected_position = mag(m*g/k)
# 重物初始位置 -> 設定 amplitude
initial_pos = 3

initial_pos = vec(0, initial_pos, 0)
while(fabs(initial_pos.y) >= L):
    print('Warning')
    print('Because the amplitude should be less than the length of the spring, ')
    initial_pos.y = int(input('so please enter a number which is less than ' + str(L) + ' : '))
# 調整顯示的彈簧粗細，僅供美觀功能而已，可略過
spring_ratio = k
if(k >= 4 or k<= 0.1):
    if(k>=4):
        spring_ratio = 4
    elif(k <= 0.1):
        spring_ratio = 0.1

'''
2 物件
'''
#
scene = canvas(title='', width=400, height=400, background=vec(0., 0.65, 0.65))
#設定視窗的距離，若將其註解會自動找尋適當距離
scene.range = 20
#設定視窗視角方向
scene.forward = vector(-2, -2, -3) 

ceiling = box(pos=vec(0, L + R + thick/2 + corrected_position, 0), size = vec(size, thick, size), texture = textures.wood)

ball = sphere(radius = R, pos = initial_pos, color = color.red, make_trail = True)
ball.v = vec(0, 0, 0)

spring = helix(pos=vec(0, L + R + corrected_position, 0), radius = R/2, thickness = 0.025*spring_ratio*size, texture = textures.metal)

corrected_direction = (ball.pos - spring.pos)/mag(ball.pos - spring.pos)
spring.axis = ball.pos - spring.pos - R*corrected_direction
# 畫圖：設定
gd_1 = graph(title="y-t plot", width=600, height=600, x=0, y=400, xtitle="<i>time</i>(s)", ytitle="y position")
y_t = gcurve(graph=gd_1, color=color.blue)

'''
3 程式運行
'''
image, git = [], False
while True:
    t += dt
    rate(1000)
    corrected_direction =  (ball.pos - spring.pos)/mag(ball.pos - spring.pos)
    # 合力、加速度、速度、位置計算
    F = -k*(spring.axis - L*corrected_direction) + m*g - b*ball.v
    ball.a = F/m
    ball.v += ball.a*dt
    ball.pos += ball.v*dt
    # 更新彈簧位置
    spring.axis = ball.pos - spring.pos - R*corrected_direction
    # 畫圖
    y_t.plot(pos=(t, ball.pos.y))
    if(git == False):
        continue
    if(t%0.2 < dt):
        #print(t)
        im = ImageGrab.grab((100, 250, 750, 850))
        image.append(im)






