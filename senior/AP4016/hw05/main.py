# -*- coding: utf-8 -*-
'''
Created Date: 2023/12/20
Author: @1chooo (Hugo ChunHo Lin)
Version: v0.0.1
'''


import os
import matplotlib.pyplot as plt
import numpy as np


def lorenz(
        xyzth, 
        theta, 
        s=10., 
        r=24.74, 
        b=2.6666667, 
        f=2.5
    ) -> np.array:

    x, y, z = xyzth
    x_dot = s * (y - x) + f * np.cos(theta)
    y_dot = r * x - y - x * z + f * np.sin(theta)
    z_dot = x * y - b * z

    return np.array(
        [x_dot, y_dot, z_dot]
    )


def main():
    os.makedirs(
        f"./imgs/",
        exist_ok=True
    )

    pi = np.pi
    dt = 0.01
    num_steps = 5001
    theta = 45 / 180 * np.pi
    xyzs = np.empty((num_steps + 1, 3))
    xyzs[0] = (0., 10., 0.)

    for i in range(num_steps):
        theta = theta + pi * dt / 180
        xyzs[i + 1] = xyzs[i] + lorenz(xyzs[i], theta) * dt

    # Plot 3D Lorenz Attractor
    fig = plt.figure(figsize=(8, 6), dpi=400)
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(*xyzs.T[0:3], lw=0.5)
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")
    ax.set_title("Lorenz Attractor")
    plt.savefig("./imgs/lorenz_attractor_3d.jpg")
    plt.close()

    # Plot X-t
    plt.figure(figsize=(8, 6), dpi=400)
    plt.plot(dt * np.arange(num_steps + 1), xyzs[:, 0], lw=0.5)
    plt.grid("--")
    plt.xlabel("Time (t)")
    plt.ylabel("X Axis")
    plt.title("X-t Plot")
    plt.savefig("./imgs/x_t_plot.jpg")
    plt.close()

    # Plot X-z
    plt.figure(figsize=(8, 6), dpi=400)
    plt.plot(xyzs[:, 0], xyzs[:, 2], lw=0.5)
    plt.grid("--")
    plt.xlabel("X Axis")
    plt.ylabel("Z Axis")
    plt.title("X-z Plot")
    plt.savefig("./imgs/x_z_plot.jpg")
    plt.close()

    # Plot Z-t
    plt.figure(figsize=(8, 6), dpi=400)
    plt.plot(dt * np.arange(num_steps + 1), xyzs[:, 2], lw=0.5)
    plt.grid("--")
    plt.xlabel("Time (t)")
    plt.ylabel("Z Axis")
    plt.title("Z-t Plot")
    plt.savefig("./imgs/z_t_plot.jpg")
    plt.close()

    # Plot Z-y
    plt.figure(figsize=(8, 6), dpi=400)
    plt.plot(xyzs[:, 2], xyzs[:, 1], lw=0.5)
    plt.grid("--")
    plt.xlabel("Z Axis")
    plt.ylabel("Y Axis")
    plt.title("Z-y Plot")
    plt.savefig("./imgs/z_y_plot.jpg")
    plt.close()

    # Plot Y-t
    plt.figure(figsize=(8, 6), dpi=400)
    plt.plot(dt * np.arange(num_steps + 1), xyzs[:, 1], lw=0.5)
    plt.grid("--")
    plt.xlabel("Time (t)")
    plt.ylabel("Y Axis")
    plt.title("Y-t Plot")
    plt.savefig("./imgs/y_t_plot.jpg")
    plt.close()

    # Plot X-y
    plt.figure(figsize=(8, 6), dpi=400)
    plt.plot(xyzs[:, 0], xyzs[:, 1], lw=0.5)
    plt.grid("--")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.title("X-y Plot")
    plt.savefig("./imgs/x_y_plot.jpg")
    plt.close()


if __name__ == "__main__":
    main()
