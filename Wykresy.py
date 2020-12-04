import funkcje as fn
import matplotlib.pyplot as plt
import numpy as np
import math
time = np.linspace(0., 1000., 10000)
angle = np.vectorize(fn.angle)
plt.plot(time, angle(time, math.pi*1/12, 0.5))
plt.show()
