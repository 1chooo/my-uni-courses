from os.path import dirname, join as pjoin
import scipy.io as sio
import matplotlib.pyplot as plt
import numpy as np

#讀資料
mat_contents = sio.loadmat(r"cceqs.mat")
sorted(mat_contents.keys())
#print(mat_contents)
Tc = mat_contents['Tc'][0]
e = mat_contents['e'][0]

#確認資料
#plt.plot(Tc,e)
plt.scatter(Tc,e)
plt.title("Vapor Pressure vs Temperature")
plt.ylabel("Vapor Pressure (Pa)")
plt.xlabel("Temperature (degree Celsius)")
plt.show()

def sig_xn(inf, power, dat):
    sig = 0
    for i in range(0, dat):
        sig = sig + inf[i]**power
    return sig
#回傳回歸直線係數的矩陣
def a(x, y, dat):
    sig_y = 0
    sig_yy = 0
    sig_xy = 0
    sig_xxy = 0
    for i in range(0, dat):
        sig_y = sig_y + y[i]
        sig_yy = sig_yy + y[i]**2
        sig_xy = sig_xy + x[i] * y[i]
        sig_xxy = sig_xxy + x[i]*x[i]*y[i]
    linear_A = np.array([[dat, sig_xn(x, 1, dat)],
                         [sig_xn(x, 1, dat), sig_xn(x, 2, dat)]])
    linear_B = np.array([[sig_y],
                         [sig_xy]])

    l = np.array([[linear_A[0, 0],linear_A[0, 1]],
                  [linear_A[1, 0]-linear_A[0, 0]*(linear_A[1, 0]/linear_A[0, 0]),linear_A[1, 1]-linear_A[0, 1]*(linear_A[1, 0]/linear_A[0, 0])]])
    
    a1 = (linear_B[1, 0]-(linear_B[0, 0]*(linear_A[1, 0]/linear_A[0, 0]))) / l[1, 1]  
    a0 = (linear_B[0, 0] - l[0, 1]*a1) / l[0, 0]
    arr_a = np.array([[a0],
                      [a1]])
    return arr_a
#a_0 a_1 為回歸直線的2係數
def a_0(x, y, dat):
    arr_l = a(x, y, dat)
    return float(arr_l[0, 0])
def a_1(x, y, dat):
    arr_l = a(x, y, dat)
    return float(arr_l[1, 0])

def linear(x):
    a0_3 = a_0(Tc, e, len(Tc))
    a1_3 = a_1(Tc, e, len(Tc))
    return a0_3 + a1_3 * x

xs = np.arange(-30, 35, 0.1)
plt.title('3.(a) Vapor Pressure vs Temperature(Linear)')
plt.xlabel('Temperature (degree Celsius)')
plt.ylabel('Vapor Pressure (Pa)')
plt.plot(Tc, e, 'o', label = 'data')
plt.plot(xs, linear(xs), label = "Regression Line\n(y=" + str(a_0(Tc, e, len(Tc))) + "+" + str(a_1(Tc, e, len(Tc))) + "*x)")
plt.grid(True)
plt.legend()
plt.show()

e_ln = np.log(e)    #轉為ln

def expolin(x):
    a0_3 = a_0(Tc, e_ln, len(Tc))
    a1_3 = a_1(Tc, e_ln, len(Tc))
    return np.exp(a0_3 + a1_3 * x)  #轉回e

plt.title('3.(b) Vapor Pressure vs Temperature(exp)')
plt.xlabel('Temperature (degree Celsius)')
plt.ylabel('Vapor Pressure (Pa)')
plt.plot(Tc, e, 'o', label = 'data')
plt.plot(xs, expolin(xs), label = "Regression Line\n(y=e**(" + str(a_0(Tc, e_ln, len(Tc))) + "+" + str(a_1(Tc, e_ln, len(Tc))) + "*x))")
plt.grid(True)
plt.legend()
plt.show()
