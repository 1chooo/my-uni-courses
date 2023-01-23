import pylab

pi = pylab.pi
#[a,b]分為100等分
a,b,n=0,pi/2,100
#定義函式
fn=lambda x:(sin(3*x)**2)*(cos(3*x))
#取等分點成xs,向量運算得ys
xs,h=pylab.linspace(a,b,n+1,retstep=True)
ys=(pylab.sin(3*xs)**2)*(pylab.cos(3*xs))
#rsum:矩形面積,lsum:下矩形面積,usum:上矩形面積,tsum:梯形面積
rsum,lsum,usum,tsum=0,0,0,0
y1=ys[0]
#迴圈計算:矩形,下矩形,上矩形,梯形
for y2 in ys[1:]:
    rsum+=y1
    if y1<y2:
        lsum+=y1
        usum+=y2
    else:
        lsum+=y2
        usum+=y1
    tsum+=y1+y2
    y1=y2
rsum*=h
lsum*=h
usum*=h
tsum*=h/2
isum=-1/9   #正確解
print('數學積分:',round(isum,9),end="\n\n")
print('迴圈求積:')
print("矩形積分:",round(rsum,9),"誤差:",round(abs(isum-rsum),10))
print("上矩形積分:",round(usum,9),"誤差:",round(abs(isum-usum),10))
print("下矩形積分:",round(lsum,9),"誤差:",round(abs(isum-lsum),10))
print("梯形積分法:",round(tsum,9),"誤差:",round(abs(isum-tsum),10))
#公式計算:矩形,梯形,Simpson
#矩形法係數:1,1,1,1,.....1,1
isum1=h*sum(ys[1:])    
#梯形法係數:1,2,2,2,..,1,2,1
isum2=h*sum([ys[0],2*sum(ys[1:-1]),ys[-1]])/2
#Simpson 1/3 rule 係數:1,4,2,4,2...,2,4,1
isum3=h*sum([ys[0],4*sum(ys[1:-1:2]),2*sum(ys[2:-1:2]),ys[-1]])/3
print("公式求積:")
print("矩形積分法:",round(isum1,9),"誤差:",round(abs(isum-isum1),10))
print("梯形積分法:",round(isum2,9),"誤差:",round(abs(isum-isum2),10))
print("Simpson積分:",round(isum3,9),"誤差:",round(abs(isum-isum3),10))