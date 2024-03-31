"""
Date: 2023/10/23
HW: 16
Author: 林群賀
Student Number: 109601003
"""

from sympy import symbols, Eq, solve

# 定义符号变量
P, Q = symbols('P Q')

# 定义供需方程
Qs = 43.3 + 1.25 * P
Qd = 96.3 - 2.13 * P

# 设置供需方程相等，求解P和Q
eq1 = Eq(Qs, Qd)

# 解方程
solution = solve((eq1, Qs - Q), (P, Q))

# 提取均衡价格和数量
equilibrium_price = solution[P]
equilibrium_quantity = solution[Q]

print(f"均衡价格 (P) = {equilibrium_price:.2f}")
print(f"均衡数量 (Q) = {equilibrium_quantity:.2f}")

