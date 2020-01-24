# Setting the position of the second hand

You've just calculated how many degrees the second hand turns for each second of time.

The next step is to use Python to get the time (just like we did with the digital clock) then set the second hand to point to exactly the right position on the clock.

The code for telling a turtle which way to point is ```t.setheading(x)``` where the turtle is called ```t``` and we want it to point in a direction of ```x``` degrees counting clockwise round from the 12 o'clock position. So if we want our turtle called second_hand to point towards the 3 on the clock we'd use the code ```second_hand.setheading(90)```.

For the time being delete the loop from the Step 3 code and instead put this into the code (you will recognise this from Step 1):
```
time_now = datetime.now()
H = time_now.hour
M = time_now.minute
S = time_now.second

print(S)

second_hand.setheading(?)
```
As before, **THIS CODE WON'T WORK** because of the question mark. You need to put in a little formula, which uses the value of the variable S to point the hand in the right direction. Use the number you calculated for how many degrees the hand moves for each second.

Run the code several times and check the number printed in the Python shell (which is the value of S) and the position of the second hand. Do they agree?


To keep our clock in synch with the computer's time we will need to keep checking the time and setting the position of the hands correctly. This is 

[Continue to Step 5 - Adding the minute and hour hands](../Step5-Adding-minute-and-hour-hands)


