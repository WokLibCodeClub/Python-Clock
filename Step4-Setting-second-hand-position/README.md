# Setting the position of the second hand

You've just calculated how many degrees the second hand turns for each second of time.

The next step is to use Python to get the time (just like we did with the digital clock) then set the second hand to point to exactly the right position on the clock.

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


