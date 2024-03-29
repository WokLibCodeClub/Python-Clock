Oh dear, when the turtle updates the time it writes the new time over the top of the previous time and creates a horrible mess.

To correct this we need to clear the text each time we update it. There is a turtle function called ```clear()``` which does this, so add this line just before the ```t.write()``` line in the ```while True:``` loop:

```python
  t.clear()
```

There is one more thing which we should change to make a good digital clock. When the clock ticks over to the next minute the number of seconds is less than 10 and displays using only a single digit. This makes all the other numbers shift over. (The same thing happens with the minutes when we tick over to a new hour or the hours when we tick over to a new day.)

We need a way to **fill** the number of seconds/minutes/hours with an extra zero, so that the number shows as 01, 02, 03 instead of 1, 2, 3. We can do this with a string method called ```zfill()```. Add the code ```.zfill(2)``` to the end of the three ```str()``` parts of the ```write()``` command. This will add additional zeros to make sure the number of seconds or minutes or hours always shows with two digits:

```python
    t.write(str(H).zfill(2) + ":" + str(M).zfill(2) + ":" + str(S).zfill(2),
            font=("Arial", 96, "normal"), align = "center")
```

This line of code has become quite long and might run off the edge of your editor. Luckily where Python code has a comma you can hit the *Enter* key to start a new line straight after the comma and the code will still run as normal.

If you would like a different colour text you could change the *colour* of the turtle. If you wanted the text to be red, for example, you would add the code

```python
t.color("red")
```

after the line ```t = Turtle()``` that *creates* the turtle - near the beginning of the code.

**Note:** we have to use the American spelling *color*.

You should now have a functioning Digital Clock. You could experiment with changing the font, or trying italics to get a display you like.

The next section shows how to create an Analogue clock. Lucklily we can use a lot of the same code for the Analogue clock.

[Go to Step 3 - Setting up the Analogue clock](../Step3-Setting-up-the-Analogue-clock)

[Go back to previous page](README3.md)