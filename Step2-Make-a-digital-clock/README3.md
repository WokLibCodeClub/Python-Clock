If you've corrected your code properly the turtle ```write()``` line should look like this:
```
t.write(str(H)+":"+str(M)+":"+str(S))
```
and when you run your code the turtle should write the time in the middle of the window.

Is the display of the time very small? We can make it bigger by adding a ```font``` parameter in the ```write()``` function. If we want to use the font Arial and have the size 96 and use normal text (instead of bold or italic) we would change the ```write()``` function to this:
```
t.write(str(H)+":"+str(M)+":"+str(S), font=("Arial", 96, "normal"))
```

Now the display is big enough, but it goes off the edge of the screen. This is because the text in a ```write()``` function is set to **Left** alignment. It would be better if the alignment was **centred**. We can add an ```align``` parameter to the ```write()``` function:
```
t.write(str(H)+":"+str(M)+":"+str(S), font=("Arial", 96, "normal"), align = "center")
```
**Note:** we have to use the American spelling of center here.

# Keep the time updating

Displaying the time once is not very useful. We want our digital clock to keep updating itself. For this we need a Python **forever loop** and we can put all the code for 
* finding out the time, 
* putting the hours minutes and seconds into variables and 
* having the turtle write the time 

*inside* the loop.

Start the forever loop with this code:
```
while True:
```
Move your lines of code which find out the time, extract the hour, minutes and seconds to variables and display the time *below* this line and **INDENT ALL THESE LINES**  to show they are part of the loop.

**Add one more line** to the end of the ```while True:``` loop:
```
sleep(1)
```
This will cause the code to pause for one second then check the time again and display the new time.

Save your code and run it to see what happens.

[Continue](README4.md)

[Go back to previous page](README2.md)

