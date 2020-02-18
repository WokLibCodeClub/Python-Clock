### Draw ticks at all the seconds positions

Hopefully you've now got one short tick at the 12 o'clock position. But we want **60** ticks this size. You probably realise this is going to need a loop - in fact it's a **repeat 60 times** loop.

At this point we need to make a very slight change to the size of the circle around the clock. If the thickness of the circle is large the circle will obscure part of the tick marks, so we will make the circle slightly bigger to avoid this problem. **Change** the line of code which draws the circle to this:
```
grid_turtle.circle(clock_radius + circle_thick*clock_radius/2)
```

Now back to the **repeat 60 times** loop.

The loop will work like this:

1. Send the turtle to middle of the clock pointing upwards
2. Rotate the turtle by an angle clockwise
3. Send turtle towards the edge of the clock on the new heading with pen up
4. Put the pen down and draw the tick
5. Return the turtle to the middle of the clock
6. REPEAT steps 2, 3, 4, and 5 until all the ticks are drawn.

In Python the way to make a loop which repeats a set number of times is this:
```
for i in range(n):
```
where ```n``` is the number of times the loop repeats.

For the seconds ticks we want the loop to repeat 60 times, but we have a variable called ```num_ticks``` which is already set to 60 so instead of putting the number 60 inside the brackets we'll put the variable name.

We have already written the code to do all these operations for one tick mark, so all we need to do is rearrange these lines of code so that some of them are inside the loop and some of them are outside, and we also have to add one extra line inside the loop which will rotate the turtle.

**_Before the loop starts_** we want the lines of code which set the four variables (```tick_len```, ```tick_thick``` etc), **AND** the code which sets the pensize, pencolor, sends turtle home, sets heading to 0 and puts the pen up.

**_THEN_** we start the loop with the line
```
for i in range(num_ticks):
```
**_THEN_** as the first line *inside* the loop we need to rotate the turtle with

```
    grid_turtle.right(?)
```
Note how this line is *indented*. All the other lines of code *inside* the loop must also be indented.

**BUT** there's another question mark inside the brackets. How many degrees will the turtle have to turn between one tick and the next?

You can get Python to work this out using a formula. Think which variable contains the number of ticks we want, think how many degrees there are in a circle, and compose a formula to go in the brackets which will use these two values.

After the command to turn the turtle right you can use the same five lines of code you've already written to draw the ticks, but **remember to indent it**.




[Continue to next section *Draw all the different size ticks*](README5.md)

[Go back to previous page](README2.md)