# Setting up the Analogue clock

It's best to start a new .py file for the analogue clock to avoid confusion with the code for the digital clock. Start a New File and Save As **analogue-clock.py** (or any other name you like).

At the top of the file we need to import the same modules as for the digital clock, so **copy all the import lines** in from the digital clock code.

We are going to use turtles for the clock hands but first we need a clock background. For this step we will use a ready-made background (but at the end of the project you should try writing code to create your own background).

You need to download the clock image. Do this by clicking [here](blank_clock.gif) then *right-click* on the grey Download button and save the file to the same folder where you are writing the clock code.

> After you have downloaded the clock background click the **Back** button in your browser to get back to this page.

Add these lines of code below the import lines:
```
screen = Screen()
setup(600,600)
clock_image = "blank_clock.gif"
screen.register_shape(clock_image)
screen.bgpic(clock_image)
```

These lines set up a turtle screen and specify its size as 600 pixels across by 600 pixels high. This will be just big enough to contain the blank clock image, which is 551 pixels by 551 pixels.

The other lines tell Python to make the clock image available for us to use, and to set the background of the turtle screen to show the clock image.

Save this code and run it to see what happens.

We will now create a turtle to use as the clock's second hand. First, though, add this line to your code:
```
mode("logo")
```
This tells Python that when we tell the turtle to point in the direction of 0 degrees we want it to point directly upwards (towards North). (Without this line the turtle would point to the right if we set it to 0 degrees.)

Now make a turtle to use for the second hand and set its colour to red:
```
second_hand = Turtle()
second_hand.color("red")
```

Save your code and run it. You should see the clock background with a red arrow-shaped turtle in the middle of the clock pointing towards the 12.

Unfortunately the arrow shape is not much good as a second hand - we need something longer and thinner. We can create our own shape for a turtle by specifying a set x and y coordinates. Use this code to make a long thin second hand shape:
```
screen.register_shape("second hand", ((-1,-4), (1,-4), (1,230), (-1, 230)))
second_hand.shape("second hand")
```
Each pair of numbers in brackets is an x coordinate and a y coordinate for a corner of the turtle shape. Save your code and run it. You should see a long thin turtle pointing to the number 12.

# Moving the second hand

To get the second hand to turn to the right and point to a different number we use the turtle ```right()``` function. Try adding this line to the end of your code:
```
second_hand.right(45)
```
Save your code and run it. Hopefully you saw the second hand move round by 45 degrees, so it's now pointing between the 1 and 2.

Delete the last line you just added.

Now we're going to make a loop and get the second hand to move round the clock by turning it to the right a set number of degrees, then waiting one second. Here is the code:

```
while True:
    second_hand.right(?)
    sleep(1)
```
**THIS CODE WON'T WORK.** Python won't understand the question mark. **_You_** need to calculate the number of degrees to put inside the brackets instead of the question mark so that the second hand will move exactly one unit each second, so it takes exactly one minute to go right round the clock.

Hint: You know how many degrees there are in a circle. You know how many seconds there are in a minute. So, you can calculate how many degrees make one second.

When you've calculated the number edit your code, save it and try running it.

[Continue to Step 4 - Setting the position of the second hand](../Step4-Setting-second-hand-position)

###### Clock image copied from [https://www.codenameone.com/blog/codename-one-graphics-part-2-drawing-an-analog-clock.html](https://www.codenameone.com/blog/codename-one-graphics-part-2-drawing-an-analog-clock.html)


