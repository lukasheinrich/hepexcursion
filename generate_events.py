import random
import numpy as np
import time

def generator():
    while True:
        yield random.random()

def evgen_single_point(x,nevents = 10000):
    #generate n events and fill "histo"
    p = m1,m2 = x
    thresh = (1+np.tanh(m1-m2))/2.
    accepted_events = []
    for i,rn in enumerate(generator()):
        if i==nevents:
            break
        time.sleep(0.001)
        rnd = random.random()
        if rnd < thresh:
            accepted_events.append(1)
    return np.sum(accepted_events)

