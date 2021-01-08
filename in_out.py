import funkcje as fn
import os
def param():
    try:
        data=open('data.txt', 'r')
        dist=data.readline()
        init_ang=data.readline()
        mass=data.readline()
        acceleration=data.readline()
        global d
        global theta_0
        global m
        global g
        d = float(dist.split(':')[1])
        theta_0 = float(init_ang.split(':')[1])
        if theta_0>10:
            print('Proszę wprowadzić kąt do 10 stopni')
            return
        m = float(mass.split(':')[1])
        try:
            g = float(acceleration.split(':')[1])
        except ValueError:
            g = 9.8067
        return d, theta_0, m, g

    except FileNotFoundError:
        data=open('data.txt', 'a')
        data.write('d[m]:')
        data.write('\ntheta_0[stopnie] - do 10 stopni:')
        data.write('\nm[kg]:')
        data.write('\ng[m/s^2] - domyślnie ziemskie:')
        data.close()



def output():
    odata=open('data.txt','a')
    fn.period(d, g)
    T=round(fn.T, 4)
    odata.write('\nT[s]:'+str(T))
    fn.angfreq(d, g)
    omega=round(fn.omega, 4)
    odata.write('\nomega[rad/s]:'+str(omega))
    fn.tot_en(d,theta_0, m, g)
    Ec=round(fn.Ec, 4)
    odata.write('\nEc[J]:'+str(Ec))
    odata.close()

    try:
        os.rename('data.txt','odata.txt')
    except FileExistsError:
        os.remove('odata.txt')
        os.rename('data.txt','odata.txt')

def preview():
    pdata=open('odata.txt','r')
    prev=pdata.read()
    print(prev)






