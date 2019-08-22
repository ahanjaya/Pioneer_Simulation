#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def trajectory_sin():
    print("test")

def main():
    time = 1
    res  = 0.1
    h_curve = 10

    t = np.linspace(0.0, np.pi, num=time/res)
    s = np.sin(t)
    # s = np.sin(t) * 0

    plt.subplot(3, 1, 1)
    plt.plot(t, s, 'o-')
    plt.ylabel("sin (${\Theta}$)")
    plt.xlabel("theta (${\Theta}$)")
    plt.title('Trajectory Planning Using Sin')
    plt.grid()

    waktu = np.linspace(0.0, time, num=time/res)
    plt.subplot(3, 1, 2)
    plt.plot(waktu, waktu*0, 'o-')
    plt.xlabel("time")
    plt.grid()

    plt.subplot(3, 1, 3)
    x_dis = np.interp(t, [0, np.pi], [20, 40])
    y_dis = np.interp(s, [0, 1], [10, 30])
    # y_dis = h_curve * s

    plt.plot(x_dis, y_dis, 'o-')
    plt.ylabel("y distance")
    plt.xlabel("x distance")
    plt.grid()

    plt.tight_layout()
    plt.show()  


if __name__ == '__main__':
    main()