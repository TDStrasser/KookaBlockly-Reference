Loops
=====

 

Loops are a category of control blocks that direct the flow of a program.  They run the nested action blocks a number of times in accordance with the test taken at the beginning of the loop.

 


Repeat a Number of Times
------------------------

 

This block runs the blocks nested inside of it for the specified number of times.  When those are complete the program moves on to the blocks below it.





Repeat While / Until
--------------------


In this block the two operations of While and Until are very similar to each other.  Both require a 
True / False value block in their socket.  Repeat While will act like a Repeat Forever while the 
socketed value block is True.  Repeat Until will act like a Repeat Forever while the socketed block 
is False.  

Count With Variable (i) From # To # By #
----------------------------------------










This loop will run its nested blocks several times depending upon the numbers given.  It will start 
by setting the chosen variable to the first number.  If the variable is smaller than the second 
number it will run the nested blocks then increase the value of the variable by the third number.  
It will then keep repeating the check-if-variable-less-than-second-number, run blocks, increase-
variable-by-third-number cycle until the value of the variable is equal to or greater than the 
second number.  So if it was from 0 to 3 by 1, it would run the nested blocks with the variable’s 
value being 0,1 and 2.  The variable would be increased to 3 but as 3 is not less than 3 the blocks 
in the loop would not be run again and the program would advance to the next block after the 
loop.  This can be used to mimic a Repeat Number of Times loop but with the added benefit of 
being able to use the variable’s value to know which repetition of the loop is being run. 

The options “Rename variable” and “Delete variable” are configuration functions to manage the 
creation of new variables or deletion of existing variables. See also the Variables Category.







For Each Item In List
---------------------



This block has a socket that takes a List.  It starts by setting the chosen variable to be the same as 
the first item of the list and then it runs the nested blocks.  It then sets the chosen variable as 
the second item of the list and runs the nested blocks again.  This repeats until it has run once 
for every item in the list.

Break / Continue Loop
---------------------


This block requires that these options must be placed inside a loop.  Both stop the current 
iteration of a loop which is why no blocks can be attached beneath them within the loop they 
are in.  “break out” immediately ends the loop and jumps to the next block after it.   “continue 
with next iteration” stops the current iteration and jumps back to the top of the loop and will 
run again if the loop allows it.
The usual way to use this block is in an ‘If-Do block’ where breaking a loop is subject to a logical test.








