# Making a Digital Clock

If you are using a Python editor on your computer it's a good idea to start a new .py file for your code. Use File SaveAs to save your code with a new name, for example **digital-clock.py**

If you are using trinket you can ignore this step.

---

We are going to use Python Turtles to show the time in large letters, so we need to import the turtle module. Under the line of code which imports the ```datetime``` module add the code:

```python
from turtle import *
```

We will also be using the Python ```sleep()``` function which is in the ```time``` module, so we need to import this:

```python
from time import sleep
```

For the digital clock we will use the turtle ```write()``` function to display the time in the middle of the turtle window. To do this we need to create a turtle object. This code creates a turtle called ```t``` but you can call your turtle whatever you like. Put this line near the top of the code, just underneath all the ```import``` statements:

```python
t = Turtle()
```

We are using the turtle to write the time, but we don't actually want to see the turtle, so we can hide it. Put this line immediately after the ```t=Turtle()``` line:

```python
t.hideturtle()
```

---

>### Special Note if you are writing your code with the *Visual Studio Code* editor:
>
>With Visual Studio Code you will find that the Turtle window opens and closes again immediately, so you don't have a chance to see what is in the window. To stop this happening you need to add a line at the *bottom* of your code which says
>
>```python
>mainloop()
>```
>
>This will keep the turtle window open. Make sure this line is always the *last* line in your code - don't put any lines of code after this.
>
>If you are using the IDLE editor or coding using trinket _*YOU DO NOT NEED THIS LINE OF CODE*_.

---

We will get the turtle to display the time using the turtle ```write()``` function. This is like the ```print()``` function and will cause text to appear in the turtle window. The text will be whatever you put inside the brackets.

The turtle will automatically be in the middle of the screen so that's where the time will be displayed.

A common way of displaying the time is using the hours, minutes and seconds separated by a colon (:) symbol. So here is how the time 12 seconds and 33 minutes past 2 in the afternoon would be displayed:

14:33:12

We can make up a text string for the turtle to write, using the variables ```H```, ```M``` and ```S```, which contain the values of the hours, minutes and seconds of the time now. So we might try adding this line at the end of the code, *after* the lines which set the variables:

```python
t.write(H + ":" + M + ":" + S)
```

Add this line, save your code then run it.

Oh, no! It gave an error. This is because we have tried to mix text (the colon symbols) with variables which are *numerical*. Just like the ```print()``` function you can't do this with a turtle ```write()``` function. What we need to do is convert the numerical variables into strings.
 
## Do you remember how to do this?

Try and work it out, and correct your code, before looking at the answer.

<details><summary>Answer</summary>

To convert a numerical variable to a string variable use the ```str()``` function.

To have a turtle **write** several numerical variables, one after the other, convert them all to strings and place a ```+``` sign in between each inside the brackets of the ```write()``` function.

Try this in your code before continuing.

</details>

<p>

[Continue](README3.md)

[Go back to previous page](../Step1-Whats_the_time/README.md)