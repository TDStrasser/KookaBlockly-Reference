Display
=======

Display blocks control what appears on the Kookaberry's display.

.. figure:: images/display-palette.png
   :width: 300
   :align: center
   
   The palette of KookaBlockly Display blocks


Each block is described in turn below.


Kookaberry Display
------------------

The Kookaberry’s display is a 128 pixel wide x 64 pixel high cyan OLED display.  

The x direction is the width of the display having a range specified as 0 to 127 pixels and the y direction 
is the height of the display having a range specified as 0 to 63 pixels.  

The (x,y) location (0,0) is at the top left-hand corner of the display.  
The bottom right of the display has a location reference (x,y) of (127,63).

.. figure:: images/display-coordinates.png
   :width: 300
   :align: center
   
   The Display coordinates


The display is driven from an internal memory array known as a Framebuffer, 
into which the software writes the pixel data prior to its contents being transferred to the physical Kookaberry display.  
This reduces any display flicker.  

The method of writing to a display is generally:

1.	**Clear** the Framebuffer
2.	Write text and/or graphics to the Framebuffer in one or more parts to build up the entirety of the Display's contents, and then
3. **Show** the display buffer on the display.

The following blocks provide the functionality to operate the Kookaberry's Display.


Display Clear
-------------
 
This block clears the display’s frame buffer.  The physical display will not be updates until a "Display Show" is used.

.. figure:: images/display-clear.png
   :width: 300
   :align: center
   
   Display Clear block

Display Show
------------
 
This block transfers the display’s frame buffer to the Kookaberry’s physical display.  
If not specified in the KookaBlockly script, the generated MicroPython script will contain the equivalent **Display Show** code towards the end of the script.


.. figure:: images/display-show.png
   :width: 300
   :align: center
   
   Display Show block



Display Set Font
----------------
 
This block sets the character font to that selected from the drop down box.  The display fonts 
available for selection are from smallest to largest: mono5x5 (i.e. each character occupies 5  pixels wide by 5 pixels tall), 
mono6x7, mono6x8, mono8x13 and sans12.

The selected font will be applied from the point of selection.

A display using several fonts sizes may be constructed by using the **Display Set Font** block 
as the display Framebuffer is constructed by the KookaBlockly script.


.. figure:: images/display-setfont.png
   :width: 300
   :align: center
   
   Display Set Font block

Display Print
-------------
 
This block prints the editable text in the socketed block to the Kookaberry display at position x=0 on a new line.  
The current line is set to the top of the screen immediately after the display is cleared. 

If the line is longer than the display’s width, the line is wrapped onto successive lines of the display. 
The current display line is increased by each successive **Display Print** until the bottom of the display is reached.  

Thereafter each successive **Display Print** will scroll the display upwards by one line and the current line is shown at the bottom of the display.


.. figure:: images/display-print.png
   :width: 300
   :align: center
   
   Display Print block



Display Print-and
-----------------
 
This block displays the editable text or value in the attached socketed block on the current line of the display, 
followed by the output of any value block.


.. figure:: images/display-print-and.png
   :width: 300
   :align: center
   
   Display Print-and block



The following is an example using the date and time:
 
.. figure:: images/display-print-and-example.png
   :width: 400
   :align: center
   
   Display Print-and example script


This example results in a display that looks like this and is updated every second. 


.. figure:: images/display-print-and-tw.png
   :width: 300
   :align: center
   
   Display Print-and example Display

By using “Display Clear” the displayed text stays at the top of the screen instead of scrolling down the display.


Display Pixel
-------------
 
This block displays a pixel at the x and y locations with the specified colour on the display.  The 
values of x, y and colour are the outputs of any value block.  If the values of x or y are outside of 
the display dimensions then the pixel will not be visible.  The values for colour should be either 0 
or 1, where 0 is pixel off (black) and 1 is pixel on (blue).

Display Line
------------

 

This block draws a line on the display starting from the location given by the values x1, y1 to the 
location given by the values x2,y2.  The values for colour should be either 0 or 1, where 0 is pixel 
off (black) and 1 is pixel on (blue).


Display Rectangle
-----------------

 


This block displays a rectangle starting at location given by the values  x, y  with a width and 
height given by the results of the value blocks attached to those parameters.
The “fill?” box when ticked fills the rectangle with visible pixels.




Display Text Value
------------------

 

This block enables the display of the attached output of the attached value block (ie “Hello”) at 
the location specified by the value blocks at x and y on the display, with the colour being the 
value block output of 0 or 1.
Note:    The x, y coordinate is where the bottom left corner of the display text is positioned.

This is an example where the value of the current seconds since epoch is displayed at location 0, 
40.

 
 









Display Image
-------------

 
This block allows for the creation of an 8 x 8 pixel array which can be displayed on the 
Kookaberry display at the locations of x and y.

The “transparent?” box if ticked will not extinguish any pre-existing pixels that were on giving an 
impression of transparency.

By manipulating the values of x and y using value blocks, the pixel array can be made to move 
around the screen.  

The following is an example where a pixel block shaped as an arrow moves
diagonally from the top left to the bottom right of the display then wraps around to the top ad-infinitum.  

See also the descriptions of the variable and if-do statements later in this manual.

 

 
