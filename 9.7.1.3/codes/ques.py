import math
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as  LA
import subprocess
import shlex


#A=r*np.array(([np.cos(theta),np.sin(theta)]))
k = 1
c = 5
a = 4
theta = np.arctan(c/a)
O = np.sqrt(c**2+a**2)*np.array(([np.cos(theta),np.sin(theta)]))
print(O)
D = np.array(([0,0]))
e1 = np.array(([1,0]))
A=a*e1
print(A)
B=np.array(([a,2*c]))
C=np.array(([2*a,2*c]))
#e1=np.array(([1,0]))
#D=np.array(([-4,-3]))
#O=(A+B)/2


#generating a line
def line_gen(A,B):
    len=10
    dim = A.shape[0]
    x_AB = np.zeros((dim,len))
    lam_1 = np.linspace(0,1,len)
    for i in range(len):
        temp1 = A + lam_1[i]*(B-A)
        x_AB[:,i] = temp1.T
    return x_AB
#generating all lines
X_OA=line_gen(O,A)
X_OB=line_gen(O,B)
X_OD=line_gen(O,D)
X_OC=line_gen(O,C)
X_AD=line_gen(A,D)
X_BC=line_gen(B,C)

#plotting all lines
plt.plot(X_OA[0,:],X_OA[1,:])
plt.plot(X_OB[0,:],X_OB[1,:])
plt.plot(X_OD[0,:],X_OD[1,:])
plt.plot(X_OC[0,:],X_OC[1,:])
plt.plot(X_AD[0,:],X_AD[1,:])
plt.plot(X_BC[0,:],X_BC[1,:])



#Labeling the coordinates
tri_coords =np.vstack((B,C,D,A,O)).T

plt.scatter(tri_coords[0,:],tri_coords[1,:])
vert_labels = ['B','C','D','A','O']
for i,txt in enumerate(vert_labels):
  plt.annotate(txt,      (tri_coords[0,i],tri_coords[1,i]),
      textcoords="offset points",      xytext=(0,10),
      ha='center')
plt.xlabel('$X$')
plt.ylabel('$Y$')
plt.grid()
plt.axis('equal')
plt.show()


#plt.savefig('/sdcard/FWCmodule1/line/output.pdf')
