# -*- coding: utf-8 -*-
"""
Date: 2023/12/11
HW: 38
Author: 林群賀
Student Number: 109601003
"""

# import matplotlib.pyplot as plt

# time = [2021, 2022, 2023, 2024, 2025]
# mercedes = [3367, 4120, 5539, 4328, 6213]
# bmw = [4000, 3590, 4423, 3528, 2987]
# lexus = [5200, 4930, 5350, 6721, 5230]

# plt.plot(time, mercedes, lw=3)
# plt.plot(time, bmw, lw=3)
# plt.plot(time, lexus, lw=3)

# plt.tick_params(axis='both', labelsize=14, color='red')
# plt.title("Car Sales", fontsize=14)
# plt.xlabel("year", fontsize=10)
# plt.ylabel("amount", fontsize=10)
# plt.grid(True)
# plt.legend(['Mercedes', 'BMW', 'Lexus'], loc='upper left')

# plt.show()


# import matplotlib.pyplot as plt
# import numpy as np

# x = [i for i in range(10)]
# y = [(3 * i - 18) for i in x]

# plt.plot(x, y, "-*")
# plt.grid(True)

# plt.show()

import matplotlib.pyplot as plt
import numpy as np

x = [i for i in range(-3, 10)]
y = [(i ** 2 - 6 * i + 10) for i in x]

plt.plot(x, y, "-*")
plt.grid(True)

plt.show()
