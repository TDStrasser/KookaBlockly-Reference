LEDs
====

This LEDs category supports the three LED’s that are beneath the display on the 
Kookaberry.   ( Also supported are the LEDS on the “Show Display” pane in KookaSuite)
These LEDs are coloured Red, Orange and Green.
In addition, support is provided for Neopixel displays



 


Turn ON LED
-----------


This block turns ON the LED selected from the drop-down box


Turn OFF LED
------------

 

This block turns OFF the LED selected from the drop-down box


Toggle LED
----------

 

This block toggles the LED selected in the drop-down box. Toggle means to change the state of the LED from off to on, or from on to off, depending on the LED’s state.   

Neopixels
---------

 


This block supports Neopixel arrays connected to one of the connections selected in the drop- 
down box. 

The Kookaberry has five connectors on the back, P1 through to P5, with connector P3 having two 
possible connection points (see the Pins category description).

Neopixels are multicolour LEDs with Red, Green and Blue LEDs in every individual Neopixel.  The 
apparent colour of a Neopixel is the result of mixing the Red Green and Blue colours, in the same 
way that a television screen produces colours.
Neopixels come as single units or in chains of multiple Neopixels.



THE FOLLOWING MAY NOW NOT BE RELEVANT
-------------------------------------

The Neopixel block contains two value blocks: 
•	pixel being the number of the LED in the chain of Neopixels (beginning with 1 up to the length of the chain); and 
•	RGB being the value in hexadecimal of the brightness of each of the Red, Green and Blue LEDs within the specified Neopixel.  
 
Hexadecimal numbers comprise the values 0 to 15 expressed as single characters 0 to 9 and A to 
F, where A is decimal 10 and F is decimal 15.  The # symbol preceding the RGB value denotes the 
use of hexadecimal notation.

The RGB value comprises 6 hexadecimal digits, the first two digits being the brightness of the 
Red LED, the third and fourth digits being the brightness of the Green LED, and the fifth and sixth 
LED being the brightness of the Blue LED.  

Each pair of digits ranges from #00 to #FF, which is equivalent to 0 to 255 in decimal. #00 means 
the LED is off and #FF means the LED is fully bright.

The following table gives some RGB examples that produce common colours.  The ratios of RGB 
values produce the colour hue, and the values produce brightness or alternatively known as 
luminosity:

+-------+---------+---------+---------+-----------------------+
|RGB	|Red	  |Green    |Blue     |Neopixel Colour        |
+=======+=========+=========+=========+=======================+
|#000000|#00 (0)  |#00 (0)  |#00 (0)  |Black (all LEDs off)   |
+-------+---------+---------+---------+-----------------------+
|#3F3F3F|#3F (63) |#3F(63)  |#3F(63)  |White 25% brightness   |
+-------+---------+---------+---------+-----------------------+
|#7F7F7F|#7F (127)|#7F (127)|#7F (127)|White 50% brightness   |
+-------+---------+---------+---------+-----------------------+
|#BFBFBF|#BF (191)|#BF (191)|#BF (191)|White 75% brightness   |
+-------+---------+---------+---------+-----------------------+
|#FFFFFF|#FF (255)|#FF (255)|#FF (255)|White 100% brightness  |
+-------+---------+---------+---------+-----------------------+
|#FF0000|#FF (255)|#00 (0)  |#00 (0)  |Red 100% brightness    |
+-------+---------+---------+---------+-----------------------+
|#00FF00|#00 (0)  |#FF (255)|#00 (0)  |Green 100% brightness  |
+-------+---------+---------+---------+-----------------------+
|#0000FF|#00 (0)  |#00 (0)  |#FF (255)|Blue 100% brightness   |
+-------+---------+---------+---------+-----------------------+
|#FFFF00|#FF (255)|#FF (255)|#00 (0)  |Yellow 100% brightness |
+-------+---------+---------+---------+-----------------------+
|#FF00FF|#FF (255)|#00 (0)  |#FF (255)|Magenta 100% brightness|
+-------+---------+---------+---------+-----------------------+
|#00FFFF|#00 (0)  |#FF (255)|#FF (255)|Cyan 100% brightness   |
+-------+---------+---------+---------+-----------------------+

Every pixel in a Neopixel array can be set to an individual colour if desired.


.. note::

  Please note that arrays up to 5 Neopixels can be directly plugged into a Kookaberry connector.  Larger arrays will require special electronics to supply more power.  Directly plugging in large Neopixel arrays may irreparably damage the Kookaberry!

