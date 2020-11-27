import math
# d - długość wahadła [m]
# theta_0 - kąt wychylenia początkowego [rad]
# g - przyspieszenie grawitacyjne (docelowo ziemskie jako domyślne lub wprowadzane przez użytkownika)
# m - masa punktowa [kg]
# omega - częstość kołowa [rad/s]
# T - okres [s]
# t - czas [s]
g = 9.8067
def czestosc(d):
    global omega
    omega = d/g
    return omega
def okres(d):
    global T
    czestosc(d)
    T = 2*math.pi*(omega)**(1/2)
    return T
def wychylenie(t, theta_0, d):
    czestosc(d)
    global theta
    theta=theta_0* math.sin(omega*t+theta_0)
    return theta
def energia_potencjalna(t, d, theta_0, m):
    wychylenie(t, theta_0, d)
    global Ep
    Ep = m*g*d*(1-math.cos(theta))
    return Ep
def energia_kinetyczna(t, d, theta_0, m):
    wychylenie(t, theta_0, d)
    global Ek
    Ek = m*g*d*(math.cos(theta)-math.cos(theta_0))
    return Ek
def energia_calkowita(t, d, theta_0, m):
    energia_potencjalna(t, d, theta_0, m)
    energia_kinetyczna(t, d, theta_0, m)
    global Ec
    Ec = Ek + Ep
    return Ec