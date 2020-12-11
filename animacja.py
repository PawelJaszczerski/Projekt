import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as ani

g = 10
d = 10
theta_0 = 1/36*np.pi
time = np.linspace(0., 50., 1000)
fig = plt.figure()

lines = plt.plot([])
line = lines[0]
def animation(swing):
    #należy stworzyć odpowiednia funkcję
    position = time*swing
    line.set_data((swing, position))

plt.xlim(-d*2, d*2)
plt.ylim(-d*2, d*2)
ani = ani.FuncAnimation(fig, animation, frames=100, interval=1000)
plt.show()