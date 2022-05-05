import plotly,matplotlib, random, time, sys
import plotly.graph_objs as go

class die:
    '''class representing a die'''
    def __init__(self, num_sides=6):
        '''default is 6 sides'''
        self.num_sides=num_sides

    def roll(self):
        '''simulates a roll'''
        return random.randint(1, self.num_sides)
    
die_1=die()
die_2=die()

#sets number of rolls and maximum result
num_rolls = 1020
maxResult = die_1.num_sides+die_2.num_sides

#creates a list of die rolls
resultsComp = [die_1.roll()+die_2.roll() for x in range(num_rolls)]
#counts the number of times a result appears
freqComp = [resultsComp.count(x) for x in range(2,maxResult+1)]

#plots the frequency of all rolls as a histogram
x_values = [x for x in range(2,maxResult+1)]
data = [go.Bar(x=x_values, y=freqComp)]
x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = go.Layout(title=f'Results of rolling one D6 {num_rolls} times',
 xaxis=x_axis_config, yaxis=y_axis_config)
plotly.offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')

