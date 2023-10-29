# %%
import numpy

def f(x):
    return 7 ** numpy.cos(x) * numpy.sin(x)

def f_ig(x):
    return -(7 ** numpy.cos(x)) / numpy.log(7)

def simpson(a, b):
    return (b - a) / 6 * (f(a) + f(b) + 4 * f((a + b) / 2))

def result(s):
    global res, ans
    print(s, "%.9f" % res, "　誤差:", "%.9f" % abs(ans - res))

lower = 0.0
upper = numpy.pi / 2
n = 100
dx = (upper - lower) / n
xs = numpy.linspace(lower, upper, n + 1)
ans = f_ig(upper) - f_ig(lower)
print("數學積分　:", "%.9f" % ans)

# %%
print("\n迴圈求積　:")
res = 0.0
for i in range(n):
    res += f(xs[i]) * dx
result("矩形積分　:")
res = 0.0
for i in range(n):
    res += max(f(xs[i]), f(xs[i + 1])) * dx
result("上矩形積分:")
res = 0.0
for i in range(n):
    res += min(f(xs[i]), f(xs[i + 1])) * dx
result("下矩形積分:")
res = 0.0
for i in range(n):
    res += (f(xs[i]) + f(xs[i + 1])) * dx / 2
result("梯形積分　:")

# %%
print("\n公式求積　:")
res = f(xs[:n]).sum() * dx
result("矩形積分法:")
res = (f(xs[:n]) + f(xs[1:])).sum() * dx / 2
result("梯形積分法:")
res = simpson(xs[:n], xs[1:]).sum()
result("Simpson 　:")

# %%