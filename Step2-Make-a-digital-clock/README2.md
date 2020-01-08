If you have the hour in a variable called ```H```, the minutes in a variable called ```M``` and the seconds in a variable called ```S``` then you could write the time on the screen using
```
t.write(str(H)+str(M)+str(S))
```

Try this and see what happens by saving your code and running it.

You could improve this by putting a colon in between each of the values: ```str(H)+":"+str(M)+``` etc. Edit your code to get a display with colons.

Is the display of the time very small? We can make it bigger by adding a ```font``` parameter in the ```write()``` function. If we want to use the font Arial and have the size 96 and use normal text (instead of bold or italic) we would change the ```write()``` function to this:
```
t.write(str(H)+":"+str(M)+":"+str(S), font=("Arial",96, "normal"))
```

Now the display is big enough, but it goes off the edge of the screen. This is because the text in a ```write()``` function is set to **Left** alignment. It would be better if the alignment was centred. We can add an ```align``` parameter to the ```write()``` function:
```
t.write(str(H)+":"+str(M)+":"+str(S), font=("Arial",96, "normal"), align = "center")
```
**Note:** we have to use the American spelling of center here.





[Go to step 3](../Step3-Analogue-clock-second-hand)


