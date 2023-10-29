import pylab

lower = -pylab.pi
upper = pylab.pi
n = 1001
dx = (upper - lower) / (n - 1)

xs = [lower + i * dx for i in range(n)]
ys = [
    1.2732  * pylab.sin(2  * x) +
    0.4244  * pylab.sin(6  * x) +
    0.25465 * pylab.sin(10 * x) +
    0.18189 * pylab.sin(14 * x) +
    0.14147 * pylab.sin(18 * x) for x in xs]
pylab.plot(xs, ys, label = "h(t)", color = "blue")

ys = [
    1.2732  * pylab.cos(2  * x) * 2  +
    0.4244  * pylab.cos(6  * x) * 6  +
    0.25465 * pylab.cos(10 * x) * 10 +
    0.18189 * pylab.cos(14 * x) * 14 +
    0.14147 * pylab.cos(18 * x) * 18 for x in xs]
pylab.plot(xs, ys, label = "h\'(t)", color = "green")

pylab.title("sawtooth function approximation and derivative")
pylab.xlabel("t")
pylab.ylabel("y")
pylab.legend()
# pylab.xlim(lower, upper)
# pylab.ylim(-15, 15)
pylab.grid(axis='both')
pylab.show()