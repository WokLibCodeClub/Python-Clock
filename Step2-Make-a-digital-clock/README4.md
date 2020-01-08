Oh dear, when the turtle writes the new time it writes it over the top of the previous time. Luckily we can clear the turtle screen using the function ```clearscreen()```. It doesn't need any values in the brackets. Add this function to the end of the ```while True:``` loop and test your code again.

There is one more thing which we should change to make a good digital clock. When the clock ticks over to the next minute the number of seconds is less than 10 so only uses a single digit. This makes all the other numbers shift over until the number of seconds gets above 10.

What we need is a way to fill the number of seconds with an extra zero, so that the number of seconds shows as 01, 02, 03 instead of 1, 2, 3. We can do this with a method called ```.zfill(2)``` added on to the end of the ```str(S)``` part of the ```write()``` function. This will add zeros to make sure the number of seconds always shows with two digits. We can do the same to the minutes and the hours.

The finished write function will look like this:
```
    t.write(str(H).zfill(2) + ":" + str(M).zfill(2) + ":" + str(S).zfill(2),
            align = "center", font=("arial", 96, "normal"))
```

To change the colour of the text you need to change the colour of the turtle. If you wanted the text to be red, for example, you would do this by adding the code ```t.color("red")``` just after you have created the turtle called ```t```.

We can use a lot of the same code in creating an Analogue clock.

[Go to step 3](../Step3-Setting-up-the-Analogue-clock)

