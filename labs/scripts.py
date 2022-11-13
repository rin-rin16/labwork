import numpy as np
import matplotlib.pyplot as plt

def avg(a):
    return sum(a)/len(a)
def rande(a):
    s = 0
    for i in range(len(a)):
        s += (a[i] - avg(a))**2
    return s**0.5/len(a)
def delta(a, b):
    return (rande(a)**2 + b**2)**0.5

def lsm(x, y):
    sumy = sum(y)
    sumx = sum(x)
    sumx2 = 0
    sumy2 = 0
    for i in range(len(x)):
        sumx2 += x[i]**2
        sumy2 += y[i] ** 2
    sumxy = 0
    for i in range(len(x)):
        sumxy += x[i]*y[i]
    n = len(x)
    b = (sumy*sumx2 - sumx*sumxy)/(n*sumx2 - sumx**2)
    a = (n*sumxy - sumx*sumy)/(n*sumx2 - sumx**2)
    D = n*sumx2 - (sumx)**2
    Sy2 = 0
    for i in range(len(x)):
        Sy2 += (y[i]-b-a*x[i])**2/(n-2)
    Sa2 = 0
    Sb2 = 0
    for i in range(len(x)):
        Sa2 += Sy2*n/D
        Sb2 += Sy2 * sumx2/D
    return [a, b, Sa2, Sb2]

def plotlsm(x, y, dx, dy, xlegend = '', ylegend = '', name = ''):
    print('a перед x, b просто')
    print('a = ', lsm(x, y)[0])
    print('b = ', lsm(x, y)[1])
    print('da = ', lsm(x, y)[2])
    print('db = ', lsm(x, y)[3])
    xax = np.linspace(min(x) - 1.5, max(x) + 2, 1000)
    yax = lsm(x, y)[0]*xax + lsm(x, y)[1]
    plt.plot(xax, yax, color="deepskyblue")
    plt.errorbar(x, y, xerr=dx, yerr=dy, fmt=".k", color="blue")
    plt.xlabel(str(xlegend), fontsize=12)
    plt.ylabel(str(ylegend), fontsize=12)
    plt.title(str(name), fontsize=14)
    plt.ylim(5, 14)
    plt.grid()
    plt.show()


