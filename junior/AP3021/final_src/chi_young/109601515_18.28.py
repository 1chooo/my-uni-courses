import numpy as np
import Newton_interpolating as ni
T = [0, 8, 16, 24, 32, 40]
o = [14.621, 11.843, 9.870, 8.418, 7.305, 6.413]

print("find o(27)")
#----------Linear interpolation-------------------
def O(x):
    i = 0
    while True:
        if T[i] < x and T[i+1] > x:
            break
        else:
            i += 1

    return o[i] + ((o[i+1] - o[i]) / (T[i+1] - T[i])) * (x - T[i])

lin_ans = O(27.0)
print("Linear interpolation:" + str(lin_ans))
print("------------------------------------------------------------")
#----------Newton’s interpolating polynomial-------
def f1(x_g, site, x, y) :
    return y[site] + (x_g-x[site]) * ni.f_1(site+1, site, x, y)

def f2(x_g, site, x, y) :
    return y[site] + (x_g-x[site]) * ni.f_1(site+1, site, x, y) + (x_g-x[site]) * (x_g-x[site+1]) * ni.f_2(site+2, site+1, site, x, y)

def f3(x_g, site, x, y) :
    return y[site] + (x_g-x[site]) * ni.f_1(site+1, site, x, y) + (x_g-x[site]) * (x_g-x[site+1]) * ni.f_2(site+2, site+1, site, x, y) + (x_g-x[site]) * (x_g-x[site+1])* (x_g-x[site+2]) *ni.f_3(site+3, site+2, site+1, site, x, y)

def f4(x_g, site, x, y) :
    return y[site] + (x_g-x[site]) * ni.f_1(site+1, site, x, y) + (x_g-x[site]) * (x_g-x[site+1]) * ni.f_2(site+2, site+1, site, x, y) + (x_g-x[site]) * (x_g-x[site+1])* (x_g-x[site+2]) *ni.f_3(site+3, site+2, site+1, site, x, y) + (x_g-x[site]) * (x_g-x[site+1])* (x_g-x[site+2]) * (x_g-x[site+3]) * ni.f_4(site+4, site+3, site+2, site+1, site, x, y)

print("Newton’s interpolating polynomial:")
print("1 order = " + str(f1(27, 3, T, o)))
print("2 order = " + str(f2(27, 2, T, o)))
print("3 order = " + str(f3(27, 2, T, o)))
print("4 order = " + str(f4(27, 1, T, o)))
print("------------------------------------------------------------")
#----------Cubic spline---------------------------
arr_a = np.array([[2*(T[2]-T[0]), (T[2]-T[1]), 0, 0],
                  [(T[2]-T[1]), 2*(T[3]-T[1]), (T[3]-T[2]), 0],
                  [0, (T[3]-T[2]), 2*(T[4]-T[2]), (T[4]-T[3])],
                  [0, 0, (T[4]-T[3]), 2*(T[5]-T[3])]])
arr_c = np.array([[0.],
                 [0.],
                 [0.],
                 [0.]])
for i in range(0, 4):
    two = i+2
    one = i+1
    zer = i
    #print(float(((o[two]-o[one])/(T[two]-T[one])) + ((o[zer]-o[one])/(T[one]-T[zer])))*6)
    arr_c[i, 0] = float(((o[two]-o[one])/(T[two]-T[one])) + ((o[zer]-o[one])/(T[one]-T[zer])))*6.0

#print(arr_c)
d2f = np.linalg.inv(arr_a).dot(arr_c)
#print(d2f)

# i = 4
def f_i(x, i):
    c1 = d2f[i-2]/6/(T[i]-T[i-1])
    c2 = d2f[i-1]/6/(T[i]-T[i-1])
    c3 = (o[i-1]/(T[i]-T[i-1]))-d2f[i-2]*(T[i]-T[i-1])/6
    c4 = (o[i]/(T[i]-T[i-1]))-d2f[i-1]*(T[i]-T[i-1])/6
    t1 = c1 * (T[i] - x)**3
    t2 = c2 * (x - T[i-1])**3
    t3 = c3 * (T[i] - x)
    t4 = c4 * (x - T[i-1])
    return float(t1 + t2 + t3 + t4)
print("Cubic spline = " + str(f_i(27 ,4)))



