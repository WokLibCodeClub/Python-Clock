### Draw ticks at all the seconds positions

Hopefully you've now got one short tick at the 12 o'clock position. But we want **60** ticks this size. You probably realise this is going to need a loop - in fact it's a **repeat 60 times** loop.

In Python the way to make a loop which repeats a set number of times is this:
```
for i in range(n):
```
where ```n``` is the number of times the loop repeats.

For the seconds ticks we want the loop to repeat 60 times, but we have a variable called ```num_ticks``` which is already set to 60 so instead of putting the number 60 inside the brackets we'll put the variable name.



[Continue to next section *Draw all the different size ticks*](README5.md)

[Go back to previous page](README2.md)