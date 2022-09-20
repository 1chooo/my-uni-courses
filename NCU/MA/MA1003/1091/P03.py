import pylab
a , b , n = -4 , 4 , 500

def g(t):
    glist = []
    for i in range(0,n):
        if t[i]%pylab.pi>0 and t[i]%pylab.pi<pylab.pi/2:
            glist.append(1)
        else:
            glist.append(-1)
    return glist
    
gxs = pylab.linspace(a,b,n)
gys = g(gxs)

pylab.plot(gxs,gys)
pylab.grid()
pylab.show()

def dg(s):
    dglist=[]
    h = (b-a)/(n-1)
    for j in range(0,n):
        if abs((g(s+h)[j]-g(s)[j])/h) < 100:
            dglist.append((g(s+h)[j]-g(s)[j])/h)
        else:
            dglist.append(0)
    return dglist

dgxs = pylab.linspace(a,b,n)
dgys = dg(dgxs)

pylab.plot(dgxs,dgys)
pylab.show()

def h(u):
    return 1.2732*pylab.sin(2*u)+0.4244*pylab.sin(6*u)+0.25465*pylab.sin(10*u)+0.18189*pylab.sin(14*u)+0.14147*pylab.sin(18*u)
hxs = pylab.linspace(a,b,n)
hys = h(hxs)
pylab.plot(hxs,hys)
pylab.show()

def dh(v):
    p = (b-a)/(n-1)
    return (h(v+p)-h(v))/p
    
dhxs = pylab.linspace(a,b,n)
dhys = dh(dhxs)
pylab.plot(dhxs,dhys)
pylab.show()