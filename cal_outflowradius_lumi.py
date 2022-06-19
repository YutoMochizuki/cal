#!/bin/sh
#アウトフローまでの半径を計算するプログラム

import math
#L erg/s
L = float(input('Enter luminosity ='))
#logξ erg*cm/s
e = float(input('Enter logξ ='))
e = 10**e
#Nh 1/cm^2
#n 1/cm^3
N = float(input('Nh = '))
N = N*1e22
#アウトフローまでの半径 cm
r = L/e/N * 1e-5
print("Outflow radius =", r,"cm")
