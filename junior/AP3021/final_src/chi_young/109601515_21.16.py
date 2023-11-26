def f(x):
    return float(0.2 + 25 * x - 200 * (x ** 2) + 675 * (x **3) - 900 * (x ** 4) + 400 * (x ** 5))
#多重區間
n = int(input("Input n:"))
h = float(0.8 / n)

tra_sum = f(0)
for i in range(1, n):
    tra_sum = tra_sum + 2 * f(i*h)

tra_sum = tra_sum + f(0.8)
trap = h * tra_sum / 2
print('Ans = ' + str(trap))
