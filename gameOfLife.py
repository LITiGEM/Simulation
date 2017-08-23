from __future__ import division
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def gameoflit(length, height, bound, unbound, genNum, time_pause);
# initialise the model framework
# height = number of cells along the y-axis
# length = number of cells along x-axis
# gen = the number of generations
# bound = percentage of bound cells (depends on light intensity)
# timePause = time gap between each graph

    M=np.zeros((heigt,lenght)) #Defining the zero matrix

    print(M)


#The whole point of this loop is to generate a random number of cells between zero and 1
   for i in range(1,length)
       for j in range(1, height)
           if random.random(0,bound) #generate a random number whose value is less than or equal to the number of bound cells
               A=array([[i],[j]])
               A=1

#Error catching
    if bound >1 or unbound >1
        print ("Enter percentage value between 0 and 1");

#Creating a grid on python
grids= [[0]*gridSize for _ in range (height, length)];

print (grid)

#How do we make a grid as a figure?


#Defining the placeholders for plotting the time course data

snapshot=[];
cellCount=[];
counter=0;

#Defining the neighbours only horizontally and vertically

def init_grid(self, array):
    for i in range(self.rows):
        single_row = []
        for j in range(self.cols):
            if (i == 0 or j == 0 or (i == self.rows - 1) or (j == self.cols - 1)):
                single_row.append(-1)
            else:
                ran = random.randint(0, 3)
                if ran == 0:
                    single_row.append(1)
                else:
                    single_row.append(0)
        array.append(single_row)








