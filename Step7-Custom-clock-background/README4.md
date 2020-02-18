### Draw ticks at all the seconds positions

Hopefully you've now got one short tick at the 12 o'clock position. But we want **60** ticks this size. You probably realise this is going to need a loop - in fact it's a **repeat 60 times** loop.

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

Before we start the loop we need to move the turtle to the middle of the clock and make it point up.

[Continue to next section *Scale the clock hands to the size of clock*](README5.md)

[Go back to previous page](README2.md)