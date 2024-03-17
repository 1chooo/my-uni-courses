a, b = eval(input("> "))

sum = 0
for i in range(a, b + 1) :
    sum += i

print(f"{a}+{a + 1}+...+{b}={sum}")

print(a, end = "")
print("+", end = "")
print(a + 1, end = "")
print("+...+", end = "")
print(b, end = "")
print("=", end = "")
print(sum)