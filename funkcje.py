import math
# d - długość wahadła [m]
# theta_0 - kąt wychylenia początkowego [rad]
# g - przyspieszenie grawitacyjne (docelowo ziemskie jako domyślne lub wprowadzane przez użytkownika)
# m - masa punktowa [kg]
# omega - częstość kołowa [rad/s]
# T - okres [s]
g = 9.8067
def częstość(d):
    global omega
    omega = d/g
    return omega
def okres(omega):
    global T
    T= 2*math.pi*(omega)**(1/2)
    return T

