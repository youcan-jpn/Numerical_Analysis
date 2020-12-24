# sample: Dahlquist's test equation

import numpy as np
import matplotlib.pyplot as plt

ini = 1
c = -1/2
et = 10
y = [ini]
mtd = 'FEM'


# calculate
# 関数の定義
def g(t, y):
    return c*y


# 自励系に制限
def f(y):
    return g(0, y)


# Forwaed Euler's Method
def FEM(y):
    return y + f(y)*dt


mode = 1  # ここを書き換える
# mode1はあるnに対する近似解のプロット
# mode2は最大誤差のn依存性のグラフ

if mode == 1:

    n = 10  # 分割数はここを変える
    dt = et / n
    tv = np.linspace(0, et, n)

    # plot
    fig, ax1 = plt.subplots(1, 1)

    # 近似解の計算
    for i in range(n-1):
        y.append(FEM(y[-1]))
    ax1.plot(tv, y, label='exact solution')

    # 厳密解の計算
    etv = np.linspace(0, et, 1000)
    ey = ini*np.exp(c*etv)
    ax1.plot(etv, ey, label=mtd)

    ax1.set_xlabel('t')
    ax1.set_ylabel('y')
    plt.legend()
    plt.show()

elif mode == 2:
    max_error = []
    for n in range(2, 12):
        y = [ini]
        dt = et / n
        tv = np.linspace(0, et, n)
        for i in range(n-1):
            y.append(FEM(y[-1]))
        ey = np.exp(c*tv)
        error = np.abs(ey-y)
        max_error.append(np.max(error))

    ns = np.linspace(2, 11, 10)
    fig, ax = plt.subplots(1, 1)
    ax.plot(ns, max_error, label='FEM error')
    ax.set_xlabel('n')
    ax.set_ylabel('error')
    plt.legend
    plt.show()
