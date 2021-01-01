import numpy as np
import matplotlib.pyplot as plt


def f(a, p, x):
    '''
    x_kからx_{k+1}を求める関数
    '''
    return x - x / p + a / (p*(x**(p-1)))


# 各種パラメータ
a = 7
p = 5
ini_val = 0.1
itr = 300
xs = [ini_val]


# f(x)のプロット
fig1, ax = plt.subplots()
xn = np.linspace(-5, 0, 100)
xp = np.linspace(0, 5, 100)
yn = f(a, p, xn)
yp = f(a, p, xp)

ax.plot(xn, yn, c='black')
ax.plot(xp, yp, c='black')
ax.set_xlabel('$x$')
ax.set_ylabel(r'$f(x)=\frac{{{2}x}}{{{0}}} + \frac{{{1}}}{{{1}x^{{{2}}}}}$'.format(a, p, p-1))


# 数列{x_k}を計算する
for i in range(itr):
    x_new = f(a, p, xs[-1])
    xs.append(x_new)

xs = np.array(xs)

# (itr)回反復した後のx_kの値を出力
print(xs[-1])


# x_k及び|x_k-a^{1/p}|のプロット
fig2 = plt.figure(figsize=(17, 8))

# 横軸の目盛り(iterations)を作成
seq = np.arange(itr+1)

# x_kのプロット
ax1 = fig2.add_subplot(121)
ax1.plot(seq, xs)
ax1.set_xlabel('iterations(k)')
ax1.set_ylabel('$x_k$')

# |x_k-a^{1/p}|のプロット
ax2 = fig2.add_subplot(122)
d = np.abs(xs-np.power(a, 1/p))
ax2.plot(seq, d)
ax2.set_xlabel('iterations(k)')
ax2.set_ylabel(r'$|x_k-{0}^\frac{{1}}{{{1}}}|$'.format(a, p))

plt.show()
