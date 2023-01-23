# -*- coding: utf-8 -*-

from vpython import *

scene.exit = False

"""
 1. 參數設定, 設定變數及初始值ㄋ
"""
m = 0.1             # 木塊質量 4 kg
size = 1            # 木塊邊長 1 m
R = 5               # 振幅 5 m
k = 1               # 彈性常數 1 N/m
L0 = R + size       # 彈簧原長
i = 0               # 木塊回到初位置的次數
t = 0               # 時間
dt = 0.001          # 時間間隔
g = 9.8             # 重力加速度 (m/s^2)
uk = 0.2
# 記錄位置訊息，用來尋找最大值
vertex, tem_position = 0, 0
"""
 2. 畫面設定
"""
# 產生動畫視窗、地板、木塊、彈簧
scene = canvas(title="Simple Harmonic Motion", width=800, height=400, x=0, y=0, background=vec(0, 0.6, 0.6))
scene.range = 8 #設定視窗的距離，若將其註解會自動找尋適當距離
scene.forward = 2*vector(-2, -2, -3) #設定視窗視角方向
floor = box(pos=vec(0, -(size+0.1)/2, 0), size=vec(2*L0, 0.1, R), texture=textures.metal)
wall = box(pos=vec(-L0, 0, 0), size=vec(0.1, size, R), texture=textures.metal)
block = box(pos=vec(R+size/2, 0, 0), size=vec(size, size, size), texture=textures.wood, v=vec(1, 0, 0))
spring = helix(pos=vec(-L0, 0, 0), radius=0.3*size, thickness=0.05*size, color=color.yellow)
spring.axis = block.pos - spring.pos - vec(size/2, 0, 0)

"""
 3. 物體運動部分
"""

while(True):
    rate(1000)
# 計算彈簧長度、伸長量、回復力
    spring.axis = block.pos - spring.pos - vec(0.5*size, 0, 0)
    F = -k * (spring.axis - vec(L0, 0, 0))
    fk = -(uk)*m*g*block.v/mag(block.v)

# 計算木塊加速度, 更新速度、位置
    tem_position = vertex
    vertex = block.pos.x
    block.a = (F+fk)/m
    block.v += block.a*dt
    block.pos += block.v*dt
# 找出彈簧伸長量最大的時候
    if(vertex > block.pos.x and vertex > tem_position):
        print(t, vertex)
# 更新時間
    t += dt

