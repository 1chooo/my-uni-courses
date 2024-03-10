#中插法
def D(l, y):
    ans = []
    h = float(l[1] - l[0])
    for i in range(0, len(l)):
        if i == 0:
            d = (float(y[i+1] - y[i])) / (h)
        elif i == len(x) - 1:
            d = (float(y[i] - y[i-1])) / (h)
        else:            
            d = (float(y[i+1] - y[i-1])) / (2*h)
        ans.append(d)
    return ans
t = [0, 25, 50, 75, 100, 125]
x = [0, 32, 58, 78, 92, 100]

v = D(t, x)
a = D(t, v)

for i in range(0, len(t)):
    print('When t =', t[i], 's, x =', x[i], 'km, v =', v[i], 'km/s, a =', a[i], 'km/s^2')
