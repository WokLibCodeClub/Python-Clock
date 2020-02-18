## 2. Scale the clock hands to the size of clock

When we made the clock hands we used a clock background which was 551 pixels across. So the clock radius was 275 pixels (actually it was 275.5 to be exact, but you can't have decimals of pixels).

The clock radius of your new customised clock is ... whatever number you put in the variable ```clock_radius```.

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

This is the last stage. You should now have a customised clock which keeps proper time. If you want to make it bigger or smaller you should only have to change the value of the variable ```clock_radius```. Try that now, and see if it works.

Congratulations on your clock!

[Go back to previous page](README6.md)