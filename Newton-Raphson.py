import matplotlib.pyplot as plt
import numpy as np


def f(a, x):
    return x*(2-a*x)


ini_val = 0.001
a = 5
itr = 30
xs = [ini_val]

fig1, ax = plt.subplots()
x = np.linspace(-1, 1, 100)
y = f(a, x)
ax.plot(x, y)
ax.set_ylabel('$f(x)$')
ax.set_xlabel('$x$')

for i in range(itr):
    x_new = f(a, xs[-1])
    xs.append(x_new)

xs = np.array(xs)
d = np.abs(xs - 1 / a)

seq = np.arange(itr+1)

fig2 = plt.figure(figsize=(17, 8))

ax1 = fig2.add_subplot(121)
ax1.plot(seq, xs)
ax1.set_xlabel('iterations(k)')
ax1.set_ylabel('$x_k$')

ax2 = fig2.add_subplot(122)
ax2.plot(seq, d)
ax2.set_xlabel('iterations(k)')
ax2.set_ylabel('$|x_k-x|$')

plt.show()
