## Hint for distance to move before drawing tick mark

We need to give the distances in fractions of the circle radius.

We know that

*fraction to move before drawing* + *fraction to move while drawing* = 1

We can rearrange this to

*fraction to move before drawing* = 1 - *fraction to move while drawing*

The *fraction to move while drawing* is in the variable ```tick_len```

So the *fraction to move before drawing* is ```1 - tick_len```

You need to multiply this by the clock radius to get the distance in pixels. You will need to use some brackets to get the right number!

[Go back to previous page](README2.md)