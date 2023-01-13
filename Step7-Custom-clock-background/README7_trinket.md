# Designing your own clock background (continued)

## 2. Scale the clock hands to the size of clock using trinket

The clock radius of your new customised clock is ... whatever number you put in the variable ```clock_radius```.

But when you were designing your clock hands you would have been using a different sized clock 400 pixels across, based on the size of the background image. This means your clock hands may not look right with the new clock size.

To make the clock hands grow or shrink in the right proportion to fit the customised clock we need to scale the clock hand turtle shapes up or down. The trinket starter project for the analogue clock has an extra file included which contains a scaling function, to do exactly this.

First we need to add an extra line to the import section of the code - at the very beginning. After the line which imports the turtle library add

```python
from scaler import scale_hands
```

Now we need to rewrite a couple of lines of code for each of the clock's hands, adding a call to the function called scale_hands. Here is a sample section of code for the minute hand ***before*** changing the code (you may have slightly different numbers for your shape coordinates):

```python
s.register_shape("minute hand", ((-3,-11), (3,-11), (1,160), (-1, 160)))
minute_hand = Turtle()
minute_hand.color("black")
minute_hand.shape("minute hand")
```

Here is the same section of code ***after*** making the change:

```python
minute_shape = scale_hands(((-3,-11), (3,-11), (1,160), (-1, 160)), clock_radius)
s.register_shape("minute hand", minute_shape)
minute_hand = Turtle()
minute_hand.color("black")
minute_hand.shape("minute hand")
```

We have made a new variable called ```minute_shape``` and moved the set of coordinates into the first line. Then, in the second line we have replaced the list of coordinates by the new variable. When you run the code you should see your minute hand has been resized to fit the clock radius you are now using.

You now need to make the same change for the hour and second hands (but, of course, the coordinate numbers will be different, and you should alter the name of the new variable for these hands).

Rerun your code and you should now see that all the hands are the right size for the clock circle.

To test this is working try changing the value of ```clock_radius``` at the top of your code. Do the circle and the hands change size together?

[Continue to *3. Draw tick marks round the outside*](README2.md)

[Go back to previous page](README.md)
