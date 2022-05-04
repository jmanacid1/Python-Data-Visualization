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
            yList.append(yList[-1]+random.randint(-1,1))
        return yList
    def genXYCoords(self):
        yList = [0]
        xList = [0]
        for i in range(self.numPoints):
            xList.append(xList[-1]+random.randint(-1,1))
            yList.append(yList[-1]+random.randint(-1,1))
        return xList,yList


randWalk = RandomWalk(100)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(*randWalk.genXYCoords())
plt.show()
