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



def output():
    odata=open('data.txt','a')
    fn.period(d)
    T=round(fn.T, 4)
    odata.write('\nT[s]:'+str(T))
    fn.angfreq(d)
    omega=round(fn.omega, 4)
    odata.write('\nomega[rad/s]:'+str(omega))
    fn.tot_en(d,theta_0,m)
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






