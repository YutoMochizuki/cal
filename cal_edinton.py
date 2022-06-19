#!/bin/sh
#エディントン光度を計算するプログラム
#L=3.4e+4*太陽光度*M/ソーラーマス
#1erg=1e-7J
import math
M = float(input('Enter mass of black hole ='))
L = 3.2e+4 * 3.828e+33 * M
#print(round(L, 2)) 有効数字になるはず...
print("Edinton Luminosity =", L,"erg/s")
#print("Edinton Luminosity =", L*1e-7,"J/s")
