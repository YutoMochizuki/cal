#!/bin/sh
#赤方偏移の補正をしたエネルギーを計算するプログラム

import math
#redshiht
z = float(input('Enter cosmic redshiht ='))
az = float(input('Enter cosmic redshiht error='))
e = float(input('Enter line energy ='))

#flux erg/cm^2/s
E = e/(z+1)
bE = e/(z+az+1)
cE = e/(z-az+1)
print("observed line energy  =", E,cE-E,bE-E,"keV")
