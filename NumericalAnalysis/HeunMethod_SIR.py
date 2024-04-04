"""
ホイン法によって微分方程式を可視化する
"""

import math
import matplotlib.pyplot as plt

dt = 0.01


def dsdt(s,i):
    return(-0.0015*s*i)
def didt(s,i):
    return(0.0015*s*i-0.9*i)
def drdt(i):
    return(0.9*i)
# 初期値
s0 = 1000
i0 = 1
r0 = 0
dtlis =[0.01]
s_list=[]
i_list=[]
r_list=[]
sum_list=[]
sp=s0
ip=i0
rp=r0
s_list.append(sp)
i_list.append(ip)
r_list.append(rp)
sum_list.append(sp+ip+rp)
i = 0
while i_list[i]>0.00001:

    k1 = dsdt(s_list[i],i_list[i])
    l1 = didt(s_list[i],i_list[i])
    r1 = drdt(i_list[i])
    
    k2 = dsdt(s_list[i]+dt*k1,i_list[i]+dt*l1)
    l2 = didt(s_list[i]+dt*k1,i_list[i]+dt*l1)
    r2 = drdt(i_list[i]+dt*l1)
    
    sp = dt*(k1+k2)/2 + sp
    ip = dt*(l1+l2)/2 + ip
    rp = dt*(r1+r2)/2 + rp

    s_list.append(sp)
    i_list.append(ip)
    r_list.append(rp)
    sum_list.append(sp+ip+rp)
    dt = dt + 0.01
    dtlis.append(dt)
    i+=1

plt.scatter(dtlis,s_list,s=0.5,label="S")
plt.scatter(dtlis,i_list,s=0.5, label="I")
plt.scatter(dtlis,r_list,s=0.5, label="R")
plt.scatter(dtlis,sum_list,s=0.5, label="Sum")
plt.legend()
plt.show()
