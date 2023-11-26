# %% [markdown]
# # [2021 Fall] Final Exam
# 
# Date: 2022/01/12
# 
# 1. The given data is the temperature profile of the radiosonde.
#    1. Determine the vertical temperature gradient with the central difference method (10%)
#    2. Determine the determine the temperature at the level of $975hPa$ with the Newton finite difference methods. (10%)
#    3. Determine the determine the temperature at the level of $975hPa$ with the cubic spline method (10%)
#    4. Determine the depth of inversion with the Lagrange method (10%)
# 2. Please evaluate the total precipitable water (TPW) with the following formula.  
#    $$TPW=\frac{1}{\rho_wg}\int_{0}^{Z_T}q(z)dz$$  
#    , where $q(z)$ is the water vapor mixing ratio, $\rho_w$ is the water density $1000 (kg/m^3)$, g is the gravitational constant $9.8 (m/s^2)$ and $Z_T$ is the top of atmosphere. The vertical distribution of water vapor mixing ratio $(g/Kg)$ can be described as function of height $(km)$ $(Eq. (1))$.   
#    $$q(z) = −6.01z^8 + 4.92z^7 − 0.024z^4 + 0.13z^3 + − 0.37z^2 − 1.88z + 20.00 (1)$$  
#    1. Calculate TPW with the trapezoid, Simpson 1/3 and Romberg methods. (24%)  
#    Please use the data points from 0 to 10km with an interval of 1km.
#    2. Calculate TPW with the Gauss-quadrature method (16%)
# 3. Given pairs of temperature (°C) and saturation vapor pressure data (Pa), Please derive the Clausius–Clapeyron (C-C) equation.
#    1. Please construct the C-C equation using the **LINEAR** regression (25%)
#    2. Please determine the goodness of fitting (5%).
# 4. The given data is the ground-based Global Navigation Satellite System (GNSS) zenith total
# delay on 19 July 2019 with an interval of 30 min (at 15 and 45 minutes). Please apply FFT
# and find the diurnal component of this data set.

# %%



