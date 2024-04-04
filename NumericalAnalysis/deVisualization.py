#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 26 13:42:00 2022

@author: imao

ルンゲクッタ法による微分方程式の可視化

"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def dsdt(s, i, B):
    return B * s * i

def didt(s, i, B, G):
    return -B * s * i - G * i

def drdt(i, G):
    return G * i

# 初期値
s0 = 1000
i0 = 100
r0 = 0
dt = 0.01
s_list = [s0]
i_list = [i0]
r_list = [r0]
dt_list = [0.01]

fig, ax = plt.subplots()
ax.set_ylim(-100, 1100)
ax.set_xlim(0, 1)
ax.legend(["S", "I", "R"])

def plot(data):
    global dt, s_list, i_list, r_list

    bata = -0.0015
    Ga = 0.9

    k1 = dsdt(s_list[-1], i_list[-1], bata)
    l1 = didt(s_list[-1], i_list[-1], bata, Ga)
    r1 = drdt(i_list[-1], Ga)

    k2 = dsdt(s_list[-1] + dt * k1, i_list[-1] + dt * l1, bata)
    l2 = didt(s_list[-1] + dt * k1, i_list[-1] + dt * l1, bata, Ga)
    r2 = drdt(i_list[-1] + dt * l1, Ga)

    sp = dt * (k1 + k2) / 2 + s_list[-1]
    ip = dt * (l1 + l2) / 2 + i_list[-1]
    rp = dt * (r1 + r2) / 2 + r_list[-1]

    s_list.append(sp)
    i_list.append(ip)
    r_list.append(rp)

    dt += 0.01
    dt_list.append(dt)

    if len(dt_list) > 90:  # 描画範囲を更新
        ax.set_xlim(ax.get_xlim()[1], ax.get_xlim()[1] + 0.01)

    ax.plot(dt_list, s_list, label="S")
    ax.plot(dt_list, i_list, label="I")
    ax.plot(dt_list, r_list, label="R")

ani = animation.FuncAnimation(fig, plot, interval=10)
plt.show()

