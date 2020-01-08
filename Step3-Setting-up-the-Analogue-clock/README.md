# Setting up the Analogue clock

It's best to start a new .py file for the analogue clock to avoid confusion with the code for the digital clock. You could call this file **analogue-clock.py**

At the top of the file we need to import the same modules as for the digital clock, so **copy all the import lines** in from the digital clock code.

We are going to use turtles for the clock hands but first we need a clock background. For this step we will use a ready-made background (but at the end of the project you should try writing code to create your own background).

You need to download the clock image. Do this by clicking [here](blank_clock.gif) then *right-click* on the grey Download button and save the file to the same folder where you are writing the clock code.

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

Save your code and run it. You should see the clock background with a red arrow-shaped turtle in the middle of the clock.

Unfortunately the arrow shape is not much good as a second hand - we need something longer and thinner. We can create our own shape for a turtle by specifying a set x and y coordinates. Use this code to make a long thin second hand shape:
```
screen.register_shape("second hand", ((-1,-4), (1,-4), (1,230), (-1, 230)))
second_hand.shape("second hand")
```
Each pair of numbers in brackets is an x coordinate and a y coordinate for a corner of the turtle shape. Save your code and run it. You should see a long thin turtle pointing at the number 12.

