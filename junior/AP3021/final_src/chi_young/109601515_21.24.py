import numpy as np
from scipy import integrate
# 還套件無法參考
x = [0, 2, 3, 4, 6, 8, 10]
p = [4.00, 3.95, 3.89, 3.80, 3.60, 3.41, 3.30]
A = [100, 103, 106, 110, 120, 133, 150]

y = []
for i in range(0, len(x)):
    y.append(float(A[i]) * float(p[i]) * 0.1)

y_1 = [y[0], y[1]]
y_2 = [y[1], y[2], y[3]]
y_3 = [y[3], y[4], y[5], y[6]]
m1 = np.trapz(y_1, dx=2)
m2 = integrate.simps(y_2,dx=1)
m3 = integrate.simps(y_3,dx=2)
m = m1 + m2 + m3
print('Mass of the rod =', m, 'kg')



