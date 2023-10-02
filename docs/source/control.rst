=======
Control
=======



Control blocks direct program flow or provide time-related functionality.



On Start
--------


TEXT
TEXT







Scheduled Loop
--------------



This block is a loop that runs the blocks nested inside it every at the time interval specified. 
The loop will continue forever at the defined period unless the program is externally stopped.
The time specification is in decimal seconds, for example 0.001 is 1 millisecond.

Repeat
------

 

This block runs the blocks nested inside it in a repeated loop.  The loop will run forever unless
 externally stopped.  Another name is a Repeat Forever loop.

Exit Program
------------

 

Causes the running program to exit

Sleep
-----

 
This block causes the program to wait / pause for the specified time before continuing to the next block.  Decimal portions of seconds are allowed.

Time (s)
--------

 
This block returns a value in whole seconds since the Kookaberry’s epoch time ( 00:00 on 1st 
January 2000).  By subtracting successive values given by this block, the elapsed interval in 
seconds between the samples may be calculated which is useful for timing functions.


Time (ms)
---------

 

This block returns a value in milliseconds since the Kookaberry’s epoch time (00:00 on 1st 
January 2000).  By subtracting successive values given by this block, the elapsed interval in 
seconds between the samples may be calculated which is useful for high-resolution timing 
functions.
