-------
Display
-------

Display blocks control what appears on the Kookaberry's display.

.. figure:: images/display-palette.png
   :width: 400
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

Text coordinates
----------------

The coordinates at which text is positioned on the Display differs from the graphical elements (``pixel``, ``line``, ``rectangle``, and ``image``).

*  Graphical elements are positioned at their top-left corner.
*  Text is positioned at its bottom-left corner.

To accurately position text, one can use trial-and-error, or make a calculation that depends on the text font size (the default being ``mono8x8``).

* To position a pixel at the top-left of the Display (0,0) simply specify x=0 and y=0 in the **Display Pixel** block.
* To position text at the top-left of the Display, specify (0,7) being x=0 and y=7 (the mono8x8 font height) in the **Display Print** block.

Display Clear
-------------
 
This block clears the display’s frame buffer.  The physical display will not be updated until a "Display Show" is used.

.. image:: images/display-clear.png
   :height: 60
   :align: center
   

Display Show
------------
 
This block transfers the display’s frame buffer to the Kookaberry’s physical display.  

KookaBlockly automatically inserts the equivalent **Display Show** code towards the end of the generated MicroPython script.
However it may be desirable to refresh the physical display earlier in the KookaBlockly script, 
such as at the end of a loop that updates the display.  
Use this **Display Show** block in such circumstances as otherwise the display will not update until the end of the script.

.. image:: images/display-show.png
   :height: 60
   :align: center
   

Display Set Font
----------------
 
This block sets the character font to that selected from the drop down box.  The display fonts 
available for selection are from smallest to largest: 

* ``mono5x5`` - each text character is 5  pixels wide by 5 pixels tall

* ``mono6x7``,- 6 pixels wide by 7 pixels tall

* ``mono6x8`` - 6 pixels wide by 8 pixels tall

* ``mono8x8`` - 8 pixels wide by 8 pixels tall (the default font)

* ``mono8x13`` - 8 pixels wide by 13 pixels tall, and 

* ``sans12``.- 12 pixels wide by 12 pixels tall

The selected font will be applied from the point of selection.

A display using several fonts sizes may be constructed by using the **Display Set Font** block 
as the display Framebuffer is constructed by the KookaBlockly script.

.. image:: images/display-setfont.png
   :height: 200
   :align: center
   

Display Print
-------------
 
This block prints the editable text in the socketed block to the Kookaberry display at position x=0 on a new line.  
The current line is set to the top of the screen immediately after the display is cleared. 

If the line is longer than the display’s width, the line is wrapped onto successive lines of the display. 
The current display line is increased by each successive **Display Print** until the bottom of the display is reached.  

Thereafter each successive **Display Print** will scroll the display upwards by one line and the current line is shown at the bottom of the display.

.. image:: images/display-print.png
   :height: 60
   :align: center
   

Display Print-and
-----------------
 
This block displays the editable text or value in the attached socketed block on the current line of the display, 
followed by the output of any value block.

.. image:: images/display-print-and.png
   :height: 60
   :align: center
   

The following is an example to display the time:
 
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
values of x, y and colour are the outputs of any value block.  

If the values of x or y are outside of the display dimensions then the pixel will not be visible.  

The values for colour should be either 0 or 1, where 0 is pixel off (black) and 1 is pixel on (cyan).

.. image:: images/display-pixel.png
   :height: 60
   :align: center
   

Display Line
------------

This block draws a line on the display starting from the location given by the values x1, y1 to the 
location given by the values x2,y2.  

The values for colour should be either 0 or 1, where 0 is pixel off (black) and 1 is pixel on (cyan).

.. image:: images/display-line.png
   :width: 300
   :align: center
   

Display Rectangle
-----------------

This block displays a rectangle starting at location given by the values  x, y  with a width and 
height given by the results of the value blocks attached to those parameters.

The **fill?** box when ticked fills the rectangle with visible pixels.

.. image:: images/display-rectangle.png
   :width: 300
   :align: center
   

Display Text
------------

This block enables the display of the attached output of the attached value block (ie “Hello”) at 
the location specified by the value blocks at x and y on the display, with the colour being the 
value block output of 0 or 1.

.. image:: images/display-text.png
   :height: 60
   :align: center
   


.. note::    The (x, y) coordinate is where the bottom left corner of the display text is positioned.


Display Image
-------------

This block allows for the creation of an 8 x 8 pixel array positioned on the Kookaberry display at the coordinates of x and y.

The **transparent?** box if ticked will not extinguish any pixels that were already on, thereby giving an 
impression of transparency.

By manipulating the values of x and y using value blocks, the pixel array can be made to move 
around the screen.  

Larger pixel arrays can be created by using multiple **Display Image** blocks with adjacent coordinates (by incrementing x and y in multiples of 8).

.. image:: images/display-image.png
   :width: 300
   :align: center
   
