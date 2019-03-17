import numpy as np
import time

start_time=time.time()

def createx (n):
   x=np.empty(n)
   for i in range (0, n):
      x[i]=np.random.rand()
   return x*2-1

def square_and_returnN (x, y):
   c=x*x+y*y
   return (len(c[c<1]))


def algo (N):
   n=10000000
   tomean=np.empty(N)
   for i in range (0, N):
      tomean[i]=square_and_returnN(createx(n),createx(n))
      print("Sono al ", i*100/N, "%")
   return 4*np.mean(tomean)/n
   

#print(algo())   
#print (4*square_and_returnN(createx(1000),createy(1000)))
N=1000
pi=algo(N)
print("pi is ", pi, " in ", time.time()-start_time, "sec with precision ", np.abs(pi-np.pi))


