# Designing your own clock background

We took our clock background from a rather small image copied from the internet.

What if we wanted a much bigger clock, or a clock with different style lettering? We could use a turtle to draw our own clock face, then put the clock hands we've already coded on top of this. There are four steps in these instructions for making the background, but, of course, the choice is up to you which ones you want to use for your own clock:

1. Draw a circle around the outside of the clock
2. Draw all the different size tick marks round the outside
3. Draw the numbers
4. Scale the clock hands to the size of clock

### Save your code with a new name

If you have a properly working clock using the image background it would be a shame to risk losing that by changing the code to make a customised clock, so at this stage it would be a good idea to save the clock code with a new name, using Save As - for example - **custom-analogue-clock.py**. If you do all your customising in the new file you will still have the code for the working clock in the old file.

### Set the clock size

The first step is to decide how big you want your clock to be. This will partly depend on the size in pixels of your screen.

Click [here](SCREENSIZE.md) to see how to find out your screen size.

The smaller number of the two screen size dimensions will give you the largest clock you can display on your screen. You probably need to limit the size to a bit less than this to leave room for the border and the Windows taskbar. On my screen the size is 1920 x 1080, so I would make my biggest clocksize 900.

To set the clock size we will make a variable called ```clock_radius``` and this should go at the top of the code, just underneath all the ```import``` instructions. Be careful here - if my clock is going to be 900 pixels across, then this is the clock's *diameter*. The radius is half that. For this example we'll make a clock 800 pixels across, so add this line just under the ```import``` lines:
```
clock_radius = 400
```
Now we need to make sure the turtle window is big enough to show the clock. **_Change_** the ```setup(600, 600)``` instruction so the size is big enough for the clock. If the clock radius is 400, then the turtle window needs to be twice this in both directions. To be safe make the window just a little bit bigger. The setup code should be changed to
```
setup(clock_radius * 2.1, clock_radius * 2.1)
```
This code will adjust the window size to fit the clock radius, so if we change the radius the size of the window will change as well.

### Make a turtle to draw the background

We will create a new turtle to do all the background drawing. In this example the turtle is called ```grid_turtle```. We don't actually want to see this turtle, only the results of the drawing, so we can hide the turtle. When the turtle is created we will set the pen to penup so the turtle won't start drawing until we tell it. Here are three lines of code to do these things:

Place these lines of code _**after**_ the code that creates the other turtles, but put them _**before**_ the statement ```tracer(0)```

```
grid_turtle = Turtle()
grid_turtle.hideturtle()
grid_turtle.penup()
```

Since we are going to create our own clock background we should delete the existing turtle background:
### **DELETE THESE LINES:**
```
clock_image = "blank_clock.gif"
screen.register_shape(clock_image)
screen.bgpic(clock_image)
```

## 1. Draw a circle around the outside of the clock

To make sure the clock background appears **underneath** the clock hands we need to draw the background _**before**_ doing anything with the hands.

We can make the turtle draw a circle with the code ```grid_turtle.circle(******)``` where we need to put the radius of the circle in pixels inside the brackets. Luckily we have a variable ```clock_radius``` which contains the radius of the clock, so we can use this variable in the ```circle()``` instruction.

We also want to set a colour for the circle. There are a lot of turtle colours ready for use in Python and we have already used "red" and "black" in the code. Some of the other colours available are: "white", "gray", "lightgray", "green", "lightgreen", "blue", "cyan", "yellow", "magenta", "gold", "orange", "maroon", "violet", "purple", "navy", "skyblue", "turquoise", "darkgreen", "chocolate", "brown". The turtle colour is set with ```grid_turtle.color(****)``` with the colour, *including quote marks*, inside the brackets.

The turtle will initially be set with a pen width of 1, which will produce a very thin line - only one pixel wide. The outline of the clock will need to be thicker. You can set it to any number using ```grid_turtle.pensize(***)``` where you put your pen thickness in the brackets. 

However, a smarter way to do this is to give the pen thickness as a fraction of the clock radius. Then if you make your clock bigger or smaller the thickness of the circle will change in proportion. 

We can put the circle thickness as a fraction in a variable called ```circle_thick```. Try a value of 0.05 to start with, and experiment to achieve a good look. Then to get the *actual* thickness of the line in pixels  multiply ```circle_thick``` by ```clock_radius```.

When the turtle draws the circle it will start and finish at the rightmost point of the circle, so before drawing we need to move the turtle to this point. 

Before drawing the circle we need to put the pen down. After drawing the circle we will put the pen up, to stop it drawing.

Here are the lines of code to draw the circle. You will need to fill in the question marks. Use the information above to help, and don't worry if it doesn't work exactly first time.

Insert these lines _**above**_ the ```while True:``` loop.

```
circle_thick = 0.05

grid_turtle.color(?)
grid_turtle.pensize(clock_radius * circle_thick)

grid_turtle.goto(?,?)
grid_turtle.pendown()
grid_turtle.circle(clock_radius)
grid_turtle.penup()
```

Run the code - you should now see a circle around the clock, and the hands moving inside it. Adjust the parameters to get the circle just right.

[Continue to *2. Draw all the different size tick marks round the outside*](README2.md)