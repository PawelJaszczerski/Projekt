import funkcje as fn
import matplotlib.pyplot as plt
import numpy as np
import in_out as io
from animacja import animacja

g = io.g
d = io.d
theta_0 = np.radians(io.theta_0)
m = io.m
time = np.linspace(0., 2*fn.T, 100000)
def wykresy():
    plt.subplot(411)
    angle = np.vectorize(fn.angle)
    plt.plot(time, angle(time, theta_0, d, g), label='angle')
    plt.xlabel('time')
    plt.ylabel('angle')

    plt.subplot(412)
    pot_en = np.vectorize(fn.pot_en)
    plt.plot(time, pot_en(time, d, theta_0, m, g), color='r', label='pot_en')
    plt.xlabel('time')
    plt.ylabel('pot_en')

    plt.subplot(413)
    kin_en = np.vectorize(fn.kin_en)
    plt.plot(time, kin_en(time, d, theta_0, m, g), color='g', label='kin_en')
    plt.xlabel('time')
    plt.ylabel('kin_en')

    plt.subplot(414)
    velocity = np.vectorize(fn.velocity)
    plt.plot(time, velocity(time, d, theta_0, m, g), color='y', label='velocity')
    plt.xlabel('time')
    plt.ylabel('velocity')

    animacja()
    plt.show()

