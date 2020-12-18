import numpy as np
# d - długość wahadła [m]
# theta_0 - kąt wychylenia początkowego [rad]
# g - przyspieszenie grawitacyjne (docelowo ziemskie jako domyślne lub wprowadzane przez użytkownika)
# m - masa punktowa [kg]
# omega - częstość kołowa [rad/s]
# T - okres [s]
# t - czas [s]

#przykładowe dane
g = 9.8067
d = 10
m = 1
t = np.arange(0., 1000., 0.1)
theta_0 = 1/12*np.pi

def angfreq(d):
    global omega
    omega = (d/g)**(1/2)
    return omega
def period(d):
    global T
    angfreq(d)
    T = 2*np.pi*(omega)
    return T
def angle(t, theta_0, d):
    angfreq(d)
    global theta
    theta=theta_0* np.cos(omega*t)
    return theta
def pot_en(t, d, theta_0, m):
    angle(t, theta_0, d)
    global Ep
    Ep = m*g*d*(1-np.cos(theta))
    return Ep
def kin_en(t, d, theta_0, m):
    angle(t, theta_0, d)
    global Ek
    Ek = m*g*d*(np.cos(theta)-np.cos(theta_0))
    return Ek
def tot_en(d, theta_0, m):
    global Ec
    Ec = m*g*d*(1-np.cos(theta_0))
    return Ec
def velocity(t, d, theta_0, m):
    global v
    kin_en(t, d, theta_0, m)
    v = (2*Ek/m)**(1/2)
    return v
