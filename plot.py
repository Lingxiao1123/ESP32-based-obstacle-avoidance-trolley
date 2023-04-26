from ORGHCSR04_ULTR import ORGHCSR04_ULTR
from time import sleep
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initialize the ultrasonic sensors
Ultr1 = ORGHCSR04_ULTR(25, 26)  # front ultrasonic sensor
Ultr2 = ORGHCSR04_ULTR(4, 36)  # left ultrasonic sensor
Ultr3 = ORGHCSR04_ULTR(12, 34)  # right ultrasonic sensor

# Define a function to update the plot in real-time
def update_plot(frame):
    # Get the distance readings from the ultrasonic sensors
    dist1 = Ultr1.start_scan()
    dist2 = Ultr2.start_scan()
    dist3 = Ultr3.start_scan()

    # Clear the previous plot
    plt.clf()

    # Plot the distance readings in subplots
    plt.subplot(3, 1, 1)
    plt.ylim(0, 100)  # set y-axis limit
    plt.plot(dist1, 'b-')
    plt.title('Front Ultrasonic Sensor')

    plt.subplot(3, 1, 2)
    plt.ylim(0, 100)  # set y-axis limit
    plt.plot(dist2, 'r-')
    plt.title('Left Ultrasonic Sensor')

    plt.subplot(3, 1, 3)
    plt.ylim(0, 100)  # set y-axis limit
    plt.plot(dist3, 'g-')
    plt.title('Right Ultrasonic Sensor')

# Create a new figure
fig = plt.figure()

# Animate the plot
ani = animation.FuncAnimation(fig, update_plot, interval=100)

# Show the plot
plt.show()
