


We are going to code these ticks in Python using the ```grid_turtle``` turtle to draw them.
What information do we need to draw the exact type of ticks we want? Here are suggestions:
- tick length
- tick colour
- tick thickness
- how many ticks round the circle
- how big the circle is

That should cover everything.

We can define our function 


Put the function _**after**_ the code which creates the turtles, but _**before**_ the line ```tracer(0)```.

To avoid duplicating the code we will write a **function** to draw a general type of tick and use the same function with different parameters for our different types of ticks.

We can write the code for each type of tick separately but that would mean duplicating a lot of code, which is the worst thing a coder can do.