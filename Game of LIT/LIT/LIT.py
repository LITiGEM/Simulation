import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.colors as mlpCol
import time

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

#A RulSet refers to the probabilities of a cell changing state depending on the number of its neighbours
class RuleSet:
    def __init__(self, neighbNone, neighbOne, neighbTwo, neighbThree, neighbFour):
        self.neighbNone = neighbNone
        self.neighbOne = neighbOne
        self.neighbTwo = neighbTwo
        self.neighbThree = neighbThree
        self.neighbFour = neighbFour

#--------------------------------------------------------
# Defining functions
#--------------------------------------------------------

def GenProb(numParam):

    probArray = np.random.rand(1, numParam)
    # 1 dimensional array

    return probArray

def GenSetAgent(numAgent, A, B, C, D, E):

    agentArray = []

    for num in range(numAgent):

        agentArray.append(Agent(A, B, C, D, E))

    return agentArray

def GenRandAgent(numAgent):

    agentArray = []

    for num in range(numAgent):

        instance = GenProb(5)

        agentArray.append(Agent(instance[0][0] , instance[0][1] , instance[0][2], instance[0][3], instance[0][4]))

    return agentArray

def NewGrid(length,height):
    #generate a new grid with a specifed length and height

    grid = np.zeros((length,height))

    return grid

def PlaceCells(grid, agent, cellNum):

    #Getting dimensions of the grid
    dimensions = grid.shape

    rowMax = dimensions[0]
    colMax = dimensions[1]

    #Getting the agents to place the cells in the grid
    counter = 0
    
    while counter < cellNum:
        sample = [divmod(i, rowMax) for i in random.sample(range(colMax * rowMax), 1)] #Pick a random point on the grid

        sampleRow = sample[0][0]
        sampleCol = sample[0][1]

        #setting parameters
        try:
            top=grid[sampleRow+1][sampleCol]
        except:
            #if the value is out of bound set top to zero (if you can't run it give it a zero value)
            top = np.float64(0)

        try:
            down = grid[sampleRow -1][sampleCol]
        except:
            # if the value is out of bound set top to zero
            down = np.float64(0)

        try:
            forward = grid[sampleRow ][sampleCol+1]

        except:
            # if the value is out of bound set top to zero
            forward = np.float64(0)

        try:
            backward = grid[sampleRow][sampleCol-1]
        except:
            # if the value is out of bound set top to zero
            backward = np.float64(0)

        envState = down + top + backward + forward

        changeChance = np.float64(0)

        if envState == 0:
            changeChance = agent.none
        elif envState == 1:
            changeChance= agent.one
        elif envState == 2:
            changeChance = agent.two
        elif envState == 3:
            changeChance = agent.three
        elif envState == 4:
            changeChance= agent.four


        if np.random.rand() <= changeChance:
            grid[sampleRow][sampleCol] = np.float64(1)

            counter = counter + 1

        #print(counter)
        #print("cell added")

    newGrid = grid
    return newGrid

def DrawGrid(grid):

    dimensions = grid.shape

    maxRow = dimensions[0]
    maxCol = dimensions[1]


    # I do 1. because it has to be float, we need to normalise the color map
    norm = mlpCol.Normalize(vmin=0.,vmax=1.)

    # tell imshow about color map so that only set colors are used
    img = plt.imshow(grid,interpolation='nearest',cmap=None,norm=norm)

    # make a color bar
    plt.colorbar(img, cmap=None, norm=norm)

    plt.xticks([])
    plt.yticks([])

    plt.show()

def RunGame(grid, genNum, ruleSet):

    # Getting the agents to place the cells in the grid
    counter = 0

    dimensions = grid.shape

    rowMax = dimensions[0]
    colMax = dimensions[1]

    while counter < genNum:

        for i in range(0,rowMax):
            for j in range(0,colMax):
                sampleRow = i
                sampleCol = j

                # setting parameters
                try:
                    top = grid[sampleRow + 1][sampleCol]
                except:
                    # if the value is out of bound set top to zero (if you can't run it give it a zero value)
                    top = np.float64(0)

                try:
                    down = grid[sampleRow - 1][sampleCol]
                except:
                    # if the value is out of bound set top to zero
                    down = np.float64(0)

                try:
                    forward = grid[sampleRow][sampleCol + 1]

                except:
                    # if the value is out of bound set top to zero
                    forward = np.float64(0)

                try:
                    backward = grid[sampleRow][sampleCol - 1]
                except:
                    # if the value is out of bound set top to zero
                    backward = np.float64(0)

                envState = down + top + backward + forward

                changeChance = np.float64(0)

                if envState == 0:
                    changeChance = ruleSet.neighbNone
                elif envState == 1:
                    changeChance = ruleSet.neighbOne
                elif envState == 2:
                    changeChance = ruleSet.neighbTwo
                elif envState == 3:
                    changeChance = ruleSet.neighbThree
                elif envState == 4:
                    changeChance = ruleSet.neighbFour

                if np.random.rand() <= changeChance:
                    grid[sampleRow][sampleCol] = np.float64(1)

                    counter = counter + 1

                    # print(counter)
                    # print("cell added")


    newGrid = grid

    return newGrid

def FindCoverTime(agent, grid, ruleSet):

    dimensions = grid.shape
    maxRow = dimensions[0]
    maxCol = dimensions[1]

    totalCell = maxRow*maxCol

    genNum = 0
    currentGrid = grid
    DrawGrid(grid)
    while currentGrid.sum() < totalCell:
        currentGrid = RunGame(currentGrid, genNum, ruleSet)
        genNum = genNum + 1


    return genNum



def FindBestAgent(agentArray, grid, ruleSet):

    #initiating the variables to return, those values do not matter
    emptyGrid = grid
    bestAgent = agentArray[0]
    bestGenNum = 0

    # find the number of generation needed to cover the grid for each agents
    for agent in agentArray:
        zeroGrid = NewGrid(50, 50)
        initialGrid = PlaceCells(zeroGrid, agent, 12) #Needs to change to be agent specific

        genNum = FindCoverTime(agent, initialGrid, ruleSet)

        if bestGenNum < genNum:
            bestGenNum = genNum
            bestAgent = agent

    return bestAgent, bestGenNum

#--------------------------------------------------------
# Running simulation
#--------------------------------------------------------

if __name__ == "__main__":
    agentArray = GenRandAgent(10)

    GenSetAgent(100, 0.7, 0.5, 0.6, 0.3, 0.2)

    grid = NewGrid(50,50)

    updateGrid = PlaceCells(grid, agentArray[0], 12)

    ruleSet = RuleSet(0.2, 0.3, 0.4, 0.5, 0.6)

    finalGrid = RunGame(updateGrid,2000,ruleSet)


    #reinitialise empty grid
    zeroGrid = NewGrid(50,50)
    #DrawGrid(zeroGrid)
    print("Finding cover time")
    gen = FindCoverTime(agentArray[0],zeroGrid, ruleSet)
    zeroGrid = NewGrid(50,50)

    bestAgent, bestGen = FindBestAgent(agentArray,zeroGrid,ruleSet)

    print(bestGen)
    print("Finding the probabilities/ finding best agent")

    print(bestAgent.none, bestAgent.one, bestAgent.two, bestAgent.three, bestAgent.four)