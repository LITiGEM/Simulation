import numpy as np

#--------------------------------------------------------
# Object
#--------------------------------------------------------

class Agent:

    def __init__(self, A,B,C,D,E):
        self.none = A
        self.one = B
        self.two= C
        self.three= D
        self.four= E

#--------------------------------------------------------
# Defining functions
#--------------------------------------------------------

def GenProb(numParam):

    probArray = np.random.rand(1,numParam)

    return probArray

def GenAgent(numAgent):

    agentArray = []

    for num in range(numAgent):

        instance = GenProb(5)

        agentArray.append(Agent(instance[0][0] , instance[0][1] , instance[0][2], instance[0][3], instance[0][4]))

    print(agentArray[99].one) #we use [] to call a particular array (as now we are generating 100 agents

    return agentArray

def NewGrid(length,height):

    M=np.zeros(length,height)

    return display(M)












#--------------------------------------------------------
# Running simulation
#--------------------------------------------------------




agentArray = GenAgent(100)

