# Setting up the Analogue clock using trinket

There is a starter trinket project for the analogue clock, which you can find at

- [trinket.io/python/9459a45b06](https://trinket.io/python/9459a45b06)

We are going to use turtles for the clock hands but first we need a clock background. The starter project has a ready-made background included, but when you've created a working analogue clock you could try experimenting with writing code to create your own clock background.

When you are building up this project you might need to widen the trinket graphics window slightly to make sure you can see all of the clock background.

The lines of code included in the starter project are

```python
s = Screen()
s.setup(410,410)
clock_image = "blank_clock_sm.gif"
s.register_shape(clock_image)
s.bgpic(clock_image)
```

These lines set up a turtle screen and specify its size as 410 pixels across by 410 pixels high. They also specify an image file to be used as the background and set that file as the background image.

## Making a turtle for the second hand

First, we'll create a turtle to use as the clock's second hand and set its colour to red:

```python
second_hand = Turtle()
second_hand.color("red")
```

Save your code and run it. You should see the clock background with a red arrow-shaped turtle in the middle of the clock pointing towards the 3.

Unfortunately the arrow shape is not much good as a second hand - we need something longer and thinner. We can create our own shape for a turtle by specifying a set x and y coordinates. Use this code to make a long thin second hand shape to use for our second_hand turtle:

```python
s.register_shape("second hand", ((0,-4), (0,-4), (0,140), (0, 140)))
second_hand.shape("second hand")
```

Each pair of numbers in brackets is a pair of coordinates for a corner of the turtle shape. Save your code and run it. You should see a thin red line (which is the turtle) pointing to the number 3.

## Moving the second hand

To get the second hand to turn to the right and point to a different number we use the turtle ```right()``` function. Try adding this line to the end of your code:

```python
second_hand.right(45)
```

Save your code and run it. Hopefully you saw the second hand move round by 45 degrees, so it's now pointing between the 4 and 5.

Delete the last line you just added as we don't need it.

Now we're going to make a forever loop and get the second hand to move round the clock by turning it to the right a set number of degrees, then waiting one second. Here is the code:

```python
while True:
    second_hand.right(?)
    sleep(1)
```

**THIS CODE WON'T WORK.** Python won't understand the question mark. **_You_** need to calculate the number of degrees to put inside the brackets instead of the question mark so that the second hand will move exactly one unit each second, so it takes exactly one minute to go right round the clock.

Hint: You know how many degrees there are in a circle. You know how many seconds there are in a minute. So, you can calculate how many degrees make one second.

When you've calculated the number edit your code, save it and try running it.

[Continue to Step 4 - Setting the position of the second hand](../Step4-Setting-second-hand-position)

###### Clock image copied from [https://www.codenameone.com/blog/codename-one-graphics-part-2-drawing-an-analog-clock.html](https://www.codenameone.com/blog/codename-one-graphics-part-2-drawing-an-analog-clock.html)
