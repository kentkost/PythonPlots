import plotly.offline as py
import plotly.graph_objs as go
import random

from datetime import datetime, timedelta
from collections import namedtuple

#note. remove boundary line to have perfect color. But maybe put in markers
#https://plot.ly/python/filled-area-plots/

#Creates Faux data to test the plotting methods
def CreateFauxData():
    startDate = 28
    allTests = {} #Referenced by the keys in the variable tests
    tests = ["passed tests", "failed tests", "skipped tests"]
    colors = ['rgb(49,148,50)','rgb(249,66,58)','rgb(52,80,92)'] #Green, Red, Blue
    traces = []
    dates = CreateDates(startDate)
    Data = namedtuple('Data', 'dates, allTests, tests, colors')

    for i in range(0, len(tests)):
        allTests[tests[i]] = []
        allTests['sum'] = [] #used to get the percentage since barplots can't do them.

    for i in range(0, len(dates)):
        #temp = CreateFauxTestDayData(random.randint(1100, 1700))
        temp = CreateFauxTestDayData(1700)
        for j in range(0, len(tests)):
            allTests[tests[j]].append(temp[j])
            allTests['sum'].append(sum(temp))

    return Data(dates, allTests, tests, colors)

def CreateStackedAreaTrace(xValues, yValues, nameValue, colorValue, percent=False):
    trace = dict(
        x=xValues,
        y=yValues,
        text=yValues,
        name = nameValue,
        hoverinfo='x+text+name', #['x', 'y', 'z', 'text', 'name'] 
        mode='lines', #'lines', 'markers', 'text', or none
        stackgroup='one',
        marker = dict(
            color = colorValue,
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
        opacity=0,
    )
    if percent:
        trace['groupnorm'] = 'percent'

    return trace

def CreateBarTrace(xValues, yValues, nameValue, colorValue, textVal):
    trace = go.Bar(
        x=xValues,
        y=yValues,
        text=textVal,
        name = nameValue,
        hoverinfo='x+text+name', #['x', 'y', 'z', 'text', 'name'] 
        marker = dict(
            color = colorValue,
            # line = dict(
            #   color = colorValue,
            #   width = 12
            # )
        ),
    )
    return trace

#Creates dates array to be used in faux data
def CreateDates(date):
    dates = []
    for i in range(0, 10):
        y = ''
        y += '2019/'+str(date-i)+'/03'
        dates.append(y)
    dates.reverse()
    return dates

#Creates faux data for one day of testing
def CreateFauxTestDayData(numberOfTests):
    p = random.randint(0, numberOfTests)
    s = random.randint(0, numberOfTests-p)
    f = numberOfTests - p -s
    return [p, s, f]

def MakeBarGraph(d, percent=False):
    traces = []
    yAxisLabel = 'Number of Tests'
    fileName = 'Tests-Bar.html'

    if percent:
        yAxisLabel = '% of Tests'
        fileName = 'Tests-Bar-Percent.html'
    
    #Make the traces
    for i in range(0, len(d.tests)):
        temp = None
        if percent:
            yValues = NewYvalues(d.allTests[d.tests[i]], d.allTests['sum'])
            temp = CreateBarTrace(d.dates, yValues,d.tests[i],d.colors[i], d.allTests[d.tests[i]])
        else:
            temp = CreateBarTrace(d.dates, d.allTests[d.tests[i]],d.tests[i],d.colors[i], d.allTests[d.tests[i]])
        traces.append(temp)

    layout = CreateLayout('2019/28/03', 'Dates', yAxisLabel, 'stack')
    fig = go.Figure(data=traces, layout=layout)
    py.plot(fig, filename=fileName, auto_open=False)
    #py.plot(fig, filename=fileName, image='svg', auto_open=False)

#New Y-values because stacked bar plot doesn't have an attribute groupnom=percent.
def NewYvalues(yValues, sums):
    newyValues = []
    for i in range(0, len(yValues)):
        newyValues.append((yValues[i] / sums[i])*100)
    return newyValues

def MakeStackedAreaGraph(d, percent=False):
    traces = []
    yAxisLabel = 'Number of Tests'
    fileName = 'Stacked-Area.html'
    if percent:
        yAxisLabel = '% of Tests'
        fileName = 'Stacked-Area-Percent.html'

    for i in range(0, len(d.tests)):
        temp = CreateStackedAreaTrace(d.dates, d.allTests[d.tests[i]],d.tests[i],d.colors[i], percent)
        traces.append(temp)

    layout = CreateLayout('2019/28/03', 'Dates', yAxisLabel)
    fig = go.Figure(data=traces, layout=layout)
    py.plot(fig, filename=fileName, auto_open=False)
    #py.plot(fig, filename=fileName, image='svg', auto_open=False)

def MakeGraphs():
    data = CreateFauxData()
    MakeBarGraph(data, True)
    MakeBarGraph(data, False)
    MakeStackedAreaGraph(data, False)
    MakeStackedAreaGraph(data, True)

#https://plot.ly/python/reference/#layout
#bg: rgb(17,17,17) nuance=160, luminance=16, saturation=0. Colour used to seamlessly colour the background in html. abandoned
def CreateLayout(title, xTitle, yTitle, barmodeVal='', darkTheme=True):
    layout = go.Layout(
        title=dict(
            text=MakeTitle(title, 10),
            x=0.5,
        ),
        hovermode='x',
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
    if barmodeVal != '':
        layout['barmode']=barmodeVal
    if darkTheme:
        layout['template'] = 'plotly_dark'
    return layout

def MakeTitle(date, span):
    toDate = datetime.strptime(date, '%Y/%d/%m').date()
    fromDate = toDate - timedelta(days=span)
    fromDate = fromDate.strftime("%Y/%d/%m")
    return 'Test from '+str(fromDate)+' to '+str(date)


def main():
    #Requirements. Start Date, Span, dark theme
    MakeGraphs()
  
if __name__== "__main__":
    main()