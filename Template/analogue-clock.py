from datetime import datetime
from turtle import *
from time import sleep

######################################################################
# SETUP SCREEN
#######################################################################
screen = Screen()
setup(600,600)
clock_image = "blank_clock.gif"
screen.register_shape(clock_image)
screen.bgpic(clock_image)

mode("logo")

#######################################################################
# CREATE TURTLES
#######################################################################
screen.register_shape("minute hand", ((-5,-12), (5,-12), (1,225), (-1, 225)))
minute_hand = Turtle()
minute_hand.color("black")
minute_hand.shape("minute hand")

screen.register_shape("hour hand", ((-6,-10), (6,-10), (1,120), (-1, 120)))
hour_hand = Turtle()
hour_hand.color("black")
hour_hand.shape("hour hand")

second_hand = Turtle()
second_hand.color("red")
screen.register_shape("second hand", ((-1,-4), (1,-4), (1,230), (-1, 230)))
second_hand.shape("second hand")

tracer(0)

#######################################################################
# MAIN PROGRAMME LOOP
#######################################################################
while True:
    # get time
    time_now = datetime.now()
    # put hours, minutes and seconds in variables
    H = time_now.hour
    M = time_now.minute
    S = time_now.second

    # compute direction for each hand
    minute_hand.setheading(360/3600*(60*M + S))
    hour_hand.setheading(360/(60*60*12)*(3600*H + 60 * M + S))
    second_hand.setheading(S*6)

    # redraw the clock
    update()
