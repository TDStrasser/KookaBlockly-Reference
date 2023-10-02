Functions
=========



Functions are used to specify a commonly used sequence of blocks once instead of repeatedly in 
a program, and when that sequence is needed the function can be invoked.  This simplifies 
programs and saves valuable computer memory space.

 


Function Definition
-------------------

 
This control block allows a user to define a sequence of blocks that will be run together when 
the function’s block is used.  

The Function block has a gear wheel for further definition as below

 
A function may be invoked with a set of parameters called “arguments” that are used to tailor 
the function’s operation to its context.  For example, if the function performs a complex 
mathematical calculation, the arguments would be the parameters that feed into the 
calculation.

Function Definition with Return Value
-------------------------------------


 

This block works in a similar manner to the Function Definition block except that this block 
returns a value back to the block that called it.  The value returned is the value block socketed at 
the bottom of the block.  When called this function will be treated as whatever value it returns 
when it is done with its own blocks.

Here is an example where a function is defined to calculate the area of a circle given a radius, 
and a program that uses the function.
 
 


If Condition Return Value
-------------------------


 

This block can be used in both the Function Definition and Function Definition With Return 
Value.  It will check the True / False condition in the first value block socket and if it is True it will 
end the function immediately. It will return the value in the second socket to where it was 
called. If used inside a Function Definition block (without a return value) the returned value will 
be ignored.









 
