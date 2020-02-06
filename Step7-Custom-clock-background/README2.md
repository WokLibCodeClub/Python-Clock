## 2. Draw all the different size tick marks round the outside

The image for the clock background showed three different type of tick marks - long fat ticks at 12, 3, 6, and 9; medium length medium thickness marks at all the other numbers and short thin ticks at all the minute positions.

We are going to code these ticks in Python using the ```grid_turtle``` turtle to draw them. We can write the code for each type of tick separately but that would mean duplicating a lot of code, which is the worst thing a coder can do.

To avoid duplicating the code we will write a **function** to draw a general type of tick and use the same function with different parameters for our different types of ticks.

What information do we need to draw the exact type of ticks we want? Here are suggestions:
- tick length
- tick colour
- tick thickness
- how many ticks round the circle


Put the function _**after**_ the code which creates the turtles, but _**before**_ the line ```tracer(0)```.



[Continue to *3. Draw the numbers*](README3.md)

[Go back to previous page](README.md)