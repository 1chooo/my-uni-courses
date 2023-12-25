# -*- coding: utf-8 -*-
"""
Date: 2023/12/25
Question: 07
Author: 林群賀
Student Number: 109601003
"""

import matplotlib.pyplot as plt

weekdays = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

city_a = [20, 21, 26, 24, 22, 22, 21]
city_b = [50, 55, 41, 51, 52, 55, 54]
city_c = [12, 12, 14, 11, 5, 8, 8]

plt.figure(figsize=(8, 6))

plt.scatter(weekdays, city_a, label='City A')
plt.scatter(weekdays, city_b, label='City B')
plt.scatter(weekdays, city_c, label='City C')

plt.title('City\'s temperature change over next week')
plt.xlabel('Day')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)  # 旋转x轴刻度标签，以便更好地显示

plt.tight_layout()
plt.show()