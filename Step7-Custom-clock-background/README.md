# Designing your own clock background

We took our clock background from a rather small image copied from the internet.

What if we wanted a much bigger clock, or a clock with different style lettering? We could use a turtle to draw our own clock face, then put the clock hands we've already coded on top of this. There are four steps in these instructions for making the background, but, of course, the choice is up to you which ones you want to use for your own clock:

1. Draw a circle around the outside of the clock
2. Scale the clock hands to the size of clock
3. Draw all the different size tick marks round the outside
4. Draw the numbers

## Saving your code with a new name

If you have a properly working clock using the image background it would be a shame to risk losing that by changing the code to make a customised clock, so at this stage it would be a good idea to save the clock code with a new name.

_If you are using a **standalone Python installation**_ then go to File>Save As and save the code with a new name - for example - **custom-analogue-clock.py**. If you do all your customising in the new file you will still have the code for the working clock in the old file.

_If you are using a **trinket**_ then Copy your code and change the name of the copied project.

## Set the clock size

The first step is to decide how big you want your clock to be. 

- _If you are using a **standalone Python installation**_ the biggest clock you can make will  depend on the size in pixels of your screen.

   Click [here](SCREENSIZE.md) to see how to find out your screen size if you are using Windows.

   The smaller number of the two screen size dimensions will give you the largest clock you can display on your screen. You probably need to limit the size to a bit less than this to leave room for the border and the Windows taskbar. On my screen the size is 1920 x 1080, so I would make my biggest clock diameter 900.

- _If you are using a **trinket**_ the size of clock will be limited by the size of the graphics area on the trinket page in your web browser. On most web browsers a clock diameter of 400-500 is about the biggest you can use

We will put our chosen clock size a variable called ```clock_radius``` and this should go at the top of the code, just underneath all the ```import``` instructions. Be careful here - if your clock is going to be 900 pixels across, then this is the clock's *diameter*. The radius is half that. For this example to make a clock 800 pixels across, we add this line just under the ```import``` lines:

```
clock_radius = 400
```

Now we need to make sure the turtle window is big enough to show the clock which we will do by changing the line of code which sets the turtle window size. We know we want the window to be twice the clock radius across, and we probably need to add a little bit extra for a border. We can use a clever bit of Python which will automatically calculate the window size based on our clock radius.

Change the line of code with the setup parameters:

- _standalone Python installation_:

```python
setup(clock_radius * 2.2, clock_radius * 2.2)
```

- _trinket_:

```python
s.setup(clock_radius * 2.2, clock_radius * 2.2)
```

## Make a new turtle to draw the background

We will create a new turtle to do all the background drawing. In this example the turtle is called ```grid_turtle```. We don't actually want to see this turtle, only the results of the drawing, so we can hide the turtle. When the turtle is created we will set the pen to penup so the turtle won't start drawing until we tell it. Here are three lines of code to do these things:

Place these lines of code _**just after**_ the code that creates the other turtles:

```python
grid_turtle = Turtle()
grid_turtle.hideturtle()
grid_turtle.penup()
```

Since we are going to create our own clock background we should delete the existing code which sets the screen background.

**DELETE THESE LINES:**

```python
clock_image = "blank_clock.gif"
screen.register_shape(clock_image)
screen.bgpic(clock_image)
```
(In trinket the word ```screen``` will be replaced by the letter ```s```.)

## 1. Draw a circle around the outside of the clock

To make sure the clock background appears **underneath** the clock hands we need to draw the background _**before**_ doing anything with the hands.

We can make the turtle draw a circle with the code ```grid_turtle.circle(******)``` where we need to put the radius of the circle in pixels inside the brackets. Luckily we have a variable ```clock_radius``` which contains the radius of the clock, so we can use this variable in the ```circle()``` instruction.

We also want to set a colour for the circle. There are a lot of turtle colours ready for use in Python and we have already used ```"red"``` and ```"black"``` in the code. Some of the other colours available are: ```"white", "gray", "lightgray", "green", "lightgreen", "blue", "cyan", "yellow", "magenta", "gold", "orange", "maroon", "violet", "purple", "navy", "skyblue", "turquoise", "darkgreen", "chocolate", "brown"```. The turtle colour is set with ```grid_turtle.color(****)``` with the colour, _including quote marks_, inside the brackets.

The turtle will initially be set with a pen width of 1, which will produce a very thin line - only one pixel wide. The outline of the clock will need to be thicker. You can set it to any number using ```grid_turtle.pensize(***)``` where you put your pen thickness in pixels in the brackets. Start with a thickness of, say, 3 or 4 and adjust it as you like.

When the turtle draws the circle it will start and finish at the rightmost point of the circle, so before drawing we need to move the turtle to this point.

_Before_ drawing the circle we need to put the pen down. _After_ drawing the circle we will put the pen up, to stop it drawing.

Here are the lines of code to draw the circle. You will need to fill in the question marks. Use the information above to help, and don't worry if it doesn't work exactly first time.

Insert these lines _**after**_ the ```grid_turtle.penup()``` line.

```python
grid_turtle.color(?)
grid_turtle.pensize(?)

grid_turtle.goto(?,?)
grid_turtle.pendown()
grid_turtle.circle(clock_radius)
grid_turtle.penup()
```

**Important**: if you are using *trinket* you need to add an extra line of code just before ```grid_turtle.goto```:

```python
grid_turtle.setheading(90)
```

Run the code - you should now see a circle around the clock, and the hands moving inside it.

The hands may not be the right size for your circle, but don't worry about that - we'll fix it in the next step. Adjust the circle parameters to get the appearance of the circle just right.

[Continue to _2. Scale the clock hands to the size of clock_](README7.md)

[Go back to previous page if you are coding with a standalone Python installation](../Step6-Making-the-hands-move)

[Go back to previous page if you are using trinket](../Step6-Making-the-hands-move/README_trinket.md)
