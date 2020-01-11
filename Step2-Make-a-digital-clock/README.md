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

### Special Note if you are writing your code with the *Visual Studio Code* editor:

With Visual Studio Code you will find that the Turtle window opens and closes again immediately, so you don't have a chance to see what is in the window. To stop this happening you need to add a line at the *bottom* of your code which says
```
mainloop()
```
This will keep the turtle window open. Make sure this line is always the *last* line in your code - don't put any lines of code after this.

If you are using the IDLE editor _*YOU DO NOT NEED THIS LINE OF CODE*_.

The turtle will automatically be in the middle of the screen so that's where the time will be displayed. We get the turtle to display text using the turtle ```write()``` function and put whatever we want to display inside the brackets. But *there is a problem* - which is that the turtle ```write()``` function will only display a string of text, and the variables containing the hours, minutes and seconds are *numerical*. So, before we can use them for our digital clock, we need to convert these variables into string variables.

## Do you remember how to do this?

Try and work it out before looking at the answer.

[Go to answer](README2.md)