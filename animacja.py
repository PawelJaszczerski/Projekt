import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as ani
import funkcje as fn

#przykładowe dane
g = 9.8067
d = 1
m = 1
t = np.arange(0., 1000., 0.1)
theta_0 = 1/24*np.pi

fig = plt.figure()

plt.xlim(-d*2, d*2)
plt.ylim(0, d*2)

lines = plt.plot([], 'o')
line = lines[0]

def animation(frame):
    x = d *  np.sin(fn.angle(frame, theta_0, d))
    y = d - d *  np.cos(fn.angle(frame, theta_0, d))
    line.set_data((x, y))

ani = ani.FuncAnimation(fig, animation, frames=10000, interval=10)
plt.show()