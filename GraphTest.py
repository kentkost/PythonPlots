import plotly.offline as py
import plotly.graph_objs as go
import random

from datetime import datetime, timedelta
from collections import namedtuple

#note. remove boundary line to have perfect color. But maybe put in markers
#https://plot.ly/python/filled-area-plots/

def CreateData():
    startDate = 28
    allTests = {} #Referenced by the keys in the variable tests
    tests = ["passed tests", "failed tests", "skipped tests"]
    colors = ['rgb(0,255,0)','rgb(255,0,0)','rgb(0,0,255)'] #Green, Red, Blue
    traces = []
    dates = CreateDates(startDate)

    for i in range(0, len(tests)):
        allTests[tests[i]] = []

    for i in range(0, len(dates)):
        #temp = CreateTestDayData(random.randint(1100, 1700))
        temp = CreateTestDayData(1700)
        for j in range(0, len(tests)):
            allTests[tests[j]].append(temp[j])
    
    # for i in range(0, len(tests)):
    #     #temp = CreateStackedAreaTrace(dates,allTests[tests[i]], tests[i], colors[i])
    #     temp = CreateStackedAreaPercentTrace(dates,allTests[tests[i]], tests[i], colors[i])
    #     #temp = CreateStackedBarTrace(dates,allTests[tests[i]], tests[i], colors[i])
    #     traces.append(temp)

    #return traces
    return [dates, allTests,tests,colors]

def CreateTrace0(xValues, yValues, nameValue):
    trace = go.Scatter(
        x=xValues,
        y=yValues,
        fill='tozeroy',
        name=nameValue,
        opacity=0,
    )
    return trace

def CreateStackedAreaPercentTrace(xValues, yValues, nameValue, colorValue):
    trace = dict(
        x=xValues,
        y=yValues,
        text=yValues,
        name = nameValue,
        hoverinfo='x+text+name', #['x', 'y', 'z', 'text', 'name'] 
        mode='lines', #'lines', 'markers', 'text', or none
        stackgroup='one',
        marker = dict(
            #color = colorValue,
            #size = 120,
            # line = dict(
            #   color = colorValue,
            #   width = 12
            # )
        ),
        line = dict(
            color = colorValue,
            width = 0,
        ),
        groupnorm='percent',
        opacity=0,
    )
    return trace

def CreateStackedAreaTrace(xValues, yValues, nameValue, colorValue):
    trace = dict(
        x=xValues,
        y=yValues,
        name = nameValue,
        hoverinfo='x+y',
        mode='lines', #'lines', 'markers', 'text', or none
        stackgroup='one',
        marker = dict(
            #color = colorValue,
            #size = 120,
            # line = dict(
            #   color = colorValue,
            #   width = 12
            # )
        ),
        line = dict(
            color = colorValue,
            width = 0),
        groupnorm='percent',
        opacity=0,
    )
    return trace

def CreateStackedBarTrace(xValues, yValues, nameValue, colorValue):
    trace = go.Bar(
        x=xValues,
        y=yValues,
        name = nameValue,
    )
    return trace

def CreateDates(date):
    dates = []
    for i in range(0, 10):
        y = ''
        y += '2019/'+str(date-i)+'/03'
        dates.append(y)
    dates.reverse()
    return dates

def CreateTestDayData(numberOfTests):
    p = random.randint(0, numberOfTests)
    s = random.randint(0, numberOfTests-p)
    f = numberOfTests - p -s
    return [p, s, f]

def MakeBarGraph():
    data = CreateData()
    layout = CreateLayoutBar('2019/28/03', 'Dates', 'Number of Tests')
    fig = go.Figure(data=data, layout=layout)
    py.plot(fig, filename='Tests-Bar.html')

def MakeGraph():
    data = CreateData()
    layout = ''
    fig = go.Figure(data=data, layout=layout)
    py.plot(fig, filename='basic-area.html')

def CreateLayoutBar(title, xTitle, yTitle):
    layout = go.Layout(
        barmode='stack', #Not in a stacked area graph
        title=MakeTitle('2019/28/03', 10),
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
    return layout

def CreateLayoutGraph(title, xTitle, yTitle):
    layout = go.Layout(
        title=MakeTitle(title, 10),
        xaxis=dict(
            title=xTitle,
            titlefont=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            )
        ),
        yaxis=dict(
            title=yTitle,
            titlefont=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            )
        )
    )
    return layout

def MakeTitle(date, span):
    toDate = datetime.strptime(date, '%Y/%d/%m').date()
    fromDate = toDate - timedelta(days=span)
    fromDate = fromDate.strftime("%Y/%d/%m")
    return 'Test from '+str(fromDate)+' to '+str(date)


def main():
    #Requirements. Start Date, Span
    #CreateData()
    MakeBarGraph()
    #MakeGraph()
  
if __name__== "__main__":
    main()