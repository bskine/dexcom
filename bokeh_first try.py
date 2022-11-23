import averages

from bokeh.io import output_file
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
from bokeh.layouts import row, column, gridplot
import bokeh.models.widgets

x = [averages.glucose_current()[0],
     averages.glucose_average_1hour()[0],
     averages.glucose_average_3hour()[0],
     averages.glucose_average_6hour()[0],
     averages.glucose_average_12hour()[0],
     averages.glucose_average_24hour()[0]]

top = [averages.glucose_current()[1],
       averages.glucose_average_1hour()[1],
       averages.glucose_average_3hour()[1],
       averages.glucose_average_6hour()[1],
       averages.glucose_average_12hour()[1],
       averages.glucose_average_24hour()[1]]

output_file('average_bar_graph.html', title='Average Blood Glucose')

fig = figure(title='CURRENT AND AVERAGE BLOOD GLUCOSE',
             height=500, width=500,
             x_range=(0, 24), y_range=(50, 200),
             # x_axis_type='log',
             x_axis_location='below',
             x_axis_label='hourly average',
             y_axis_label='mg/dl'
             )

fig.vbar(x, top=top,
         color='blue',
         width=0.75
         )

show(fig)