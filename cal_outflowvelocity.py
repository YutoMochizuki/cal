#!/bin/sh
#天体までの距離とmodelfluxから光度を計算するプログラム

import math
#光速km/s
c =299792.458
#redshiht
z = float(input('Enter cosmic redshiht ='))
#az = float(input('Enter cosmic redshiht error='))
V = float(input('Enter spec redshiht ='))
z=z-V
m = (z+1)**2
#vは後退速度
v = c*(m-1)/(m+1)
print("velocity =", v ,"km/s")
print("velocity =", v/c ,"c")
