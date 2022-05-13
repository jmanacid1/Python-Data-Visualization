import matplotlib.pyplot as plt
import matplotlib.cm as cm
import random



#Random Walk Time

class RandomWalk:
    '''simulates a random walk'''
    def __init__(self, numPoints=100):
        self.numPoints = numPoints

    xList = [0]
    yList = [0]

    def genXCoords(self):
        xList = [0]
        for i in range(self.numPoints):
            xList.append(xList[-1]+random.randint(-1,1))
        return xList
    def genYCoords(self):
        yList = [0]
        for i in range(self.numPoints):
            yList.append(yList[-1]+random.randiSnt(-1,1))
        return yList

randWalk = RandomWalk(100)
#ax.scatter(randWalk.genCoords(),[x for x in range(11)])
#plt.show

values = range(1,1001)
cubes = [x**2 for x in values]
plt.style.use('seaborn')

print()
fig, ax = plt.subplots()  # Create a figure containing a single axes.

ax.scatter(randWalk.genXCoords,randWalk.genYCoords)
