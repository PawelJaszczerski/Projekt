import funkcje as fn
import matplotlib.pyplot as plt
import numpy as np
import math
time = np.linspace(0., 100., 1000)
plt.subplot(212)
angle = np.vectorize(fn.angle)
plt.plot(time, angle(time, math.pi*1/12, 1), label='angle')
plt.xlabel('time')
plt.ylabel('angle')
plt.subplot(221)
pot_en = np.vectorize(fn.pot_en)
plt.plot(time, pot_en(time, 1, math.pi*1/12, 1), color='r', label='pot_en')
plt.xlabel('time')
plt.ylabel('pot_en')
plt.subplot(222)
kin_en = np.vectorize(fn.kin_en)
plt.plot(time, kin_en(time, 1, math.pi*1/12, 1), color='g', label='kin_en')
plt.xlabel('time')
plt.ylabel('kin_en')
plt.show()
