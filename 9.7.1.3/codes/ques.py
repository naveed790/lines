import numpy as np
import matplotlib.pyplot as plt
def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB
omat = np.array([[0,1],[-1,0]]) 
#Sides
a = 4
c = 3
b=np.sqrt(a**2+c**2)
print(b)
#Triangle vertices
O = np.array([0,0]) 
A = np.array([0,-a]) 
D = np.array([-c,-a])
B = np.array([0,a]) 
C = np.array([c,a])

#Generating all lines
x_OA = line_gen(O,A)
x_AD = line_gen(A,D)
x_DO = line_gen(D,O)
x_OB = line_gen(O,B)
x_OC = line_gen(O,C)
x_BC = line_gen(B,C)
#Plotting all lines
plt.plot(x_OA[0,:],x_OA[1,:],label='$OA$')
plt.plot(x_AD[0,:],x_AD[1,:],label='$AD$')
plt.plot(x_DO[0,:],x_DO[1,:],label='$DO$')
plt.plot(x_OB[0,:],x_OB[1,:],label='$OB$')
plt.plot(x_OC[0,:],x_OC[1,:],label='$OC$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.03), A[1] * (1 - 0.1) , 'A(0,-4)')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 +0.03), B[1] * (1) , 'B(0,4)')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.03), C[1] * (1 - 0.1) , 'C(3,4)')
plt.plot(O[0], O[1], 'o')
plt.text(O[0] * (1 + 0.03), O[1] * (1 - 0.1) , 'O(0,0)')
plt.plot(D[0], D[1], 'o')
plt.text(D[0] * (1 -0.15), D[1] * (1 - 0.03) , 'D(-3,-4)')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.show()
