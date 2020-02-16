# Designing your own clock background

We took our clock background from a rather small image copied from the internet.

What if we wanted a much bigger clock, or a clock with different style lettering? We could use a turtle to draw our own clock face, then put the clock hands we've already coded on top of this. There are three steps in these instructions for making the background, but, of course, you can choose which ones you want to use for your own clock:

1. Draw a circle around the outside of the clock
2. Draw all the different size tick marks round the outside
3. Draw the numbers

We will create a new turtle to do all this drawing. In this example the turtle is called ```grid_turtle```. We don't actually want to see this turtle, only the results of the drawing, so we can hide the turtle. When the turtle is created we will set the pen to penup so the turtle won't start drawing until we tell it. Here are three lines of code to do these things:

Place these lines of code _**after**_ the code that creates the other turtles, but put them _**before**_ the statement ```tracer(0)```

```
grid_turtle = Turtle()
grid_turtle.hideturtle()
grid_turtle.penup()
```

Since we are going to create our own clock background we should delete the turtle background:
### **DELETE THESE LINES:**
```
clock_image = "blank_clock.gif"
screen.register_shape(clock_image)
screen.bgpic(clock_image)
```

## 1. Draw a circle around the outside of the clock

To make sure the clock background appears **underneath** the clock hands we need to draw the background _**before**_ doing anything with the hands.

We can make the turtle draw a circle with the code ```grid_turtle.circle(******)``` where we need to put the radius of the circle in pixels inside the brackets. The clock background image we used before was 551x551 pixels in size, and the clock hands have been drawn to fit this size. So the radius of the circle should be around half this. You can experiment with this.

We are going to use the radius in all the steps of drawing the clock background.  To make our code easy to change (if we want to make the clock bigger or smaller) _**put your chosen value of the radius in a variable**_. Then we can easily use the circle radius in other bits of the code. We have called the variable ```clock_radius```.

When the turtle draws the circle it will start and finish at the rightmost point of the circle, so before drawing we need to move the turtle to this point. 

We also want to set a colour for the circle. There are a lot of turtle colours ready for use in Python and we have already used "red" and "black" in the code. Some of the other colours available are: "white", "gray", "lightgray", "green", "lightgreen", "blue", "cyan", "yellow", "magenta", "gold", "orange", "maroon", "violet", "purple", "navy", "skyblue", "turquoise", "darkgreen", "chocolate", "brown". The turtle colour is set with ```grid_turtle.color(****)``` with the colour, including quote marks, inside the brackets.

The turtle will initially be set with a pen width of 1, which will produce a very thin line - only one pixel wide. The outline of the clock will need to be thicker. You can set it to any number using ```grid_turtle.pensize(***)``` where you put your pensize in the brackets. Experiment to find the best thickness.

Before drawing the circle we need to put the pen down.

Here are the lines of code to draw the circle. You will need to fill in the question marks. Use the information above to help, and don't worry if it doesn't work exactly first time.

Insert these lines _**above**_ the ```while True:``` loop.

```
grid_turtle.goto(?,?)
grid_turtle.color(?)
grid_turtle.pensize(?)
grid_turtle.pendown()
grid_turtle.circle(clock_radius)
```

Run the code - you should see your circle with the hands moving inside it. Adjust the parameters to get the circle just right.

[Continue to *2. Draw all the different size tick marks round the outside*](README2.md)