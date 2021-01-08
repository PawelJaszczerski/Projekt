import numpy as np

def angfreq(d, g):
    global omega
    omega = (g/d)**(1/2)
    return omega
def period(d, g):
    global T
    angfreq(d, g)
    T = 2*np.pi*(1/omega)
    return T
def angle(t, theta_0, d, g):
    angfreq(d, g)
    global theta
    theta=theta_0* np.cos(omega*t)
    return theta
def pot_en(t, d, theta_0, m, g):
    angle(t, theta_0, d, g)
    global Ep
    Ep = m*g*d*(1-np.cos(theta))
    return Ep
def kin_en(t, d, theta_0, m, g):
    angle(t, theta_0, d, g)
    global Ek
    Ek = m*g*d*(np.cos(theta)-np.cos(theta_0))
    return Ek
def tot_en(d, theta_0, m, g):
    global Ec
    Ec = m*g*d*(1-np.cos(theta_0))
    return Ec
def velocity(t, d, theta_0, m, g):
    global v
    kin_en(t, d, theta_0, m, g)
    v = (2*Ek/m)**(1/2)
    return v