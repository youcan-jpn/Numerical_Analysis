import matplotlib.pyplot as plt
import numpy as np


def f(a, x):
    '''
    x_kからx_{k+1}を求める関数
    '''
    return x*(2-a*x)


a = 2
ini_val = 0.9  # 0 < ini_val < 2/a のとき1/aに収束
itr = 50
xs = [ini_val]

fig1, ax = plt.subplots()
x = np.linspace(-1, 1, 100)
y = f(a, x)
ax.plot(x, y, c='black', label='$f(x)=-{0}x^2+2x$\n $(a={1})$'.format(a, a))
axx = [-1, 1]
axy = [0, 0]
ax.plot(axx, axy, c='lightgray')
x0 = [0, 2/a]
y0 = [0, 0]
ax.scatter(x0, y0, color='red')

ax.set_ylabel('$f(x)$')
ax.set_xlabel('$x$')
ax.legend()

for i in range(itr):
    x_new = f(a, xs[-1])
    xs.append(x_new)

xs = np.array(xs)
print(xs[-1])
d = np.abs(xs - 1 / a)

seq = np.arange(itr+1)

fig2 = plt.figure(figsize=(17, 8))

ax1 = fig2.add_subplot(121)
ax1.plot(seq, xs, label=r'$x_k\ (a={})$'.format(a))
ax1.set_xlabel('iterations(k)')
ax1.set_ylabel('$x_k$')
ax1.legend()

ax2 = fig2.add_subplot(122)
ax2.plot(seq, d, label=r'$|x_k-\frac{{1}}{{{}}}|$'.format(a))
ax2.set_xlabel('iterations(k)')
ax2.set_ylabel(r'$|x_k-\frac{{1}}{{{}}}|$'.format(a))
ax2.legend()

plt.show()
