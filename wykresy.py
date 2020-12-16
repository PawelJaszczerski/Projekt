import funkcje as fn
import matplotlib.pyplot as plt
import numpy as np
import math

time = np.linspace(0., 50., 1000)

plt.subplot(411)
angle = np.vectorize(fn.angle)
plt.plot(time, angle(time, np.pi*1/36, 1), label='angle')
plt.xlabel('time')
plt.ylabel('angle')

plt.subplot(412)
pot_en = np.vectorize(fn.pot_en)
plt.plot(time, pot_en(time, 1, np.pi*1/36, 1), color='r', label='pot_en')
plt.xlabel('time')
plt.ylabel('pot_en')

plt.subplot(413)
kin_en = np.vectorize(fn.kin_en)
plt.plot(time, kin_en(time, 1, np.pi*1/36, 1), color='g', label='kin_en')
plt.xlabel('time')
plt.ylabel('kin_en')

plt.subplot(414)
velocity = np.vectorize(fn.velocity)
plt.plot(time, velocity(time, 1, np.pi*1/36, 1), color='y', label='velocity')
plt.xlabel('time')
plt.ylabel('velocity')
plt.show()