# %% [markdown]
# # [2022 Fall] Final Exam - Example Code
# 
# This is the example code from TAs.

# %% [markdown]
# ### Romberg Intergration Example

# %%
from scipy import integrate
from scipy.special import erf
import numpy as np
gaussian = lambda x: ((2*x) + (3/x))**2
result = integrate.romberg(gaussian, 1, 2, show=True)

# %% [markdown]
# ### Trapeziodal Rule Example

# %%
x=np.array([0,1,2,3])
fx=(x**2)*(np.exp(x))
np.trapz(fx, dx=1)

# %% [markdown]
# ### Simpson Rule Example (composite simpson (1/3))

# %%
integrate.simps(fx,dx=1)

# %% [markdown]
# ### Gauss Quadrature Example

# %%
from scipy import integrate

f = lambda x: 1/(1+x**2)
integrate.quadrature(f, -3.0, 3.0)

# %% [markdown]
# ### Richardson Extropolation

# %%
import numpy as np

def f(x): 
    return np.cos(x)

def fp(x): 
    return np.sin(x)

fp(np.pi/4)

def phi(x,h): 
    return (f(x+h)-f(x-h))/(2*h)

# d = [phi(1,h) for h in [2**(-n) for n in range(5)]]
d = [phi(np.pi/4,h) for h in [np.pi/3,np.pi/6]]

# %%
d

# %%
N = len(d)
D = np.zeros((N,N))
D[:,0] = d
for m in range(1,N):
    for n in range(m,N):
        D[n,m] = (4**m*D[n,m-1]-D[n-1,m-1])/(4**m-1)

# %%
D


