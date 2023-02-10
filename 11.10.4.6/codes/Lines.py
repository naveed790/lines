import matplotlib.pyplot as plt
import numpy as np
import math as ma
from matplotlib import pyplot as plt, patches
import math
import subprocess
import shlex
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)



def line_gen(A,B):
    len=10
    dim = A.shape[0]
    x_AB = np.zeros((dim,len))
    lam_1 = np.linspace(0,1,len)
    for i in range(len):
        temp1 = A + lam_1[i]*(B-A)
        x_AB[:,i] = temp1.T
    return x_AB
    


x = np.linspace(-5,5,100)
y1 = (x/7)+5/7
y2=-3*x
plt.plot(x, y1, '-r', label='line1')
plt.plot(x, y2, '-g', label='line2')
plt.axvline(x=-5/22,color='b',label='parallel line')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='upper left')
plt.grid()                                      
plt.axis('equal')
#if using termux
plt.savefig('/sdcard/download/fwcassgn/trunk/fwcassgn/trunk/naveed/line.png')
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.show()
