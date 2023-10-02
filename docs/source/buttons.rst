Buttons
=======

The Kookaberry has four buttons beneath the display labelled A, B, C and D.  These buttons are 
coloured red, blue, yellow, and green respectively.  Button functions available on the “show 
display in KookaSuit




 


When Button WAS Pressed
-----------------------

 

This is a control block that performs the actions contained within it whenever the selected 
button (options are A, B, C, or D) was pressed.  “was pressed” means that the actions will be 
performed only once after the button press.

When Button IS Pressed
----------------------







This is a control block that performs the actions contained within it whenever the selected 
button (options are A, B, C, or D) is pressed.  “is pressed” means that the actions will be 
performed repeatedly as long as the button is being pressed.


Button was pressed
------------------

 

This is a value block whose result is “True (= 1)” whenever the selected button (options are A, B, 
C, or D) was pressed.  After this value block is used its output reverts to “False (=0)” until the 
next time the button was pressed.


Button is pressed
-----------------	

 

This is a value block whose result is “True (= 1)” while the selected button (options are A, B, C, or 
D) is pressed. 


Exit Program
------------

 

This is a combination of two blocks: the “button was pressed” as before, in combination with the 
“exit program” action.
The result of using this combination is whenever the button selected was pressed the currently 
running program will finish.
