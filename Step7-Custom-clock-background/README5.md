### Draw all the different size ticks

We've written code, including a loop, to draw 60 short, thin tick marks. So all we need to do to get the 12 medium tick marks and the 4 short, fat tick marks is copy the same code but change some of the values, right?

#### **WRONG!**

This would mean duplicating code and duplicating code is one thing a Python coder should **never** do.

Instead we're going to use a clever Python technique to reuse code, with different values, without the need to retype anything. We're going to make a general purpose tick-drawing *function*.

We need a name for the function, so in this example the function is called ```draw_ticks```. The way to define a function is with a line of code like this: ```def draw_ticks():``` then, as you can probably guess, all the lines of code which are part of the function are *indented*.

Many Python functions just have empty brackets in the definition line, but for this function we'll do something different. The function definition line will go just after the turtle has finished drawing the circle. Add this line of code:
```
def draw_ticks(tick_len, tick_thick, tick_col, num_ticks):
```

then indent all the lines of code down as far as (but not including) the ```while True:``` loop.

Then **DELETE** these lines, (but, first, make a note of what values you set the variables to).
```
tick_len = ? # the fraction of the circle radius to use for the tick length. You could try 0.05 to start with.
tick_thick = ? # the fraction of the circle radius to use for the tick thickness. You could try 0.005 to start with.
tick_col = *** # choose your preferred colour for the ticks - don't forget the quote marks
num_ticks = 60 # this is the number of ticks - it's 60 for all the seconds positions
```
You will see that some lines of code have been indented **twice** - this is because they are inside the function but also inside the repeat loop.

Now that we've put the tick drawing code inside a function the code will no longer work. So to draw the ticks we add one line of code just above the ```while True:``` loop. The line of code is:
```
draw_ticks(?, ?, ?, ?)
```

What goes in place of the question marks? Well, for the first question mark put whatever value you chose for the variable ```tick_len```; for the second question mark whatever value you chose for ```tick_thick```; for the third question mark put your chosen tick colour - *including quote marks*; and for the fourth question mark put the value of ```num_ticks```, which at the moment is 60.

Save the code and run it. The clock should look exactly as it did before. The line we've just composed **calls** the function, and at the same time passes the chosen values of the variables to the function, which then draws the ticks.

But now, if I wanted to draw 12 medium length ticks I would simply repeat the line
```
draw_ticks(?, ?, ?, ?)
```
and replace the question marks with my chosen values for medium ticks - slightly longer and slightly fatter, maybe in a different colour, and now with the fourth question mark replaced by 12, which is the number of medium ticks. The function will do all the calculations and draw the new style ticks. Try that now.

And if I wanted four long fat ticks I would repeat the line again with different values, and the number 4 in place of the last question mark.

Neat!

Experiment with the lengths, thicknesses and colours of the types of ticks to get a really cool clock.

[Continue to next section *4. Draw the numbers*](README6.md)

[Go back to previous page](README4.md)