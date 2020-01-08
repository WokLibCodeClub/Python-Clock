# Making a Digital Clock

#### At this point it's a good idea to start a new .py file for your code. Use File SaveAs to save your code with a new name, for example **digital-clock.py**

We are going to use Python Turtles to show the time in large letters, so we need to import the turtle module. Under the line of code which imports the ```datetime``` module add the code:
```
from turtle import *
```

We will also be using the Python ```sleep()``` function which is in the ```time``` module, so we need to import this:
```
from time import sleep
```
For the digital clock we will use the turtle ```write()``` function to display the time in the middle of the turtle window. To do this we need to create a turtle object. This code creates a turtle called ```t``` but you can call your turtle whatever you like:
```
t = Turtle()
```

We are using the turtle to write the time, but we don't actually want to see the turtle, so we can hide it:
```
t.hideturtle()
```

The turtle will automatically be in the middle of the screen so that's where the time will be displayed. We get the turtle to display text using the turtle ```write()``` function with whatever we want to display inside the brackets. But *there is a problem* - which is that the turtle will only display a string, and the variables containing the hours, minutes and seconds are *numerical*. So, before we can use them for our digital clock, we need to convert these variables into string variables.

## Do you remember how to do this?

Try and work it out before looking below.



































If you have the hour in a variable called ```H```, the minutes in a variable called ```M``` and the seconds in a variable called ```S``` then you could write the time on the screen using
```
t.write(str(H)+str(M)+str(S))
```

Try this and see what happens by saving your code and running it.

[Go to step 3](../Step3-Analogue-clock-second hand)

