import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as ani
import funkcje as fn
import in_out as io

io.param()
#przykładowe dane
g = 9.8067
d=io.d
m=io.m
t = np.arange(0., 1000., 0.1)
theta_0=np.radians(io.theta_0)

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
    x = d * np.sin(fn.angle(frame, theta_0, d))
    y = d - d * np.cos(fn.angle(frame, theta_0, d))
    point.set_data(x, y)
    xline = x
    yline = y
    line.set_data([xline0, xline], [yline0, yline])

ani = ani.FuncAnimation(fig, animation, frames=10000, interval=10)
plt.show()