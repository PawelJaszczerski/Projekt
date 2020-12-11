import math
# d - długość wahadła [m]
# theta_0 - kąt wychylenia początkowego [rad]
# g - przyspieszenie grawitacyjne (docelowo ziemskie jako domyślne lub wprowadzane przez użytkownika)
# m - masa punktowa [kg]
# omega - częstość kołowa [rad/s]
# T - okres [s]
# t - czas [s]
g = 9.8067
def angfreq(d):
    global omega
    omega = (d/g)**(1/2)
    return omega
def period(d):
    global T
    angfreq(d)
    T = 2*math.pi*(omega)
    return T
def angle(t, theta_0, d):
    angfreq(d)
    global theta
    theta=theta_0* math.cos(omega*t)
    return theta
def pot_en(t, d, theta_0, m):
    angle(t, theta_0, d)
    global Ep
    Ep = m*g*d*(1-math.cos(theta))
    return Ep
def kin_en(t, d, theta_0, m):
    angle(t, theta_0, d)
    global Ek
    Ek = m*g*d*(math.cos(theta)-math.cos(theta_0))
    return Ek
def tot_en(t, d, theta_0, m):
    pot_en(t, d, theta_0, m)
    kin_en(t, d, theta_0, m)
    global Ec
    Ec = Ek + Ep
    return Ec

print(angle(1,0.1,1))