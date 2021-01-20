import funkcje as fn
import matplotlib.pyplot as plt
import numpy as np
import in_out as io
from animacja import animacja

g = io.g
d = io.d
theta_0 = np.radians(io.theta_0)
m = io.m
time = np.linspace(0., 30, 100000)
def wykresy():
    plt.subplot(411)
    angle = np.vectorize(fn.angle)
    plt.plot(time, angle(time, theta_0, d, g), label='angle(t)')
    plt.xlabel('time [S]')
    plt.ylabel('angle [rad]')

    plt.subplot(412)
    pot_en = np.vectorize(fn.pot_en)
    plt.plot(time, pot_en(time, d, theta_0, m, g), color='r', label='pot_en(t)')
    plt.xlabel('time [s]')
    plt.ylabel('pot_en [J]')

    plt.subplot(413)
    kin_en = np.vectorize(fn.kin_en)
    plt.plot(time, kin_en(time, d, theta_0, m, g), color='g', label='kin_en(t)')
    plt.xlabel('time [s]')
    plt.ylabel('kin_en [J]')

    plt.subplot(414)
    velocity = np.vectorize(fn.velocity)
    plt.plot(time, velocity(time, d, theta_0, m, g), color='y', label='velocity(t)')
    plt.xlabel('time [s]')
    plt.ylabel('velocity [m/s]')

    animacja()
    plt.show()

