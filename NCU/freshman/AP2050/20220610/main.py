import numpy as np
import matplotlib.pyplot as plt 

# install getmac: pip install getmac;
# include following lines to get mac address from your computer;
from getmac import get_mac_address as gma
print(gma())
# save mac address to a mac;
mac = gma()

# a simple example;
fig = plt.figure(figsize=(12, 9))
x = np.arange(36)
y = np.random.random((36))
plt.plot(x, y, color='blue',label='random number')
plt.legend(loc='best', fontsize=12)
plt.xlabel('109601005 '+mac) # add mac after your student id

fig.savefig('getmac.png', dpi=300)
plt.show()