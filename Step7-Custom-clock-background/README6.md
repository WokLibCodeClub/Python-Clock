### 3. Draw the numbers

Our clock is almost complete. The only remaining task is to draw the numbers.

We can do this using another loop - a repeat 12 times loop.

Just after the code which calls the function to draw the ticks add this line:
```
for i in range(12):
```

You might wonder what the ```i``` means in this line. This is another Python variable, and each time the loop runs the variable ```i``` increases by 1, so it's 0 the first time through the loop, 1 the second time, 2 the third time, up to 11 for the last time.

We can use the value of ```i``` in this loop to write the clock numbers, using the ```turtle.write()``` function.



This is the last stage. You should now have a customised clock which keeps proper time. If you want to make it bigger or smaller you should only have to change the value of the variable ```clock_radius```. Try that now, and see if it works.

Congratulations on your clock!


[Go back to previous page](README5.md)