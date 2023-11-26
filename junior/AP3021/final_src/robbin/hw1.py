import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# ---------------------------------------


def relative_error(current_approx, previous_approx):
    return abs((current_approx - previous_approx) / current_approx) * 100


def factorial(n):
    f_sum = 1
    for i in range(1, n + 1):
        f_sum = f_sum * i
    return f_sum


def taylor_polynomial_of_cosine(x, a, order):
    y = 0
    for i in range(0, order + 1):
        if i % 4 == 0:
            y += ((np.cos(a) / factorial(i)) * ((x - a) ** i))
        elif i % 4 == 1:
            y += ((-np.sin(a) / factorial(i)) * ((x - a) ** i))
        elif i % 4 == 2:
            y += ((-np.cos(a) / factorial(i)) * ((x - a) ** i))
        elif i % 4 == 3:
            y += ((np.sin(a) / factorial(i)) * ((x - a) ** i))
    return y


def update(frame):
    y = taylor_polynomial_of_cosine(x, a, frame)
    taylor_polynomial.set_data(x, y)
    previous_y0_ploy = taylor_polynomial_of_cosine(x0, a, frame-1)
    y0_poly = taylor_polynomial_of_cosine(x0, a, frame)
    if frame >= 1:
        relative_error_text.set_text('relative_error=%f' % relative_error(y0_poly, previous_y0_ploy))
    view_point_poly.set_data(x0, y0_poly)
    order_text.set_text('order= ' + str(frame))
    if (relative_error(y0_poly, previous_y0_ploy) <= tolerance) and (y0_poly != previous_y0_ploy):
        ani.event_source.stop()

    return taylor_polynomial,


# ---------------------------------------

a = float(input("What point you want to generate the taylor polynomial?\n"))
significant_figures = int(input("How many significant figures you want to get?\n"))
x0 = float(input("What point you want to see?\n"))
tolerance = 0.5 * (10 ** (2 - significant_figures))

# ---------------------------------------

fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
ax.grid(ls='--')
relative_error_text = ax.text(5, 2.8, '', fontsize=12)
tolerance_text = ax.text(5, 2.3, 'tolerance= ' + str(tolerance), fontsize=12)
order_text = ax.text(5, 3.2, '', fontsize=12)
plt.xlim([-20, 20])
plt.ylim([-5, 5])

# ---------------------------------------

xReference = np.linspace(-20, 20, 1000)
yReference = np.cos(xReference)

x = np.linspace(-20, 20, 1000)
y = taylor_polynomial_of_cosine(x, a, 0)

y0_reference = np.cos(x0)

# ---------------------------------------

reference_function = ax.plot(xReference, yReference)
taylor_polynomial, = ax.plot(x, y)
view_point_reference = ax.plot(x0, y0_reference, color='red', marker='o', markersize=6, markeredgecolor='black', linestyle='')
view_point_poly, = ax.plot([], [], color='aqua', marker='o', markersize=4, markeredgecolor='black', linestyle='')

ani = animation.FuncAnimation(fig=fig, func=update, frames=[i for i in range(0, 41)], interval=300)

# ---------------------------------------

ani.save('taylo.mp4')
plt.show()
