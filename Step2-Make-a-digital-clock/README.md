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
For the digital clock we will use the turtle ```write()``` function to display the time in the middle of the turtle window. To do this we need to create a turtle object. This code creates a turtle called ```t``` but you can call your turtle whatever you like. Put this line near the top of the code, just underneath all the ```import``` statements:
```
t = Turtle()
```

We are using the turtle to write the time, but we don't actually want to see the turtle, so we can hide it. Put this line immediately after the ```t=Turtle()``` line:
```
t.hideturtle()
```

>### Special Note if you are writing your code with the *Visual Studio Code* editor:
>
>With Visual Studio Code you will find that the Turtle window opens and closes again immediately, so you don't have a chance to see what is in the window. To stop this happening you need to add a line at the *bottom* of your code which says
>```
>mainloop()
>```
>This will keep the turtle window open. Make sure this line is always the *last* line in your code - don't put any lines of code after this.
>
>If you are using the IDLE editor _*YOU DO NOT NEED THIS LINE OF CODE*_.

We will get the turtle to display the time using the turtle ```write()``` function. This is like the ```print()``` function and will cause text to appear in the turtle window. The text will be whatever you put inside the brackets. 

The turtle will automatically be in the middle of the screen so that's where the time will be displayed. 

A common way of displaying the time is using the hours, minutes and seconds separated by a colon (:) symbol. So here is how the time 12 seconds and 33 minutes past 2 in the afternoon would be displayed:

14:33:12

We can make up a text string for the turtle to write, using the variables ```H```, ```M``` and ```S```, which contain the values of the hours minutes and seconds of the time now. So we might try adding this line at the end of the code, *after* the lines which set the variables:
```
t.write(H + ":" + M + ":" + S)
```

If you add this line, save your code then run it.

But *there is a problem* - which is that the turtle ```write()``` function will only display a string of text, and the variables containing the hours, minutes and seconds are *numerical*. So, before we can use them for our digital clock, we need to convert these variables into string variables.

## Do you remember how to do this?

Try and work it out before looking at the answer.

[Go to answer](README2.md)