# Designing your own clock background (continued)

## 2. Scale the clock hands to the size of clock

The clock radius of your new customised clock is ... whatever number you put in the variable ```clock_radius```.

But when you were designing your clock hands you would have been using a different sized clock, based on the background image (551 pixels acrosss for the *standalone Python installation* instructions, and 400 pixels across for the *trinket* instructions).

To make the clock hands grow or shrink in the right proportion to fit the customised clock we need to scale the clock hand turtles by an amount calculated by the Python formula ```clock_radius/275```. Luckily there is a turtle command to do exactly this.

Look in the code for your second hand turtle you should have a line of code which says
```
second_hand.shape("second hand")
```
Immediately after this line put two new lines:
```
second_hand.resizemode("user")
second_hand.shapesize(clock_radius/275, clock_radius/275)
```
These lines will scale the second hand turtle by a factor ```clock_radius/275``` in the x and y directions.

Now add the same two lines in the same place for the minute and hour hand turtles, but remember to change the name ```second_hand``` to the name of the turtle for the minute or hour hand.

Rerun your code and you should now see that the hands are the right size for the clock circle.

To test this is working try changing the value of ```clock_radius``` at the top of your code. Do the circle and the hands change size together?

[Continue to *3. Draw tick marks round the outside*](README2.md)

[Go back to previous page](README.md)
