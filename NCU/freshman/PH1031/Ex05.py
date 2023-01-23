# -*- coding: utf-8 -*-

from vpython import *

def ratio(k):
    if(k > 5):
        return 5
    elif(k < 0.05):
        return 0.05
    else:
        return k
"""
1. 參數設定, 設定變數及初始值ㄋ
"""
g = vec(0, -9.8, 0) # 重力加速度
box_size = 2        # 設定箱子尺寸(邊長:m)
m1, m2 = 1, 1       # 設定左、右箱子質量(kg)
# L0:彈簧原長 R1:左箱子初始位置 R2:右箱子初始位置
L0, R1, R2 = 10, 2, 2
# k1,k2,k3 分別為 左中右 的 彈簧彈力係數
k1, k2, k3 = 1, 1, 1
# 兩側牆壁厚度
wall_thickness = 0.1
# 地板長高寬(也就是說分別對應 x、y、z 方向的長度)
s1, s2, s3 = 3*L0 + 2*box_size + 2*wall_thickness, 0.2, box_size*1.5
# 設定彈簧粗細：只是讓彈簧粗細看起來較真實而已，略過不看也沒關係
k1_ratio, k2_ratio, k3_ratio = ratio(k1), ratio(k2), ratio(k3)

a = 0
aa = 0

while(R1 <= -L0 or R2 >= L0):
    print('Warning')
    print('Because the amplitude should be less than the length of spring,')
    print('please make sure the R1 or R2 you set is less than L0' + '(' + str(L0) + ')')
    if(R1 <= -L0):
        R1 = int(input('set left amplitude again: : '))
    if(R2 >= L0):
        R2 = int(input('set right amplitude again: : '))

'''
2. 畫面、物件創建
'''
# 、地板、木塊、彈簧
#產生動畫視窗、設定視窗的距離、設定視窗視角方向
scene = canvas(title="Coupled Oscillator", width=800, height=500, background=vec(0, 0.6, 0.6))
scene.center, scene.range, scene.forward = vec(L0/2, 0, 0), L0*1.2, -vec(2, 1, 4)
# 設定地板、牆壁(1:左、2:右)、箱子(1:左、2:右)、彈簧(1:左、2:中、3:右)
floor = box(pos = vec(0, -(box_size+s2)/2, 0), size = vec(s1, s2, s3), texture = textures.metal)
wall1 = box(pos =-vec(L0*3/2+box_size+wall_thickness/2, -box_size/4, 0), size = vec(wall_thickness, s3, s3), texture = textures.metal)
wall2 = box(pos = vec(L0*3/2+box_size+wall_thickness/2,  box_size/4, 0), size = vec(wall_thickness, s3, s3), texture = textures.metal)

box1 = box(pos =-vec((L0+box_size)/2 - R1, 0, 0), size = vec(box_size, box_size, box_size), texture = textures.wood, v=vec(0, 0, 0))
box2 = box(pos = vec((L0+box_size)/2 + R2, 0, 0), size = vec(box_size, box_size, box_size), texture = textures.wood, v=vec(0, 0, 0))

spring1 = helix(pos =-vec(L0*3/2+box_size, 0, 0), radius=0.4*box_size, thickness=k1_ratio/20, texture = textures.metal)
spring2 = helix(pos =-vec(L0/2+R1, 0, 0), radius=0.4*box_size, thickness=k2_ratio/20, texture = textures.metal)
spring3 = helix(pos = vec(L0/2+box_size+R2, 0, 0), radius=0.4*box_size, thickness=k3_ratio/20, texture = textures.metal)

spring1.axis = box1.pos - spring1.pos - vec(box_size/2, 0, 0)
spring2.axis = box2.pos - spring2.pos - vec(box_size/2, 0, 0)
spring3.axis = vec(wall2.pos.x, 0, 0) - spring3.pos - vec(wall_thickness/2, 0, 0)

# 畫圖：設定
xt = graph(title="x-t plot", width=600, height=600, x=0, y=400, xtitle="<i>time</i>(s)", ytitle="x position(blue:left, red: right)")
box1_xt = gcurve(graph=xt, color=color.blue)
box2_xt = gcurve(graph=xt, color=color.red)
vt = graph(title="v-t plot", width=600, height=600, x=0, y=400, xtitle="<i>time</i>(s)", ytitle="velocity(blue:left, red: right)")
box1_vt = gcurve(graph=vt, color=color.blue)
box2_vt = gcurve(graph=vt, color=color.red)

while( (box2.pos.x - box1.pos.x) < 2*box_size):
    print('Warning')
    print('the distance between two boxs should larger than 2*box_side,')
    print('so please est R1 and R2 again to make sure it makess sense in real world')
    R1 = int(input('set left amplitude again: : '))
    R2 = int(input('set right amplitude again: : '))
    box1.pos =-vec((L0+box_size)/2 - R1, 0, 0)
    box2.pos = vec((L0+box_size)/2 + R2, 0, 0)

'''
3 程式運行
'''
t2 = 0
t, dt = 0, 0.001
T1 = 0
while(True):
    rate(1000)
    t += dt
    # 計算各個彈簧的力
    F1 = -k1*(box1.pos - spring1.pos - vec(box_size/2, 0, 0) - vec(L0, 0, 0))
    F2 = -k2*(box2.pos - spring2.pos - vec(box_size/2, 0, 0) - vec(L0, 0, 0))
    F3 = -k3*(vec(wall2.pos.x, 0, 0) - spring3.pos - vec(wall_thickness/2, 0, 0) - vec(L0, 0, 0))
    F_on_box1, F_on_box2 = F1 - F2, F2 - F3
    #print (box1.pos, spring1.pos)
    # 計算各個木塊的加速度、速度、位置
    box1.a, box2.a = F_on_box1/m1, F_on_box2/m2
    box1.v += box1.a*dt
    box2.v += box2.a*dt
    box1.pos += box1.v*dt
    box2.pos += box2.v*dt
    # 彈簧位置的移動
    spring2.pos, spring3.pos = box1.pos + vec(box_size/2, 0, 0), box2.pos + vec(box_size/2, 0, 0)
    spring1.axis = box1.pos - spring1.pos - vec(box_size/2, 0, 0)
    spring2.axis = box2.pos - spring2.pos - vec(box_size/2, 0, 0)
    spring3.axis = vec(wall2.pos.x, 0, 0) - spring3.pos - vec(wall_thickness/2, 0, 0)

    box1_xt.plot(pos = (t, box1.pos.x + (L0+box_size)/2))
    box2_xt.plot(pos = (t, box2.pos.x - (L0+box_size)/2))
    box1_vt.plot(pos = (t, box1.v.x))
    box2_vt.plot(pos = (t, box2.v.x))

    if box1.v.x * a < 0 and box1.v.x < 0 :
        #print(t)
        t1 = t2
        t2 = t
        T = t2 - t1
        print(T)
    a = box1.v.x

    if box1.v.x * aa < 0 and box1.v.x > 0 :
        pass
    aa = box1.v.x
