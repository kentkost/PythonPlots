import plotly.offline as py
import plotly.graph_objs as go


#note. remove boundary line to have perfect color. But maybe put in markers
#https://plot.ly/python/filled-area-plots/

trace0 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[0, 2, 3, 5],
    fill='tozeroy',
    name="trace0",
    opacity=0,
)
trace1 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[3, 5, 1, 7],
    fill='tonexty', #['none', 'tozeroy', 'tozerox', 'tonexty', 'tonextx','toself', 'tonext']
    name="trace1",
    marker = dict(
        color = 'rgb(17, 157, 255)',
        size = 120,
        line = dict(
          color = 'rgb(231, 99, 250)',
          width = 12
        )
      ),
    line = dict(
        color = ('rgb(205, 12, 24)'),
        width = 4),
    opacity=1
)

layout = go.Layout(
    title='Plot Title',
    xaxis=dict(
        title='x Axis',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    ),
    yaxis=dict(
        title='y Axis',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    )
)



data = [trace0, trace1]
fig = go.Figure(data=data, layout=layout)
py.plot(fig, filename='basic-area.html')