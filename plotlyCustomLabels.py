import plotly.offline as py
import plotly.graph_objs as go

#https://plot.ly/python/text-and-annotations/

#Markers = dots
#lines = is lines
#text is the text
trace1 = go.Scatter(
    x=[0, 1, 2],
    y=[1, 1, 1],
    mode='lines+markers+text',
    name='Lines, Markers and Text',
    text=['Text A', 'Text B', 'Text C'],
    textposition='top center'
)

trace2 = go.Scatter(
    x=[0, 1, 2],
    y=[2, 2, 2],
    mode='markers+text',
    name='Markers and Text',
    text=['Text D', 'Text E', 'Text F'],
    textposition='bottom center'
)

trace3 = go.Scatter(
    x=[0, 1, 2],
    y=[3, 3, 3],
    mode='lines+text',
    name='Lines and Text',
    text=['Text G', 'Text H', 'Text I'],
    textposition='bottom center'
)

trace4 = go.Scatter(
    x=[0, 1, 2],
    y=[4, 4, 4],
    mode='markers+lines',
    name='Markers and Lines',
    text=['Text J', 'Text K', 'Text L'],
    textposition='bottom center'
)

data = [trace1, trace2, trace3, trace4]

#Legend is the informatiion in the righ hand side
layout = go.Layout(
    showlegend=True
)

fig = go.Figure(data=data, layout=layout)
py.plot(fig, filename='text-chart-basic.html')