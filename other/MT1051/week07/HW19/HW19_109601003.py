# -*- coding: utf-8 -*-
"""
Date: 2023/10/30
HW: 19
Author: 林群賀
Student Number: 109601003
"""

LA = [18, 25, 33, 8, 12, 18, 46]
print("1. LA =", LA)

LA.append(57)
print("2. LA =", LA)

print("3. LA 裡 18 有幾個:", LA.count(18))

print("4. LA length =", len(LA))

LA.append(32)
LA.append(18)
LA.append(92)
print("5. LA =", LA)

print("6. 8 在 LA 裡的 index:", LA.index(8))

LA.insert(5, 55)
print("7. LA =", LA)

LA.remove(LA[9])
print("8. LA =", LA)

LA.remove(46)
print("9. LA =", LA)

LA.reverse()
print("10. LA =", LA)

LA.sort()
print("11. LA =", LA)

print("12. LA 中所有元素的總和:", sum(LA))
