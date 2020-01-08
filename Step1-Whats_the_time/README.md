# What's the time?

Computers always need to know what the time is, and usually you can see the computer time in a display at the bottom right of your screen. Computers get the exact time from the internet. Python has functions to get the exact computer time so you can use it in your code.

#### First:

make a new folder for this project in the place where you keep your Python code. You could call it **Python-clock**

#### Second:

start a brand new Python file to put the code for this step in. You could call it **get_time.py**

The Python functions for finding out about the date or time are in a special *module* called ```datetime``` so the first line of code needs to import this module:

```
from datetime import datetime
```

To find out the present time we use the function ```datetime.now()```. Add a line of code which will use this function and put the result in a variable called ```time_now```:
```
time_now = datetime.now()
```
The variable ```time_now``` is not a number variable, or a string of letters - it is a type of variable called a *datetime object* and this means we can't just print it to find out what the time is.

What we can do is extract parts of the datetime object and print those. This command will print out the current hour:
```
print(time_now.hour)
```

Add two more lines to your code, following the same pattern, which will print the ```minute``` and ```second``` of the current time.

Save your code and run it. It should print out something like this:

```
11
32
38
>>> 
```
which means that at the moment when I ran my code the time was 38 seconds and 32 minutes past 11am.

Printing out the time like this is not a good way of showing what the time is as it's very small. In the next step we will use Turtles to make a much bigger display which keeps updating itself.

Before that we need to make some variables to hold the values of the hour, minute and second of the current time. Here is an example of putting the hour value in a variable:
```
H = time_now.hour
```

Add two more lines to put the minutes and seconds into their own variables.

You can also delete or comment out the print functions in your code as we won't be needing those.

[Go to step 2](../Step2-Make-a-digital-clock)
