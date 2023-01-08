Oh dear, when the turtle updates the time it writes the new time over the top of the previous time.

To correct this we need to clear the text each time we update it. There is a turtle function called ```clear()``` which does this, so add this line just before the ```t.write()``` line in the ```while True:``` loop:

```python
  t.clear()
```

There is one more thing which we should change to make a good digital clock. When the clock ticks over to the next minute the number of seconds is less than 10 so only uses a single digit. This makes all the other numbers shift over.

We need a way to fill the number of seconds with an extra zero, so that the number of seconds shows as 01, 02, 03 instead of 1, 2, 3. We can do this with a string method called ```.zfill(2)``` added on to the end of the ```str(S)``` part of the ```write()``` function. This will add zeros to make sure the number of seconds always shows with two digits. We can do the same to the minutes and the hours.

The finished write function will look like this:

```python
    t.write(str(H).zfill(2) + ":" + str(M).zfill(2) + ":" + str(S).zfill(2),
            font=("Arial", 96, "normal"), align = "center")
```

If you wanted a different colour text you could change the colour of the turtle. If you wanted the text to be red, for example, you would do this by adding the code

```python
t.color("red")
```

This line needs to go after the line ```t = Turtle()``` that *creates* the turtle - near the beginning of the code.

You should now have a functioning Digital Clock. You could experiment with changing the font, or trying italics to get a display you like.

The next section shows how to create an Analogue clock. Lucklily we can use a lot of the same code for the Analogue clock.

[Go to Step 3 - Setting up the Analogue clock](../Step3-Setting-up-the-Analogue-clock)

[Go back to previous page](README3.md)