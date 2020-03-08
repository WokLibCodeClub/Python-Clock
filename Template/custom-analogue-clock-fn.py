from datetime import datetime
from turtle import *
from time import sleep

#######################################################################
# SET CLOCK RADIUS
#######################################################################
clock_radius = 400

#######################################################################
# SETUP SCREEN
#######################################################################
screen = Screen()
setup(clock_radius * 2.2, clock_radius * 2.2)

mode("logo")

#######################################################################
# CREATE TURTLES
#######################################################################
screen.register_shape("minute hand", ((-5,-12), (5,-12), (1,225), (-1, 225)))
minute_hand = Turtle()
minute_hand.color("black")
minute_hand.shape("minute hand")
minute_hand.resizemode("user")
minute_hand.shapesize(clock_radius/275, clock_radius/275)

screen.register_shape("hour hand", ((-6,-10), (6,-10), (1,120), (-1, 120)))
hour_hand = Turtle()
hour_hand.color("black")
hour_hand.shape("hour hand")
hour_hand.resizemode("user")
hour_hand.shapesize(clock_radius/275, clock_radius/275)

second_hand = Turtle()
second_hand.color("red")
screen.register_shape("second hand", ((-1,-4), (1,-4), (1,230), (-1, 230)))
second_hand.shape("second hand")
second_hand.resizemode("user")
second_hand.shapesize(clock_radius/275, clock_radius/275)

grid_turtle = Turtle()
grid_turtle.hideturtle()
grid_turtle.penup()

tracer(0)

#######################################################################
# DRAW CLOCK CIRCLE
#######################################################################
circle_thick = 0.03

grid_turtle.color("orange")
grid_turtle.pensize(clock_radius * circle_thick)

grid_turtle.goto(clock_radius + circle_thick*clock_radius/2, 0)
grid_turtle.pendown()
grid_turtle.circle(clock_radius + circle_thick*clock_radius/2)
grid_turtle.penup()

#######################################################################
# DEFINE FUNCTION TO DRAW TICK MARKS
#######################################################################
def draw_ticks(tick_len, tick_thick, tick_col, num_ticks):
    grid_turtle.pensize(tick_thick * clock_radius) # this sets the pen thickness as a fraction of the clock radius
    grid_turtle.pencolor(tick_col) # this sets the turtle's colour to your choice
    grid_turtle.goto(0,0) # this sends the turtle to the middle of the clock
    grid_turtle.setheading(0) # this makes sure the turtle is pointing up
    grid_turtle.penup() # this makes sure the turtle won't start drawing yet

    for i in range(num_ticks):
        grid_turtle.right(360/num_ticks)
        #print(grid_turtle.heading())
        grid_turtle.forward((1-tick_len)*clock_radius) # this moves the turtle towards the edge of the clock
        grid_turtle.pendown() # this gets the turtle ready for drawing
        grid_turtle.forward(tick_len * clock_radius) # you must give the turtle for formula for how far to move
        grid_turtle.penup()
        grid_turtle.goto(0,0) # send the turtle back to the middle of the clock

#######################################################################
# CALL FUNCTION TO DRAW TICK MARKS
#######################################################################
draw_ticks(0.03, 0.004, "chocolate", 60)
draw_ticks(0.06, 0.008, "blue", 12)
draw_ticks(0.08, 0.012, "yellow", 4)

#######################################################################
# DRAW CLOCK NUMBERS
#######################################################################
numb_len = 0.82
font_factor = 7
grid_turtle.goto(0, -clock_radius/font_factor*0.9)
grid_turtle.setheading(0)
grid_turtle.color("black")

for i in range(12):
    grid_turtle.right(360/12)
    grid_turtle.forward(numb_len * clock_radius)
    #grid_turtle.setheading(0)
    grid_turtle.write(i+1, font=("Comic Sans MS", int(clock_radius/font_factor), "normal"), align = "center" )
    grid_turtle.goto(0, -clock_radius/font_factor*0.9)


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
