# -*- coding: utf-8 -*-
'''
Create Date: 2023/10/06
Author: @1chooo (Hugo ChunHo Lin)
Version: v0.0.1
'''

from typing import Any
import numpy as np  
import matplotlib.pyplot as plt 
import os

def plot_data(
        factor, 
        lat,
    ):
    level = [1010, 925, 775, 600, 400, 100]
    plt.figure(
        figsize=(6, 3), 
        dpi=300,
    )
    var = np.zeros(
        (6, 25)
    )
    var[1:,:] = factor[:, :, 16]

    contour = plt.contour(
        lat, 
        level, 
        var, 
        cmap='coolwarm',
        levels = np.linspace(-0.002, 0.002, 9),
    )
    
    plt.title("120E vetical velocity")
    plt.xlabel("Latitude (degrees)")
    plt.ylabel("Pressure (hPa)")
    plt.clabel(
        contour, 
        inline=1, 
        fontsize=5, 
        fmt='%1.4f',
    )

    plt.xticks(np.linspace(15, 60, 10))
    plt.yticks(np.linspace(1000, 100, 10))
    plt.yscale('log')

    plt.gca().yaxis.set_major_formatter(
        plt.FormatStrFormatter('%.0f')
    )
    plt.colorbar(
        contour, 
        orientation='vertical', 
        shrink=0.7, 
        label="(m/s)",
    )
    plt.gca().invert_yaxis()
    plt.ylim(1010, 100)
    plt.grid(
        visible=True, 
        linestyle='--', 
        alpha=0.5,
    )
    plt.savefig("120E_vetical_velocity.png")

    # plt.show()