#!/bin/sh
#天体までの距離とmodelfluxから光度を計算するプログラム

import math
#光速km/s
c =299792.458
#ハッブル定数(A. Riess+2016)
H0 = 73.24
#誤差
aH= 1.74
#redshiht
z = float(input('Enter cosmic redshiht ='))
az = float(input('Enter cosmic redshiht error='))
m = (z+1)**2
#vは後退速度
v = c*(m-1)/(m+1)
#距離Mpc
D = v/H0
print(D)
print("light year =",D*0.0326)
D = D*10**8 *3.085677581e+16
#error
aD=D*math.sqrt((aH/H0)**2 + (az/z)**2)
print("Distance =", D ,"±",aD,"cm")

#model fluxからLを計算
#flux erg/cm^2/s
F = float(input('Enter model flux ='))
L = 4*math.pi*D*D * F
l =  4*math.pi*aD*aD * F
print("Object Luminosity =", L, "±",l,"erg/s")
