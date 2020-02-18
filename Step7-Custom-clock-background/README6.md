## 3. Draw the numbers

Our clock is almost complete. The only remaining task is to draw the numbers.

We can do this using another loop - a repeat 12 times loop.

Just after the code which calls the function to draw the ticks add this line:
```
for i in range(12):
```

You might wonder what the ```i``` means in this line. This is another Python variable, and each time the loop runs the variable ```i``` increases by 1, so it's 0 the first time through the loop, 1 the second time, 2 the third time, up to 11 for the last time.

We can use the value of ```i``` in this loop to write the clock numbers, using the ```turtle.write()``` function.

Before we start the loop we'll get the turtle to the middle of the clock and pointing upwards. We can also choose a colour for the numbers. Put these lines before the line which starts the loop:
```
grid_turtle.goto(0,0)
grid_turtle.setheading(0)
grid_turtle.color(*****) # put your chosen colour, including quote marks, inside the brackets
```

Inside the loop we need to do these operations
1. turn the turtle to the right
2. move out towards the edge of the clock
3. write the number
4. move the turtle back to the middle.

For step 1 we need to turn the turtle by the number of degrees between one number and the next. You can get Python to work this out with a formula.

For the distance to move in step 2 we will use a fraction multiplied by the clock radius - you should experiment to get the best value. Somewhere between 0.7 and 0.9 works well.

For step 3 we need to be clever - the first time through the loop the variable i has a value 0, but we want to write the number 1; the second time i has the value 1 but we want to write the number 2. Think of a simple Python formula for this line.

Here is the code to go inside the loop **which must be indented**. You have to work out what goes in place of the question marks.
```
    grid_turtle.right(?)
    grid_turtle.forward(? * clock_radius)
    grid_turtle.write(?)
    grid_turtle.goto(0,0)
```

When you have worked out the values run the code. You might find the numbers are much too small. We can change the size, and also the font, and the alignment, by rewriting the third line (putting your formula instead of the question mark)
```
    grid_turtle.write(?, font=("Comic Sans MS", int(clock_radius/font_factor), "normal"), align = "center" )

```
In this example the font has been changed to Comic Sans, and the font size has been tied to the clock radius - so if you make the clock bigger the font will get bigger as well. If you find the numbers are the wrong size you can change the value 5 in this line of code to get your preferred size.

**This code will now generate an error**, because we have introduced a new variable ```font_factor``` before telling Python what its value is. So we need to add a line of code outside the loop to define the variable  ```font_factor```. Add this line just after the code the draw the ticks:
```
font_factor = 6
```
You can experiment with the value of font_factor if your text is too big or too small. Which way do you think you should change it to make the font bigger?

BUT - the numbers are all too far up. We can correct this by altering the y coordinate of the turtle's location before and inside the loop. Again, it is smart to tie this shift to the clock radius to make it easy to adjust the clock size.

Change the two lines that set the turtle position (one before the loop and one inside it) to:
```
grid_turtle.goto(0, -clock_radius/font_factor*0.9)
```

This is the last stage. You should now have a customised clock which keeps proper time. If you want to make it bigger or smaller you should only have to change the value of the variable ```clock_radius```. Try that now, and see if it works.

Congratulations on your clock!


[Go back to previous page](README5.md)