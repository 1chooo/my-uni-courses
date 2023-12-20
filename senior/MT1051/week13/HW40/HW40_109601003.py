# -*- coding: utf-8 -*-
"""
Date: 2023/12/18
HW: 40
Author: 林群賀
Student Number: 109601003
"""

import matplotlib.pyplot as plt
terms = [
    "19Q1",
    "19Q2",
    "19Q3",
    "19Q4",
    "20Q1",
    "20Q2",
]

people = [
    100,
    150,
    120,
    50,
    80,
    130,    
]

production = [
    1000,
    1400,
    1300,
    600,
    800,
    1500    
]

plt.figure(figsize=(8, 6))

plt.scatter(people, production, color='blue', marker='o')
plt.title('Scatter Plot of Number of People vs Production')
plt.xlabel('Number of People')
plt.ylabel('Production')

for i, term in enumerate(terms):
    plt.text(people[i], production[i], term, fontsize=9, ha='right', va='bottom')

plt.grid(True)
plt.tight_layout()

plt.show()
