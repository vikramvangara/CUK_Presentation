import numpy as np
import matplotlib.pyplot as plt

P = np.array([16,0])

O=np.array([0,0])



len=100
theta=np.loadtxt('./data/theta.dat',dtype='double')

a=np.loadtxt('./data/a.dat',dtype='float')
b=np.loadtxt('./data/b.dat',dtype='float')

a1=np.loadtxt('./data/a1.dat',dtype='float')
b1=np.loadtxt('./data/b1.dat',dtype='float')


A=np.loadtxt('./data/pa.dat',dtype='float')
B=np.loadtxt('./data/pb.dat',dtype='float')
C=np.loadtxt('./data/pc.dat',dtype='float')
D=np.loadtxt('./data/pd.dat',dtype='float')

x1=a*np.cos(theta)
y1=b*np.sin(theta)
x2=a1*np.cos(theta)
y2=b1*np.sin(theta)

plt.plot(x1,y1,'b')
plt.plot(x2,y2,'y')

plt.plot([A[0],B[0]],[A[1],B[1]],'b')
plt.plot([B[0],C[0]],[B[1],C[1]],'b')
plt.plot([C[0],D[0]],[C[1],D[1]],'b')
plt.plot([D[0],A[0]],[D[1],A[1]],'b')
plt.plot([A[0],B[0]],[A[1],B[1]],'o')
plt.plot([B[0],C[0]],[B[1],C[1]],'o')
plt.plot([C[0],D[0]],[C[1],D[1]],'o')
plt.plot([D[0],A[0]],[D[1],A[1]],'o')

plt.plot(O[0],O[1],"o")
plt.text(O[0]*(1+0.1),O[1]*(1-0.1),"O")

plt.plot(P[0],P[1],'o')
plt.text(P[0]*(1),P[1]*(0.8),'P')

plt.title('jee_linalg_2d\nQuestion 36')
plt.grid()
plt.axis('equal')
plt.show()
