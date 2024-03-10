import numpy as np
import matplotlib.pyplot as plt

# 定義函數 f(x)
def f(x):
    return np.sqrt((2 * (np.sin(x) + np.cos(2 * x) + 3)) / (x + 1))

# 定義導數估算函數
def estimate_derivative(f, x, h=1e-6):
    return (f(x + h) - f(x)) / h

# 定義 x 範圍
x = np.linspace(1.0, 20, 100)

# 計算 f(x) 和其導數
y = f(x)
y_prime = [estimate_derivative(f, xi) for xi in x]

# 繪製 f(x) 和其導數
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='f(x) = sqrt((2 * (sin(x) + cos(2 * x) + 3)) / (x + 1))', color='blue', linewidth=2.0)
plt.plot(x, y_prime, label="f'(x) (Estimated)", color='green', linewidth=2.0)
plt.xlabel('x')
plt.ylabel('f(x) / f\'(x)')
plt.ylim(-1.0, 2.0)
plt.xlim(0, 20)
plt.legend()
plt.grid(True)
plt.title('f(x) = sqrt((2 * (sin(x) + cos(2 * x) + 3)) / (x + 1)) and computed derivative')
plt.show()
