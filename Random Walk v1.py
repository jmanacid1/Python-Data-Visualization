import matplotlib.pyplot as plt
import matplotlib.cm as cm
import random



#Random Walk Time

class RandomWalk:
    '''simulates a random walk'''
    def __init__(self, numPoints=100):
        self.numPoints = numPoints
        self.xList = [0]
        self.yList = [0]

    def getStep(self):
        Dir = random.choice([-1,1])
        Dis = random.choice([0,1,2,3,4,5,6])
        Step = Dir * Dis
        return Step
        

    def genXYCoords(self):
        while len(self.xList)<self.numPoints:

            xStep = self.getStep()
            yStep = self.getStep()

            if xStep==0 and yStep == 0:
                continue

            x = self.xList[-1]+xStep
            y = self.yList[-1]+yStep
            
            self.xList.append(x)
            self.yList.append(y)
        return self.xList,self.yList


randWalk = RandomWalk(10000)

#scatter plots

'''
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(*randWalk.genXYCoords(), c=randWalk.yList, cmap=plt.cm.Blues,s=15)
ax.scatter(0,0,c='red',s=50)
ax.scatter(randWalk.xList[-1], randWalk.yList[-1], c='green',s=50)
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
'''


#line graph
fig, ax = plt.subplots()
ax.axis([-500,500,-500,500])
ax.plot(*randWalk.genXYCoords(),linewidth=1,c='red')


plt.show()
