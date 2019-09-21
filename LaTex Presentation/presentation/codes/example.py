import numpy as np
import matplotlib.pyplot as plt

a=[]
b=[]

o = np.array([np.cos(np.pi/6),np.sin(np.pi/6)])
O = np.array([0,0])
def line_dir_pt(m,A,k1,k2):
  len =10
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(k1,k2,len)
  for i in range(len):
    temp1 = A + lam_1[i]*m
    x_AB[:,i]= temp1.T
  return x_AB

for y in range(-10,10,1):
    x = y**2/3
    a.append(x)
    b.append(y)

#parameters
V = np.array(([0,0],[0,1]))
u = -0.5*np.array([3,0])
F = 0
#Tangent
omat = np.array([[0,1],[-1,0]])
P = np.array([9,3*np.sqrt(3)])
Q = np.array([(21/2),0])
S = np.array([(3/4),0])
n = u + V.T@P
m = omat@n

T = line_dir_pt(o,O,-2,15)
N = line_dir_pt(n,P,-2,2)
L = line_dir_pt(Q,S,0,1)
#ploting
plt.plot(P[0],P[1],'o')
plt.plot(Q[0],Q[1],'o')
plt.plot(S[0],S[1],'o')
plt.plot(a,b,label = 'Parabola')
plt.plot(T[0,:],T[1,:],label = 'Tangent')
plt.plot(N[0,:],N[1,:],label = 'Normal')
plt.plot(L[0,:],L[1,:],label = 'SQ')
plt.text(Q[0] * (1 - 0.2), Q[1] * (1 + 0.2) , 'Q')
plt.text(P[0] * (1 - 0.2), P[1] * (1 + 0.2) , 'P')
plt.text(S[0] * (3), S[1] * (1) , 'S')

plt.xlabel('$x$');plt.ylabel('$y$')
plt.legend(loc='best');plt.grid()
plt.axis('equal')

plt.show()

print('P is ',P)
print('Q is ',Q)
print('S is ',S)

d1 =Q-S
c =np.array([1,0])
d =d1@c.T
print('Distance of SQ is',d)
