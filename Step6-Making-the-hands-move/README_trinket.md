# Making the minute and hour hands move (trinket)

We are going to follow the same steps we used to make the second hand point in the right direction, first for the minute hand, then for the hour hand.

## Calculating the clock angle for the minute hand

The first step for the minute hand is to work out **how many degrees this hand moves every second**.

**Here is a very important point:** Python is really good at doing calculations. So coders *never* have to work out difficult sums - the computer can do that. What the coder has to do is **_work out the right formula_** to give the computer, so the computer can calculate the right answer.

To work out the formula for how many degrees the minute hand moves every second we can use these facts:

+ at the beginning of the hour the minute hand points up towards 12 o'clock
+ the minute hand takes exactly one hour to go right round the clock until it's pointing at 12 o'clock again
+ there are 360° in a circle
+ there are 60 seconds in a minute
+ there are 60 minutes in an hour

What is the formula for **how many degrees the minute hand moves in a second**?

<details><summary>Hint</summary>

We need to divide the number of degrees in a circle by the number of seconds in an hour.

One way of putting this in code is:

```python
360/(60*60)
```
The answer is how many degrees the minute hand moves in one second.

</details>

The second step is to find a formula for **how many seconds have passed since the minute hand pointed at the 12**.

We can then multiply the two formulas together to find the clock angle where the minute hand should point. We can then use our function to convert the clock angle to turtle angle to make the minute hand turtle point in the right direction.

Here are some facts we need to use for **how many seconds have passed since the minute hand pointed at the 12**:

+ the minute hand starts pointing towards the 12 at the beginning of the hour
+ the number of minutes since the hour began is in a variable called ```M```
+ there are 60 seconds in every minute
+ the number of seconds since the minute began is in a variable called ```S```

Can you work out the Python formula, using the variables ```M``` and ```S```, to calculate **how many seconds have passed since the minute hand pointed at the 12**?

<details><summary>Hint</summary>

If each minute lasts 60 seconds, then there will be 60 seconds for every minute in the variable ```M```. We can calculate this number using ```M * 60```.

Then we add in the number of seconds since the last minute started - this is in the variable ```S```. So the final answer for the number of seconds since the beginning of the last hour is

```python
M * 60 + S
```

</details>

Next we multiply this formula by the formula for how many degrees the minute hand moves every second and we now have a formula for the clock angle of the minute hand. 

The last step is to use the function to convert clock angle to turtle angle, then the ```setheading()``` function to point the minute hand turtle in the right direction:

```python
minute_hand.setheading(clk_to_turt(****your formula in here****))
```

Once you think you have got the formula put this line of code into the ```while True:``` loop, after the code to set the direction of the second hand and run your code. Is the minute hand pointing to the right place? Watch your clock for a while to see if the minute hand is slowly creeping round. Whenever the second hand points at 12 the minute hand should be pointing exactly at one of the minute marks.

## Calculating the clock angle for the hour hand

The steps for getting the hour hand to point in the right direction are exactly the same as for the minute hand, except the Python formulas are a little bit more complicated.

First, we need a formula for **how many degrees the hour hand moves in a second**.
Try and work this out using the same logic as for the minute hand - how many degrees there are in a circle, and how many seconds it takes for the hour hand to go all the way round the clock starting with pointing at the 12, until it's pointing to the 12 again.

Second, we need *another* formula for **how many seconds have passed since the time was 12 o'clock**.
This time we need to use all three variables ```H```, ```M``` and ```S```.

Third, we multiply the two formulas together to set the heading for the hour hand. Once you have a formula put it into this line of code and place the code inside the  ```while True:``` loop, after the code to set the direction of the minute hand.
```
hour_hand.setheading(****your formula for the hour hand in here***)
```

Run your code and see if your clock hands are in the right place.

### Stop the clock flickering

You might find the second hand flickering as it moves - this is because Python is trying to redraw all the turtles many times a second. One way to stop this is to add this line of code just *before* the ```while True:``` loop:
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

Hooray - you now have a functioning clock! Congratulations!

[Continue to Step 7 - Customising the clock background](../Step7-Custom-clock-background)
