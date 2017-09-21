import numpy as np
import random

#--------------------------------------------------------
# Object
#--------------------------------------------------------

class Agent: #defining a new class to provide the standard features, agent is the "player of the Game of Lit"

    def __init__(self, A,B,C,D,E): #function to define the initial conditions of the agents A,B,C,D,E that will be used in the code later for each iteration
        self.none = A
        self.one = B
        self.two= C
        self.three= D
        self.four= E

#--------------------------------------------------------
# Defining functions
#--------------------------------------------------------

def GenProb(numParam): #function for the probability of each generation

    probArray = np.random.rand(1, numParam)

    return probArray #return an array of random variables of shape 1, numParam

def GenAgent(numAgent): #generate an agent given that we have an agent class

    agentArray = []

    for num in range(numAgent):

        instance = GenProb(5)

        agentArray.append(Agent(instance[0][0] , instance[0][1] , instance[0][2], instance[0][3], instance[0][4]))

    print(agentArray[3].three, agentArray[4].one) #we use [] to call a particular array (as now we are generating 100 agents

    return agentArray

def Grid(length,height):

    a=np.zeros(shape=(length,height))


    return a


def FirstState(grid, agent):
    return(agent)


def Simulation(newGrid, numGen):
    return newGrid



#--------------------------------------------------------
# Running simulation
#--------------------------------------------------------
if __name__ == "__main__":

    agentArray = GenAgent(100)
M=Grid (20,20)
N=FirstState(M,3)
