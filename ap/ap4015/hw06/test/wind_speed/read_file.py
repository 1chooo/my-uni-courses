import numpy as np

# Load wind speed data
diri = "./"
fili = "fanapid.dat"
fName = diri + fili

nlat = 252
mlon = 252
nlev = 10
ntim = 1
vars = 4
UNDEF = 1.e30

x = np.empty((ntim, vars, nlev, nlat, mlon), dtype='>f4')

with open(fName, "rb") as f:
    for nt in range(ntim):
        for v in range(vars):
            x[nt, v, :, :, :] = np.fromfile(f, dtype='>f4', count=nlev * nlat * mlon).reshape(nlev, nlat, mlon)

u = x[0, 0, :, :, :]
v = x[0, 1, :, :, :]
w = x[0, 2, :, :, :]
t = x[0, 3, :, :, :]

print(u)