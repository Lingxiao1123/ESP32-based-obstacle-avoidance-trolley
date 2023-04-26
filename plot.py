from ORGHCSR04_ULTR import ORGHCSR04_ULTR
from bokeh.layouts import column
from bokeh.models import ColumnDataSource
from bokeh.plotting import curdoc, figure

# Initialize the ultrasonic sensors
Ultr1 = ORGHCSR04_ULTR(25, 26)  # front ultrasonic sensor
Ultr2 = ORGHCSR04_ULTR(4, 36)  # left ultrasonic sensor
Ultr3 = ORGHCSR04_ULTR(12, 34)  # right ultrasonic sensor

# Create a data source for the distance readings
source1 = ColumnDataSource(dict(x=[0], y=[0]))
source2 = ColumnDataSource(dict(x=[0], y=[0]))
source3 = ColumnDataSource(dict(x=[0], y=[0]))

# Create a figure with three subplots
fig1 = figure(title='Front Ultrasonic Sensor', x_axis_label='Time', y_axis_label='Distance (cm)')
fig1.line('x', 'y', source=source1, line_color='blue')
fig2 = figure(title='Left Ultrasonic Sensor', x_axis_label='Time', y_axis_label='Distance (cm)')
fig2.line('x', 'y', source=source2, line_color='red')
fig3 = figure(title='Right Ultrasonic Sensor', x_axis_label='Time', y_axis_label='Distance (cm)')
fig3.line('x', 'y', source=source3, line_color='green')

# Put the subplots in a column layout
layout = column(fig1, fig2, fig3)

# Define a function to update the plot in real-time
def update():
    # Get the distance readings from the ultrasonic sensors
    dist1 = Ultr1.start_scan()
    dist2 = Ultr2.start_scan()
    dist3 = Ultr3.start_scan()

    # Update the data source with the new distance readings
    new_data1 = dict(x=[i for i in range(len(dist1))], y=dist1)
    new_data2 = dict(x=[i for i in range(len(dist2))], y=dist2)
    new_data3 = dict(x=[i for i in range(len(dist3))], y=dist3)
    source1.stream(new_data1)
    source2.stream(new_data2)
    source3.stream(new_data3)

# Add the update function to the document's callback list
curdoc().add_periodic_callback(update, 100)

# Set the document title and add the layout to the document
curdoc().title = "Ultrasonic Sensor Readings"
curdoc().add_root(layout)
