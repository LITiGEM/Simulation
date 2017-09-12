from SALib.sample import saltelli
from SALib.analyze import sobol
import numpy as np

b_array=[]

def sensitivity(km,v):

    P=6.1564400012e-06
    n=(1-((0.99553156316)/((6.48 * 10 ** -6))))
    b=(P / (P + km)) * n * v
    b_array.append(b)

    return b

problem={
    'num_vars':2,
    'names': ['km','v'],
    'bounds': [[0,10],[5000,10000]]
}

#Generate samples
param_values=saltelli.sample(problem,1000,calc_second_order=False)

#Run Model
Y=sensitivity(param_values)

#Perform analysis

Si=sobol.analyze(problem,Y,print_to_console=True)


