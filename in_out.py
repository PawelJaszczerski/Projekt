import funkcje as fn
import os
def param():
    try:
        data=open('data.txt', 'r')
        dist=data.readline()
        init_ang=data.readline()
        mass=data.readline()
        global d
        global theta_0
        global m
        d = float(dist.split(':')[1])
        theta_0 = float(init_ang.split(':')[1])
        m = float(mass.split(':')[1])
        return d, theta_0, m

    except FileNotFoundError:
        data=open('data.txt', 'a')
        data.write('d[m]:')
        data.write('\ntheta_0[stopnie]:')
        data.write('\nm[kg]:')
        data.close()
        print('proszę wprowadzić dane do pliku tekstowego i uruchomić program ponownie')


param()

def output():
    odata=open('data.txt','a')
    fn.period(d)
    T=fn.T
    odata.write('T[s]:'+str(T))
    fn.angfreq(d)
    omega=fn.omega
    odata.write('\nomega[rad/s]:'+str(omega))
    odata.close()


output()