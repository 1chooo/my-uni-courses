import numpy as np
#1/(1+x**2)
def f(x, a, b):
    return (1/(1+(((b+a)+(b-a)*x)/(2))**2)) * ((b-a)/2)

true = np.arctan(3) - np.arctan(-3)

#Gauss-legendre
def Leg(i, a, b):
    c_2 = [1.0, 1.0]
    c_3 = [0.5555556, 0.8888889, 0.5555556]
    c_4 = [0.3478548, 0.6521452, 0.6521452, 0.3478548]
    c_5 = [0.2369269, 0.4786287, 0.5688889, 0.4786287, 0.2369269]
    c_6 = [0.1713245, 0.3607616, 0.4679139, 0.4679139, 0.3607616, 0.1713245]
    x_2 = [-0.577350269, 0.577350269]
    x_3 = [-0.774596669, 0.0, 0.774596669]
    x_4 = [-0.861136312, -0.339981044, 0.339981044, 0.861136312]
    x_5 = [-0.906179846, -0.538469310, 0.0, 0.538469310, 0.906179846]
    x_6 = [-0.932469514, -0.661209386, -0.238619186, 0.238619186, 0.661209386, 0.932469514]
    if i == 2:
        sum_l = 0.0
        for j in range(0, i):
            sum_l = sum_l + float(c_2[j])*f(float(x_2[j]), a, b)
    elif i == 3:
        sum_l = 0.0
        for j in range(0, i):
            sum_l = sum_l + float(c_3[j])*f(float(x_3[j]), a, b)
    elif i == 4:
        sum_l = 0.0
        for j in range(0, i):
            sum_l = sum_l + float(c_4[j])*f(float(x_4[j]), a, b)
    elif i == 5:
        sum_l = 0.0
        for j in range(0, i):
            sum_l = sum_l + float(c_5[j])*f(float(x_5[j]), a, b)
    elif i == 6:
        sum_l = 0.0
        for j in range(0, i):
            sum_l = sum_l + float(c_6[j])*f(float(x_6[j]), a, b)

    return sum_l

def err(timerr):
    return abs((Leg(timerr, -3, 3) - true) / true) * 100

for times in range(2, 7):
    print(times, '-point Gauss Legendre :', Leg(times, -3, 3), 'error =', err(times), '%')
