Boolean
=======




Boolean blocks are value blocks used to test whether a specified condition is True (1) or False (0).

 


Comparison
----------

 

This ‘comparison’ block compares the two value blocks that are given with the rule selected from the dropdown menu and represents the result as True or False.  The options, less than (<), less than or equal to (≤), greater than (>), and greater than or equal to (≥) only work for single numbers.  Equal to (=) and not equal to (≠) work for almost anything including numbers, lists (arrays) and character strings.


Boolean And/Or
--------------

 

This block performs a selected Boolean operation on its two inputs.  Boolean operations take True/False value blocks in their sockets and give back a True/False value based on the operation.  AND will give back a True only if both of its inputs are True.  OR will give back True if either of its inputs are True.

Not
---

 

This block takes a True/False value block in its socket and logically inverts it.  True becomes False and False become True.

True / False
------------

 

This value block gives a True or False value depending on which option is selected.  It is generally used to initialise variables that are subsequently used in a program.






Null
----

 

This value block is the value that variables have before they are given a value.  It is a special 
value that represents “none” or “nothing” but is distinct from 0.  However it is treated as a zero 
or False value if used.


Ternary Test
------------

 

This block represents a value.  What value it represents depends on the result of the block in the 
Test socket.  If the block in the Test socket is True, the whole Ternary Test block represents what 
is in the If True socket.  If the block in the Test socket is false, the whole Ternary Test block 
represents what is in the If False socket.





