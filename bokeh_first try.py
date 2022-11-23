import averages

from bokeh.io import output_file
from bokeh.plotting import figure, show
from bokeh.transform import factor_cmap
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral6
# from bokeh.layouts import row, column, gridplot
# import bokeh.models.widgets

output_file('average_bar_graph.html', title='Average Blood Glucose')

top = [averages.glucose_current()[1],
       averages.glucose_average_1hour()[1],
       averages.glucose_average_3hour()[1],
       averages.glucose_average_6hour()[1],
       averages.glucose_average_12hour()[1],
       averages.glucose_average_24hour()[1]]

tags = ['current', '1Hour', '3hour', '6Hour', '12Hour', '24Hour']
x = [tags[i] for i in range(0, 6)]

source = ColumnDataSource(data=dict(x=x, top=top))

fig = figure(title='CURRENT AND AVERAGE BLOOD GLUCOSE',
             height=500, width=500,
             x_range=x,
             y_range=(0, 300),
             x_axis_location='below',
             x_axis_label='hourly average',
             y_axis_label='mg/dl'
             )

fig.vbar(x, top=top,
         # color='blue',
         fill_color=factor_cmap('x', palette=Spectral6, factors=x),
         width=0.75
         )

show(fig)
