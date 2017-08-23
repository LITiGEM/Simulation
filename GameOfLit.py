from scipy.integrate import odeint
import numpy as np


def gameOfLit( length, height, bound, unbound, genNum,time_pause):
    #initialise the model framework
    height = 50 #number of cells along the y axis
    length = 50 #number of cells along x axis
    genNUm = 20 #the number of generations
    bound =  c #percentage of bound cells
    unbound = d #percentage of unbound cells
    time_Pause = 0.05 #time gap between each graph

    #initialise the zero matrix
    M= np.zeros(length, height)

    # generate random number between 0 and 1
    if  c > 1:
        print ('percentage needs to be between 0 and 1')
    else:
        print
        if d> 1:
            print ('percentage needs to be between 0 and 1')
        else:
            print

            d= 1-bound

    #random numbers are smaller than bound
    import random

    my_list = []

    for c,d in range(0, 1):
        my_list.append(c)
        if c <= bound:
            my_list.append(c)

    print my_list
    print 'Random (sort of) choice: %s' % random.choice(my_list)








