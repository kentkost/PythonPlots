import plotly.offline as py
import plotly.graph_objs as go
import random

from collections import namedtuple

#note. remove boundary line to have perfect color. But maybe put in markers
#https://plot.ly/python/filled-area-plots/

class TestDay():
    def __init__(self):
        self.passes = 0
        self.fails = 0
        self.skips = 0
    def __str__(self):
        return "passes: "+str(self.passes) +" fails: "+ str(self.fails) +" skips: "+ str(self.skips)

class Tests():
    def __init__(self):
        self.dates = []
        self.values =[]

def CreateData():
    startDate = 28
    allTests = {} #Referenced by the keys in the variable tests
    tests = ["passed", "fail", "skip"]
    colors = ['rgb(0,255,0)','rgb(255,0,0)','rgb(0,0,255)']
    traces = []
    dates = CreateDates(startDate)

    for i in range(0, len(tests)):
        allTests[tests[i]] = []

    for i in range(0, len(dates)):
        #temp = CreateTestDayData(random.randint(1100, 1700))
        temp = CreateTestDayData(1700)
        for j in range(0, len(tests)):
            allTests[tests[j]].append(temp[j])
    
    for i in range(0, len(tests)):
        temp = CreateTrace1(dates,allTests[tests[i]], tests[i], colors[i])
        traces.append(temp)

    return traces

def CreateTrace0(xValues, yValues, nameValue):
    trace = go.Scatter(
        x=xValues,
        y=yValues,
        fill='tozeroy',
        name=nameValue,
        opacity=0,
    )
    return trace

def CreateTrace1(xValues, yValues, nameValue, colorValue):
    trace = dict(
        x=xValues,
        y=yValues,
        name = nameValue,
        hoverinfo='x+y',
        mode='none', #line, none
        stackgroup='one',
        marker = dict(
            color = colorValue,
            size = 120,
            # line = dict(
            #   color = colorValue,
            #   width = 12
            # )
        ),
        # line = dict(
        #     color = colorValue,
        #     width = 4),
        opacity=1
    )
    return trace

def CreateDates(date):
    dates = []
    for i in range(0, 10):
        y = ''
        y += '2019/'+str(date-i)+'/03'
        dates.append(y)
    return dates

def CreateTestDayData(numberOfTests):
    p = random.randint(0, numberOfTests)
    s = random.randint(0, numberOfTests-p)
    f = numberOfTests - p -s
    return [p, s, f]

def MakeGraph():
    #Class of trace?
    #initialize with
    # trace0 = go.Scatter(
    #     x=[1, 2, 3, 4],
    #     y=[0, 2, 3, 5],
    #     fill='tozeroy',
    #     name="trace0",
    #     opacity=0,
    # )
    # trace1 = go.Scatter(
    #     x=[1, 2, 3, 4],
    #     y=[3, 5, 1, 7],
    #     fill='tonexty', #['none', 'tozeroy', 'tozerox', 'tonexty', 'tonextx','toself', 'tonext']
    #     name="trace1",
    #     marker = dict(
    #         color = 'rgb(17, 157, 255)',
    #         size = 120,
    #         line = dict(
    #           color = 'rgb(231, 99, 250)',
    #           width = 12
    #         )
    #     ),
    #     line = dict(
    #         color = ('rgb(205, 12, 24)'),
    #         width = 4),
    #     opacity=1
    # )

    layout = go.Layout(
        title='Test from to',
        xaxis=dict(
            title='Dates',
            titlefont=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            )
        ),
        yaxis=dict(
            title='Number of Tests',
            titlefont=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            )
        )
    )

    #data = [trace0, trace1]
    data = CreateData()
    fig = go.Figure(data=data, layout=layout)
    py.plot(fig, filename='basic-area.html')

def main():
    #CreateData()
    MakeGraph()
  
if __name__== "__main__":
    main()