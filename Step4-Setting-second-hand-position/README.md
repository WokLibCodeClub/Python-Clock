# Setting the position of the second hand

You've just calculated how many degrees the second hand turns for each second of time.

The next step is to use Python to get the time (just like we did with the digital clock) then set the second hand to point to exactly the right position on the clock.

## Different systems for measuring angles

At this point we have to introduce a small problem, and it explains why this project is a tiny bit more complicated to code using trinket than with a standalone Python installation.

We will calculate the angles for the clock's hands using a system similar to compass bearings in Geography - when the hand is pointing straight up (or North) it is at 0°, when it is pointing to the 3 (East) it is at 90°, to the 6 (South) is 180° and to the 9 (West) is 270°. This means that as the hand goes round the clock the angle is always getting *bigger* (until it reaches 359°, then it goes back to 0°). We will call these angles the "clock angles".

Unfortunately, in trinket, the angles for turtles are calculated using a **different** system: when the turtle is pointing East it is at 0°, when it is North it is at 90°, West is 180°, and South is 270°. So if a trinket turtle is turning round like a clock hand the angle is always getting *smaller*. To make the turtles (clock hands) point in the right direction we need to use the turtle system angles.

Luckily we can easily convert clock angles to turtle angles and the best way to do this in Python is to write a function.



## Setting the right angle for the second hand

The code for telling a turtle which way to point is ```t.setheading(x)``` where the turtle is called ```t``` and we want it to point in a direction of ```x``` degrees counting clockwise round from the 12 o'clock position. So if we want our turtle called second_hand to point towards the 3 on the clock we'd use the code ```second_hand.setheading(90)```.

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


