# Making the minute and hour hands

To make the minute and hour hands we will need to design shapes for these hands, using x and y coordinates to specify the corners.

Here is code to make a sample minute hand, using a turtle which we will call minute_hand and a shape called "minute hand":
```
screen.register_shape("minute hand", ((-20,-15), (20,-15), (25,190), (-25, 190)))
minute_hand = Turtle()
minute_hand.color("black")
minute_hand.shape("minute hand")
```
If you add this code just after the code which makes the second hand and run it you should see that your clock has a moving second hand and a very ugly, oversized minute hand.

Change the coordinates in the ```screen.register_shape()``` line of code to make a better shape. To understand what the coordinates mean look at this picture of the clock with the x and y coordinates marked. You need to select x and y values of corner points to make a thinner, more elegant minute hand.

![Clock with grid](clock_grid.gif "Clock with x and y coordinate grid") 

Once you have a nice-looking minute hand you can use very similar code to make an hour hand:

```
screen.register_shape("hour hand", (your list of coordinates for the hour hand in the brackets))
hour_hand = Turtle()
hour_hand.color("black")
hour_hand.shape("hour hand")
```

**IF YOU COPY THIS CODE** - make sure you add in your coordinates for the hour hand before you try to run it.

[Continue to Step 6 - Making the minute and hour hands move](../Step6-Making-the-hands-move)



