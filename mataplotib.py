# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 11:09:21 2023

@author: khushbu vora
"""

# metaplotib
import matplotlib.pyplot as plt
import numpy as np
xpoint=np.array([0,6])
ypoint=np.array([0,250])

plt.plot(xpoint,ypoint)
plt.show()
#====================================================================
xpoint=np.array([0,6])
ypoint=np.array([0,250])
plt.plot(xpoint,ypoint)
plt.xlabel('x point')
plt.ylabel('y point')
plt.show() 
#========================================================================
xpoint=np.array([0,1,2,3])
ypoint=np.array([3,8,1,10])
plt.subplot(1,2,1)
plt.plot(xpoint,ypoint)

xpoint=np.array([0,1,2,3])
ypoint=np.array([10,20,30,40])
plt.subplot(1,2,2)
plt.plot(xpoint,ypoint)
plt.show()

#==================================================================
#task 1
x=np.array([1,3])
y=np.array([8,10])

plt.plot(x,y, linestyle="dotted")
plt.show()
#====================================================================
#task 2

x=np.array([1,2,6,8])
y=np.array([3,8,1,10])
plt.plot(x,y, linestyle="dotted")
plt.show()
#==============================================================================
#task 3
import seaborn as sns
fmri=sns.load_dataset("C:/Users/khushbu vora/OneDrive/Desktop/mtlpoit/fmri.csv")
print(fmri.head())