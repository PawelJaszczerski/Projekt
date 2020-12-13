import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as ani

#przykładowe dane
g = 9.8067
d = 10
m = 1
t = np.arange(0., 1000., 0.1)
theta_0 = 1/36*np.pi

fig = plt.figure()
plt.axis('scaled')
plt.xlim(-d*2, d*2)
plt.ylim(-d*2, 0)

lines = plt.plot([], 'o')
line = lines[0]

def animation(frame):
    x = d*np.sin(np.cos(frame/100))
    y = d-d*np.cos(np.sin(frame/100))
    line.set_data((x, -y))

ani = ani.FuncAnimation(fig, animation, frames=100000, interval=5)
plt.show()