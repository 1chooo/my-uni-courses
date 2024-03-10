# -*- coding: utf-8 -*-

from vpython import *
import pylab

scene.exit = False
'''
設定外力：F = A*sin(wt)
'''
def Fd(t, A = 3, w = 0.2*pi):
    return vec(A*sin(w*t), 0, 0)
"""
 1. 參數設定, 設定變數及初始值ㄋ
"""
m = 0.1               # 木塊質量(kg)
size = 1            # 木塊邊長(m)
R = 5               # 振幅(m)
k = 1               # 彈性常數 (N/m)
L0 = 2*(R + size)   # 彈簧原長 -> 如果軌道太短，可以調整乘上的倍數，用來加長軌道以及彈簧長度
t = 0               # 時間(s)
dt = 0.001          # 時間間隔
uk = 0.1             # 摩擦係數
g = 9.8             # 重力加速度 (m/s^2)
a = 0
aa = 0


"""
 2. 畫面設定
"""
# 產生動畫視窗、地板、木塊、彈簧
scene = canvas(title="Driven harmonic oscillators", width=800, height=400, x=0, y=0, background=vec(0, 0.6, 0.6))
scene.range = 8 #設定視窗的距離，若將其註解會自動找尋適當距離
scene.forward = 2*vector(-2, -2, -3) #設定視窗視角方向

floor = box(pos=vec(0, -(size+0.1)/2, 0), size=vec(2*L0, 0.1, R), texture=textures.metal)
wall = box(pos=vec(-L0, 0, 0), size=vec(0.1, size, R), texture=textures.metal)
block = box(pos=vec(R+size/2, 0, 0), size=vec(size, size, size), texture=textures.wood, v=vec(0, 0, 0))
spring = helix(pos=vec(-L0, 0, 0), radius=0.3*size, thickness=0.05*size, color=color.yellow)
spring.axis = block.pos - spring.pos - vec(size/2, 0, 0)

arrow_F = arrow(pos=block.pos, axis=vec(0, 0, 0), shaftwidth = 0.25*size, headwidth = 0.5*size, color=color.red)

"""
 3. 物體運動部分
"""

while(True):
    rate(1000)
# 計算彈簧長度、伸長量、回復力
    spring.axis = block.pos - spring.pos - vec(0.5*size, 0, 0)
    Fs = -k * (spring.axis - vec(L0, 0, 0))
# 計算摩擦力
    fk = -(uk)*block.v
# 計算木塊加速度, 更新速度、位置
    F = Fs + fk + Fd(t, w = 4.68645)
    block.a = F/m
    block.v += block.a * dt
    block.pos = block.v * dt

    if block.v.x * a < 0 and block.v.x < 0:

        print(t, block.pos)
    a = block.v.x

    if block.v.x * aa < 0 and block.v.x > 0:

        print(t, block.pos)

    aa = block.v.x


# 設定想要可視化的力：F、Fs、Fd(t)、fk -> 合力、彈簧回復力、外力、阻力
    F_show = Fs
    arrow_F.pos = block.pos - (size/2+0.4)*F_show/mag(F_show) - F_show if(mag(F_show) != 0) else block.pos
    #arrow_F.pos = block.pos - (size/2+0.4)*norm(F_show) - F_show

    arrow_F.axis = F_show

# 超出地板或撞到牆壁則停止運行
    if(block.pos.x < (wall.pos.x + wall.size.x/2) or block.pos.x > (floor.pos.x + floor.size.x/2)):
        print('Hint')
        print('Error: The box hits the wall, or out of the floor')
        print('Error: Please input the other A(amplitute) or w(omega) to try again')
        print()
        break
# 更新時間
    t += dt

