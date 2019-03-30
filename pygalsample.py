import pygal
from pygal.style import Style
custom_style = Style(
  colors=('#E80080', '#404040', '#9BC850'))

b_chart = pygal.Bar(style=custom_style)
b_chart.title = "Destiny Kill/Death Ratio"
b_chart.add("Dijiphos", [0.94])
b_chart.add("Punisherdonk", [1.05])
b_chart.add("Musclemuffins20", [1.10])
b_chart.render_to_file('pygalsample.html')