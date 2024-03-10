# %% [markdown]
# # [2021 Fall] Final Exam - Question 2
# 
# > Course: AP3021

# %%
from scipy import integrate
from scipy.special import erf
import numpy as np

# %%
def q(z):
    qz = -6.01 * (z**8) + 4.92 * (z**7) - 0.024 * (z**4) + 0.13 * (z**3) - 0.37 * (z**2) - 1.88 * z + 20.00
    return qz

# %%
Pw = 1000 * 1000 * 1000 * 1000
g = 9.8 * 0.001
para = 1 / (Pw * g)

x = np.array([
    0.,1.,2.,
    3., 4., 5., 
    6., 7., 8., 
    9., 10.]
)
# x = np.array([0.,1000.,2000.,3000., 4000., 5000., 6000., 7000., 8000., 9000., 10000.])
fx = q(x)
trap = np.trapz(fx, dx=1)
simp = integrate.simps(fx,dx=1)
romb = integrate.romberg(q, 0, 10)
quad = float((integrate.quadrature(q, 0.0, 10.0))[0])

# %% [markdown]
# (a)

# %%
print('Trapezoid:', para * trap, '\nSimpson 1/3:', para * simp, '\nRomberg:', para * romb)

# %% [markdown]
# (b)

# %%
print('Gauss-quadrature:', para * quad)

# %%



