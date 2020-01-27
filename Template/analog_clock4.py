# Import statements to use parts of other Python modules
from datetime import datetime
from time import sleep
from turtle import *

# Use a variable to define the Turtle window
screen = Screen()
# Define the size of the screen
setup(600,600)

# Define a variable for the name of the blank clock image
clock_image = "blank_clock.gif"
# Register the blank clock image for use by Turtle window
screen.register_shape(clock_image)

# Set the screen background to the blank clock image
screen.bgpic(clock_image)

# Set the turtle angles so that 0 degrees points upwards
# and the degrees increase clockwise
mode("logo")

# Declare the turtle to use for the minute hand
minute_hand = Turtle()
minute_hand.color("black")
screen.register_shape("minute hand", ((-5,-12), (5,-12), (1,225), (-1, 225)))
minute_hand.shape("minute hand")

# Declare the turtle to use for the hour hand
hour_hand = Turtle()
hour_hand.color("black")
screen.register_shape("hour hand", ((-6,-10), (6,-10), (1,120), (-1, 120)))
hour_hand.shape("hour hand")

# Declare the turtle to use for the second hand
second_hand = Turtle()
second_hand.color("red")
screen.register_shape("second hand", ((-1,-18), (1,-18), (1,230), (-1, 230)))
second_hand.shape("second hand")

# Insert a command to stop Python drawing the window repeatedly
tracer(0)

# Define a forever loop
while True:
    # Get the time and put the hours, minutes and seconds into variables
    time_now = datetime.now()
    H = time_now.hour
    M = time_now.minute
    S = time_now.second

    # plot the hands, with the correctly computed headings
    second_hand.setheading(S*6)
    minute_hand.setheading((M*60+S)*360/(60*60))
    #hour_hand.setheading((H%12*60*60+M*60+S)*(360/(12*60*60)))
    hour_hand.setheading((H*60*60+M*60+S)*(360/(12*60*60)))

    # redraw the turtle window with the hands in the correct places
    update()
