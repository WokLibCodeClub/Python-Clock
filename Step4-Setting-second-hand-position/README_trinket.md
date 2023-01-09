# Setting the position of the second hand

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

We can put this into a Python function like this:

```python
def clk_to_turt(ang):
    return 90 - ang
```

This function should be put in the code before the ```while True``` loop.

When we call this function we put a number of degrees inside the brackets - this will be the clock angle. The function then sends back the angle converted to a turtle angle.

</details>

## Setting the correct angle for the second hand

First we work out what the angle is in clock degrees counting clockwise round from the 12 o'clock position, then call the ```clk_to_turt()``` function to convert this to turtle degrees.

Once we've got the correct number of turtle degrees we tell the turtle which way to point with the code ```t.setheading(ta)``` where the turtle is called ```t``` and we want it to point in a direction of ```ta``` degrees using turtle angles.

We can combine this setheading command with our conversion function in a single line of Python code like this:

```python
t.setheading(clk_to_turt(ca))
```

where the turtle is called ```t``` and ```ca``` is the angle in clock degrees. The function will convert clock degrees to turtle degrees and the ```setheading``` function will point the turtle in the desired direction.

So if we want our turtle called ```second_hand``` to point towards the 3 on the clock we'd calculate that we need a clock angle of 90, and use the code

```python
second_hand.setheading(clk_to_turt(90))
```

But *what is the correct clock angle for where we want the second hand to point?*

For this we need another simple formula. Say we get the time now, and it says the number of seconds is 26. What clock angle is this?

Well we know that the second hand moves 6° every second, so the clock angle for 26 seconds will be 26 times 6 degrees. So whatever the seconds count is we multiply it by 6 to get the clock angle.



For the time being delete the loop from the Step 3 code and instead put this into your code (you should recognise this from Step 1).

This code will

1. get the current time
2. put the hours into a variable called H, 
3. put the minutes into a variable called M and 
4. put the seconds into a variable called S
5. print the value of S in the Python shell 
6. set the direction the second hand has to point in


```
time_now = datetime.now()
H = time_now.hour
M = time_now.minute
S = time_now.second

print(S)

second_hand.setheading(?)
```
As before, **THIS CODE WON'T WORK** because of the question mark. You need to replace the question mark with a little formula, which uses the value of the variable S, to point the hand in the right direction. Use the number you calculated for how many degrees the hand moves for each second.

Run the code several times and check the number printed in the Python shell (which is the value of S) and the position of the second hand. Do they agree?

If the second hand doesn't point in the right direction you need to adjust your code and try again. Don't worry if you the hand position isn't right first time - all coders have to try things lots of times until they get the code just right.

To keep our clock in synch with the computer's time we will need to keep checking the time and setting the position of the hands correctly. We can do this with just the second hand by putting the code shown above inside a ```while True:``` loop.

Create a ```while True:``` loop containing the code for getting the time, putting the hours, minutes and seconds into variables, and setting the direction of the second hand. (You don't need the print() function).

### Note about indents
When you put code inside a loop it's essential to **_indent_** all the lines of code inside the loop. With all the main Python editors you can indent lots of lines of code all in one go - select all the lines you want to indent, then press the TAB key once. You should see all the lines indent together.

Run your code and see if the second hand moves round properly.

[Continue to Step 5 - Adding the minute and hour hands](../Step5-Adding-minute-and-hour-hands)


