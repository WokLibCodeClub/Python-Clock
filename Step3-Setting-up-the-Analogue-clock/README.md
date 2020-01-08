# Setting up the Analogue clock

It's best to start a new .py file for the analogue clock to avoid confusion with the code for the digital clock. You could call this file **analogue-clock.py**

At the top of the file we need to import the same modules as for the digital clock, so copy all the import lines in from the digital clock code.

We are going to use turtles for the clock hands but first we need a clock background. For this step we will use a ready-made background (but at the end of the project you should try writing code to create your own background).

You need to download the clock image. Do this by clicking [here](blank_clock.gif) then *right-click* on the grey Download button and save the file to the same folder where you are writing the clock code.

Add these lines of code below the import lines:
```
screen = Screen()
setup(650,650)
clock_image = "blank_clock.gif"
screen.register_shape(clock_image)
screen.bgpic(clock_image)
```

