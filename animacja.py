import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as ani
import funkcje as fn

#przykładowe dane
g = 9.8067
d = 1
m = 1
t = np.arange(0., 1000., 0.1)
theta_0 = 1/36*np.pi

fig = plt.figure()

plt.xlim(-d, d)
plt.ylim(-d/5, d)

points = plt.plot([], 'bo')
point = points[0]

xline0, yline0 = 0, d
lines = plt.plot([], [], '-')
line = lines[0]

def animation(frame):
    global x, y
    x = d *  np.sin(fn.angle(frame, theta_0, d))
    y = d - d *  np.cos(fn.angle(frame, theta_0, d))
    point.set_data(x, y)
    xline = x
    yline = y
    line.set_data([xline0, xline], [yline0, yline])

ani = ani.FuncAnimation(fig, animation, frames=10000, interval=10)
plt.show()