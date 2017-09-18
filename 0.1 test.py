#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: MShokry
"""

import numpy as np
import matplotlib.pyplot as plt

#Dimition Limits
lim = np.array([-1,1])
#random two points
x = np.random.uniform(-1,1,2)
y = np.random.uniform(-1,1,2)
#  y = Ap => A =[x,1] ; p = [m,c]
A = np.vstack([x, np.ones(len(x))]).T
#solving the equation and getting m,c
m, c = np.linalg.lstsq(A, y)[0]
#picking a random set from -1 to 1
datax = np.random.uniform(-1,1,100)
datay = np.random.uniform(-1,1,100)
data = np.vstack([datax,datay]).T
#check line fit
def check(data,m,c):
   return data[:,1] - m*data[:,0]-c
postive = data[check(data,m,c)>=0]
negative = data[check(data,m,c)<0]
#plotting
plt.ylim(-1,1)
plt.xlim(-1,1)
plt.grid(1)
plt.xlabel("X1")
plt.ylabel("X2")
plt.plot(x,y,'o',color='k')
plt.plot(lim,m*lim+c)
plt.plot(postive[:,0],postive[:,1],'.',color = 'b')
plt.plot(negative[:,0],negative[:,1],'.', color = 'r')

