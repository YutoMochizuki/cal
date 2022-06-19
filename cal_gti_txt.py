#!/bin/sh
#使う時はpython3 *.py
#gtiのSTOP-STARTの合計を計算するプログラム
#fstruct スペクトルファイル.fits
#fdump *.fits+2 STDOUT - - prhead=no page=no showrow=no showcol=no showunit=no | tee *.txt
import numpy as np
c = 0
file = input('Enter txt neme : ')#input関数で入力させる
data = np.loadtxt(file)#これで配列に読み込ませられる。csvの場合はdelimiter=","を追加。一行目を読ませないskiprows=1
a = len(data)#配列の数149個ならば0-148
for i in range(a):
    b = data[i][1] - data[i][0]
    c += b
print(c)
