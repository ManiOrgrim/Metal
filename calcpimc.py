import numpy as np
import time

N = 100000 # number of MC events
N_run = 100 # number of runs
Nhits = 0.0 # number of points accepted
pi = np.zeros(N_run) # values of pi

start_time = time.time() # start clock 
for I in range(N_run):
    Nhits = 0.0
    for i in range(N):
        x = np.random.rand()*2-1
        y = np.random.rand()*2-1
        res = x*x + y*y
        if res < 1:
            Nhits += 1.0
    pi[I] += 4. * Nhits/N

run_time = time.time()

print("pi with ", N, " steps for ", N_run, " runs is ", np.mean(pi), " in ", run_time-start_time, " sec")
print("Precision computation : ", np.abs(np.mean(pi)-np.pi))
