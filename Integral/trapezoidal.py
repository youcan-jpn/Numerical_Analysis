import numpy as np

h = 0.01
m = 100 + 10000*h
x = np.arange(-m, m, h)
y = np.exp(-x**2)

I_val = np.sqrt(np.pi)
I_est = (np.sum(y) - (y[0] + y[-1]) / 2) * h

print(I_val)
print(I_est)
