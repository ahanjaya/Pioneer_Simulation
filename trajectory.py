#!/usr/bin/env python3

import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

def plots_(axes_, x_, y_, label_=None, xlabel_="", ylabel_="", title_=""):
    axes_.plot(x_, y_, 'o-', label=label_)
    axes_.set_xlabel(xlabel_)
    axes_.set_ylabel(ylabel_)
    axes_.set_title(title_)
    axes_.grid()

def trajectory_sin(time, res):
    h_curve = 10

    # fig1, axes = plt.subplots(nrows=3, ncols=1, figsize=(8,8))
    fig1, axes = plt.subplots(nrows=3, ncols=1)

    # Axes 0
    t = np.linspace(0.0, np.pi, num=time/res)
    s = np.sin(t) #* 0
    plots_(axes[0], t, s, None, "theta (${\Theta}$)", "sin (${\Theta}$)", "Trajectory Planning - Sinus")

    # Axes1
    total_time = np.linspace(0.0, time, num=time/res)
    plots_(axes[1], total_time, total_time*0, None, "time")

    # Axes2
    x_dis = np.interp(t, [0, np.pi], [20, 40])
    y_dis = np.interp(s, [0, 1], [10, 30])
    # y_dis = h_curve * s
    plots_(axes[2], x_dis, y_dis, None, "x distance", "y distance")

    # fig1.legend()
    fig1.tight_layout()

def gaussian(x, mu, sig):
    return np.exp( -np.power(x - mu, 2.) / (2 * np.power(sig, 2.)) )

def normal_gaussian(x, mu, sig):
    return ( 1 / (sig * np.sqrt(2*np.pi)) ) * np.exp( -np.power(x - mu, 2.) / (2 * np.power(sig, 2.)) )

def trajectory_gaussian(time, res):
    x_values = np.linspace(-5, 5, num=time/res)
    # x_values = np.linspace(-5, 5, num=200)
    fig2, axes = plt.subplots(nrows=3, ncols=1)

    # Axes1
    total_time = np.linspace(0.0, time, num=time/res)
    plots_(axes[1], total_time, total_time*0, None, "time")

    # Axes2
    x_dis = np.interp(x_values, [-5, 5], [20, 40])

    for mu, sig in [(0, 1.0), (0, 0.8), (-2, 0.5)]:
        label = "$\mu$ = {0}, $\sigma$ = {1}".format(mu, sig) 
        # plots_(axes, x_values, gaussian(x_values, mu, sig), label, r'X', r'$\varphi _{\mu ,\sigma ^{2}} = (X)$', "Trajectory Gaussian")
        # plots_(axes, x_values, normal_gaussian(x_values, mu, sig), label, r'X', r'$\varphi _{\mu ,\sigma ^{2}} = (X)$', "Trajectory Gaussian")

        # Axes 0
        # y_values = normal_gaussian(x_values, mu, sig)
        y_values = norm.pdf(x_values, mu, sig)
        plots_(axes[0], x_values, y_values, label, r'X', r'$\varphi _{\mu ,\sigma ^{2}} = (X)$', "Trajectory Gaussian")

        # Axes2
        y_dis = np.interp(y_values, [0, np.max(y_values)], [10, 30])
        plots_(axes[2], x_dis, y_dis, None, "x distance", "y distance")

    fig2.legend()

def main():
    time = 3
    res  = 0.1
    trajectory_sin(time, res)
    trajectory_gaussian(time, res)

    plt.show(block=False)
    plt.pause(0.1)
    input("Press [enter] to close.")
    plt.close('all')

if __name__ == '__main__':
    main()