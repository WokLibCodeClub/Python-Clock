# Setting the position of the second hand (trinket)

You've just calculated how many degrees the second hand turns for each second of time.

The next step is to use Python to get the time (just like we did with the digital clock) then set the second hand to point to exactly the right position on the clock.

## Different systems for measuring angles

At this point we have to introduce a small problem, and it explains why this project is a tiny bit more complicated to code using trinket than with a standalone Python installation.

We will calculate the angles for the clock's hands using a system similar to compass bearings in Geography - when the hand is pointing straight up (or North) it is at 0°, when it is pointing to the 3 (East) it is at 90°, to the 6 (South) is 180° and to the 9 (West) is 270°. This means that as the hand goes round the clock the angle is always getting *bigger* (until it reaches 359°, then it goes back to 0°). We will call these angles "clock angles".

Unfortunately, in trinket, the angles for turtles are calculated using a **different** system: when the turtle is pointing East it is at 0°, when it is North it is at 90°, West is 180°, and South is 270°. So if a trinket turtle is turning round like a clock hand the angle is always getting *smaller*. To make the turtles (clock hands) point in the right direction we need to use the turtle system angles. We can call these "turtle angles".

Luckily we can easily convert clock angles to turtle angles and the best way to do this in Python is to write a function.

We need a little formula to take a clock angle and convert it to a turtle angle. If you are feeling inspired you could try to work out this formula, using the information above. Or have a look at the answer.

<details><summary>Formula</summary>

The formula for taking a clock angle and converting it to a turtle angle is

```python
turtle_angle = 90 - clock_angle
```

Notice that this formula will sometimes give a negative answer. That's ok, because Python turtles don't mind if they are asked to point in a negative direction. A negative angle means you start at zero and go the opposite direction to normal. If you start at 0° and turn forwards by 90°, you can see that is exactly the same as starting at 0° and going in the opposite direction to -270°.

We can put this formula into a Python function like this:

```python
def clk_to_turt(ang):
    return 90 - ang
```

This function should be put into your code just *before* the ```while True:``` loop. (By the way, the name of the function should really be ```clock_angle_to_turtle_angle()``` but that's a lot of typing, so I just shortened it to ```clk_to_turt()```!)

When we *call* this function we put a number of degrees inside the brackets - this will be the clock angle. The function then sends back the angle converted to a turtle angle.

</details>

## Calculating the correct angle for the second hand

First we work out what the angle is in clock degrees counting clockwise round from the 12 o'clock position, then call the ```clk_to_turt()``` function to convert this to turtle degrees.

Once we've got the correct number of turtle degrees we tell the turtle which way to point with the code ```t.setheading(ta)``` where the turtle is called ```t``` and we want it to point in a direction of ```ta``` degrees using turtle angles.

We can combine this setheading command with our conversion function in a single line of Python code like this:

```python
t.setheading(clk_to_turt(ca))
```

where the turtle is called ```t``` and ```ca``` is the angle in clock degrees. The function will convert clock degrees to turtle degrees and the ```setheading``` function will point the turtle in the desired direction. **BUT DON'T PUT THIS LINE IN YOUR CODE - IT IS JUST FOR AN EXAMPLE.**

So if we want our turtle called ```second_hand``` to point towards 3 o'clock we'd calculate that we need a clock angle of 90, and use the code

```python
second_hand.setheading(clk_to_turt(90))
```

**AGAIN, THIS LINE IS JUST AN EXAMPLE - DON'T PUT IT IN YOUR PROJECT.**

But *what is the correct clock angle for where we want the second hand to point?*

For this we need another simple formula. Say we get the time now, and it says the number of seconds is 26. What clock angle is this?

Well we know that the second hand moves 6° every second, so the clock angle for 26 seconds will be 26 times 6 degrees. So whatever the seconds count is we multiply it by 6 to get the clock angle.

## Code for pointing second hand in the correct direction

In the ```while True:``` loop delete the line which turns the second_hand turtle right by 6°.

In its place, copy in the lines of code from the Digital Clock project which get the time now and put the hours, minutes and seconds into variables called H, M and S.

After these lines of code add a line which will print the value of the variable S in the text result window, then add the line which will set the heading for the second_hand turtle. The whole loop will look like this:

```python
while True:
  time_now = datetime.now()
  H = time_now.hour
  M = time_now.minute
  S = time_now.second

  print(S)
  
  second_hand.setheading(?)

  sleep(1)
```

**BUT** *you* have to work out what to put in the setheading line in place of the question mark.

When you have sorted this out, run the code several times and check the number printed in the text result window (which is the value of S) and the position of the second hand. Do they agree?

If the second hand doesn't point in the right direction you need to adjust your code and try again. Don't worry if you the hand position isn't right first time - all coders have to try things lots of times until they get the code just right.

When you are sure your second hand is moving correctly you can delete the ```print(S)``` line, as this is just for checking the code.

### Updating the picture

You might notice some very strange behaviour when the second hand gets near the 3. Instead of ticking past the 3 it suddenly goes round almost the full circle in the wrong direction and resumes ticking after the 3.

To stop this happening we can add two lines of code. First, immediately after the line ```s.bgpic(clock_image)``` add the line

```python
tracer(0)
```

and secondly, as the *last* line in the ```while True:``` loop, add the line (and indent it)

```python
  update()
```

These two lines mean the screen will only refresh after the turtle has moved to its proper position, so you will no longer see it slowly rotating before it starts ticking.

### Note about indents

When you put code inside a loop it's essential to **_indent_** all the lines of code inside the loop. In trinket you can indent lots of lines of code all in one go - select all the lines you want to indent, then press the TAB key once. You should see all the lines indent together.

Now you've got the second hand moving properly it's time to add the minute and hour hands to the clock.

[Continue to Step 5 - Adding the minute and hour hands](../Step5-Adding-minute-and-hour-hands/README_trinket.md)

[Go back to previous page](../Step3-Setting-up-the-Analogue-clock/README_trinket.md)
