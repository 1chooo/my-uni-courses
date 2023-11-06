# while stmt
m = int(input('Input factorial: '))
r = n = 1

while n <= m:
    r *= n    # r = r * n
    n += 1    # n = n + 1

print(str(m) + '! =', r)
