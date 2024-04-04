#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 18:52:57 2022

@author: imao
"""

from math import pi,e, log, factorial
import matplotlib.pyplot as plt


### 
def g(i, x): # ラグランジュ補間の係数の計算。メイン。
    dum=1.0
    for j in range(len(x_lis)):
        if j != i :
            dum *= (x-x_lis[j])/(x_lis[i]-x_lis[j])
    return dum

#
def fLag(x,m): #ラグランジュ補間
    dum=0.0
    for j in range(m):
        dum += y_lis[j]*g(j, x)

    return dum 
###

## 例題のためのデータセット構築
m = 11  #  
x_lis = []
y_lis = []
def yy(x):
    return 1/(1+25*(x**2)) # 例題の関数 y = 1/(1+x**2)

for k in range(m):
    xm = -1.0 + (22/10)*(k / m)
    x_lis.append(xm)
    y_lis.append(yy(xm))
    

plt.plot(x_lis,y_lis, 'o',label='Row data')

print(x_lis)
print(y_lis)
##

### ラグランジュ補間実行
mm = 500
y_Laglis = []
xx_lis = []
for k  in range(mm):
    xm = -1.0 + (1000/499)*(k / mm)
    xx_lis.append(xm)


y_lis_exact=[]
for j in range(mm):#mm回繰り返す
    y_Laglis.append(fLag(xx_lis[j],m))
    y_lis_exact.append(yy(xx_lis[j]))

print(xx_lis)
print("flag")
print(y_Laglis)

#plot
plt.grid(True)
plt.xlabel('x',fontsize=24)
plt.ylabel('f(x)',fontsize=24)
plt.xticks(fontsize=9)
plt.yticks(fontsize=9)
plt.plot(xx_lis,y_Laglis, color='Red',label='Lagrange')
plt.plot(xx_lis,y_lis_exact, color='Black',label='Exact')
plt.legend(loc='upper left')
plt.ylim([-0.5,2.3])
plt.xlim([-1.1,1.1])


plt.show()