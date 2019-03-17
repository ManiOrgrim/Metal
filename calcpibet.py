import numpy as np

def createx (n):
   x=np.empty(n)
   for i in range (0, n):
      x[i]=np.random.rand()*2-1
   return x

def createy (n):
   y=np.empty(n)
   for i in range (0,n):
      y[i]=np.random.rand()*2-1
   return y

def square (x, y):
   c=x**2+y**2
   return c[c<1]
a=square(createx(20),createy(20))
print (a)


