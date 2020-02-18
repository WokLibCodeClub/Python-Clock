# Making the minute and hour hands move

We are going to follow the same steps we used to make the second hand point in the right direction, first for the minute hand, then for the hour hand.

### Setting the direction for the minute hand to point

The first step for the minute hand is to work out how many degrees this hand moves every second.

**Here is a very important point:** Python is really good at doing calculations. So coders *never* have to work out difficult sums - the computer can do that. What the coder has to do is **_work out the right formula_** to give the computer so the computer can calculate the right answer.

To work out the formula for the minute hand we can use these facts:

+ at the beginning of the hour the minute hand points up towards 12 o'clock
+ the minute hand takes exactly one hour to go right round the clock until it's pointing at 12 o'clock again
+ there are 360° in a circle
+ there are 60 seconds in a minute
+ there are 60 minutes in an hour

What is the formula to give Python so Python can calculate **how many degrees the minute hand moves in a second**?

Go [here](README2.md) for a hint.

The second step is to get the minute hand to point in the right direction depending on what the current time is.

In the ```while True:``` loop we already put in the code to get the time now, and put the hours in a variable called ```H```, the minutes in a variable called ```M``` and the seconds in a variable called ```S```. We put in a formula for the second hand to work out where it should point. Now we need to work out a formula for the minute hand.

The minute hand starts pointing towards the 12 at the beginning of the hour. So we need *another* formula for Python to calculate how many seconds have passed since the beginning of the hour. Here are some facts we need to use:

+ the number of minutes since the hour began is in a variable called ```M```
+ there are 60 seconds in every minute
+ the number of seconds since the minute began is in a variable called ```S```

Can you work out the Python formula, using the variables ```M``` and ```S```, to calculate how many seconds have passed since the beginning of the hour?

If we multiply this formula by the formula for how many degrees the minute hand moves every second we now have a formula to set the direction of pointing for the minute hand. We will set this direction using the code:
```
minute_hand.setheading(****your formula in here****)
```

Once you have got a possible formula put this line of code into the ```while True:``` loop, after the code to set the direction of the second hand and run your code. Is the minute hand pointing to the right place? Watch your clock for a while to see if the minute hand is slowly creeping round. Whenever the second hand points at 12 the minute hand should be pointing exactly at one of the minute marks.

### Setting the direction for the hour hand to point

The steps for getting the hour hand to point in the right direction are exactly the same as for the minute hand, except the Python formulas are a little bit more complicated.

First, we need a formula for **how many degrees the hour hand moves in a second**.
Try and work this out using the same logic as for the minute hand - how many degrees there are in a circle, and how many seconds it takes for the hour hand to go all the way round the clock starting with pointing at the 12, until it's pointing to the 12 again.

Second, we need *another* formula for **how many seconds have passed since the time was 12 o'clock**.
This time we need to use all three variables ```H```, ```M``` and ```S```.

Thirdly, we multiply the two formulas together to set the heading for the hour hand. Once you have a formula put it into this line of code and place the code inside the  ```while True:``` loop, after the code to set the direction of the hour hand.
```
hour_hand.setheading(****your formula for the hour hand in here***)
```

Run your code and see if your clock hands are in the right place.

### Stop the clock flickering

You might find the clock hands are flickering as they move - this is because Python is trying to redraw all the turtles many times a second. One way to stop this is to add this line of code just before the ```while True:``` loop:
```
tracer(0)
```
and this line of code as the last line *inside* the ```while True:``` loop:
```
update()
```

With these extra lines Python will only redraw the turtles when it has to, so it should stop the flickering.

### Draw the hands in the order you want

Most clocks have the second hand above the minute and hour hands. If you've added the hands in the order of this project you will find the second hand is drawn *under* the hour and minute hands. To change this and put the second hand on top you need to change the order you create the turtles.

Take all the code for creating and defining the second_hand turtle - in one example this code might look like this:
```
second_hand = Turtle()
second_hand.color("red")
screen.register_shape("second hand", ((-1,-4), (1,-4), (1,230), (-1, 230)))
second_hand.shape("second hand")
```

and move it so it is *after* the code which creates and defines the hour_hand and minute_hand turtles. That will result in the second hand being drawn *after* the minute and hour hands, so it will appear on the top.