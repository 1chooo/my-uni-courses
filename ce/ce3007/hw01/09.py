import matplotlib.pyplot as plt
import numpy as np

# Define a range of L/R values
L_over_R = np.linspace(0, 1, 100)

# Calculate the corresponding I values
I = L_over_R

# Calculate the total delay using the formula
D = (I * L_over_R + L_over_R) / (1 - I)

# Plot the total delay as a function of L/R
plt.plot(L_over_R, D, label='Total Delay')
plt.xlabel('L/R')
plt.ylabel('Total Delay')
plt.title('Total Delay vs. L/R')
plt.grid(True)
plt.legend()
plt.show()
