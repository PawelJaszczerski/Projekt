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
        data.close()
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
            template()
            print('Proszę wprowadzić dane za dwukropkiem')
            return
        try:
            theta_0 = float(init_ang.split(':')[1])
            if theta_0>10 or theta_0<-10:
                print('Proszę wprowadzić kąt z przedziału [-10, 10]')
                return
        except IndexError:
            template()
            print('Proszę wprowadzić dane za dwukropkiem')
            return
        try:
            m = float(mass.split(':')[1])
            if m<0:
                print('Proszę wprowadzić dodatnią masę')
                return
        except IndexError:
            print('Proszę wprowadzić dane za dwukropkiem')
            template()
            return

        try:
            ac = acceleration.split(':')[1].rstrip().lower()
            gamma = {'ziemia': 9.8067, 'merkury': 3.7, 'wenus': 8.9, 'mars': 3.7, 'jowisz': 23.1, 'saturn': 9.0, 'uran': 8.7, 'neptun': 11.0, 'pluton': 0.7, 'księżyc': 1.6, 'słońce': 274}
            if ac in gamma:
                g=gamma[ac]
            else:
                try:
                    g=float(ac)
                except ValueError:
                    g = 9.8067
        except IndexError:
            print('Proszę wprowadzić dane za dwukropkiem')
            template()
            return
        return d, theta_0, m, g

    except FileNotFoundError:
        template()



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

def template():
    data = open('data.txt', 'w')
    data.write('długość d wahadła [m]:')
    data.write('\nkąt wychylenia początkowego theta_0[stopnie][-10, 10]:')
    data.write('\nmasa m wahadła [kg]:')
    data.write('\nciało niebieskie lub wartość przyspieszenia grawitacyjnego g[m/s^2](domyślnie ziemskie):')
    data.close()