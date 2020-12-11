import funkcje as fn
import matplotlib.pyplot as plt
import numpy as np
import math

time = np.linspace(0., 50., 1000)

plt.subplot(311)
angle = np.vectorize(fn.angle)
plt.plot(time, angle(time, np.pi*1/36, 1), label='angle')
plt.xlabel('time')
plt.ylabel('angle')

plt.subplot(312)
pot_en = np.vectorize(fn.pot_en)
plt.plot(time, pot_en(time, 1, np.pi*1/36, 1), color='r', label='pot_en')
plt.xlabel('time')
plt.ylabel('pot_en')

plt.subplot(313)
kin_en = np.vectorize(fn.kin_en)
plt.plot(time, kin_en(time, 1, np.pi*1/36, 1), color='g', label='kin_en')
plt.xlabel('time')
plt.ylabel('kin_en')
plt.show()
