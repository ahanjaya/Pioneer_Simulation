#!/usr/bin/env python3

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from mayavi import mlab
from mpl_toolkits.mplot3d import Axes3D 

def plots_(axes_, x_, y_, label_=None, xlabel_="", ylabel_="", title_=""):
    axes_.plot(x_, y_, 'o-', label=label_)
    axes_.set_xlabel(xlabel_)
    axes_.set_ylabel(ylabel_)
    axes_.set_title(title_)
    axes_.grid()

def main():
    load  = True
    DEBUG = False
    np.set_printoptions(suppress=True)

    if not load:
        lidar_points = np.random.rand(75,161)
        height_robot = 0.58
        np.savez('lidar.npz', lidar_points=lidar_points, height_robot=height_robot)
    else:
        data = np.load('lidar.npz')
        lidar_points = data['lidar_points']
        height_robot = data['height_robot']

    head_pitch = 85
    tilt_rate = -1
    
    z_list=[]
    y_list=[]
    x_list=[]

    for points in lidar_points:
        z = points * np.cos(np.radians(90 - head_pitch))
        ho = height_robot - z
        z_list.append(ho)
        x = points * np.sin(np.radians(90 - head_pitch))
        y_list.append(x)
        y = np.arange(0, len(points))
        x_list.append(y)

        head_pitch += tilt_rate

        # if head_pitch < 10:
        #     break

    # plot point cloud
    # fig = plt.figure()
    # ax = fig.add_subplot(111, projection='3d')
    x_list= np.array(x_list)
    y_list= np.array(y_list)
    z_list= np.array(z_list)
    # ax.scatter(x_list, y_list, z_list)
    # ax.plot_wireframe(x_list, y_list, z_list, rstride=10, cstride=10)
    mlab.points3d(x_list, y_list, z_list, y_list, scale_mode='none', scale_factor=1)

    mlab.axes()
    mlab.show()

    layers = np.mean(lidar_points, axis=1)
    angle = np.arange(85, 10, -1)

    if DEBUG:
        print(lidar_points)
        print(layers)
        print(angle)
        print(height_robot)

    # plot layers point
    fig1, axes = plt.subplots(nrows=1, ncols=1)
    plots_(axes, angle, layers, None, "", "", "")
   
    plt.show()
    # plt.show(block=False)
    # plt.pause(0.1)
    # input("Press [enter] to close.")
    # plt.close('all')


if __name__ == '__main__':
    main()