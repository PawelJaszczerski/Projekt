import funkcje as fn
import os
import numpy as np
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
        try:
            d = float(dist.split(':')[1])
            if d<=0:
                print('Proszę wprowadzić dodatnią długość wahadła')
                return
        except IndexError:
            print('Proszę wprowadzić dane za dwukropkiem')
            return
        try:
            theta_0 = float(init_ang.split(':')[1])
            if theta_0>10 or theta_0<-10:
                print('Proszę wprowadzić kąt z przedziału [-10, 10]')
                return
        except IndexError:
            print('Proszę wprowadzić dane za dwukropkiem')
            return
        try:
            m = float(mass.split(':')[1])
            if m<0:
                print('Proszę wprowadzić dodatnią masę')
                return
        except IndexError:
            print('Proszę wprowadzić dane za dwukropkiem')
            return
        try:
            g = float(acceleration.split(':')[1])
        except ValueError:
            g = 9.8067
        except IndexError:
            print('Proszę wprowadzić dane za dwukropkiem')
            return
        return d, theta_0, m, g

    except FileNotFoundError:
        data=open('data.txt', 'a')
        data.write('długość d wahadła [m]:')
        data.write('\nkąt wychylenia początkowego theta_0[stopnie][-10, 10]:')
        data.write('\nmasa m wahadła [kg]:')
        data.write('\nciało niebieskie lub wartość przyspieszenia grawitacyjnego g[m/s^2](domyślnie ziemskie):')
        data.close()



def output():
    odata=open('data.txt','a')
    T=round(fn.period(d, g), 4)
    odata.write('\nT[s]:'+str(T))
    omega=round(fn.angfreq(d, g), 4)
    odata.write('\nomega[rad/s]:'+str(omega))
    Ec=round(fn.tot_en(d,np.radians(theta_0), m, g), 4)
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