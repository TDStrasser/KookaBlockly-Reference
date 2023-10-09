-------
Control
-------

Control blocks direct program flow or provide time-related functionality.

.. figure:: images/control-palette.png
   :width: 300
   :align: center
   
   The palette of KookaBlockly Control blocks


Each block is described in turn below.

On Start
--------

The "on start" block is intended to contain other action blocks that will run first and only once when the KookaBlockly script starts.

Typically the blocks contained are for the initialisation of the display, variables, sensors, and actuators.

.. image:: images/on-start.png
   :width: 150
   :align: center


Scheduled Loop
--------------

This block is a loop that repeatedly runs the blocks nested inside at the time interval specified in the numeric box. 

The loop will continue forever at the defined period unless the program is externally stopped.

The time specification is a number in decimal seconds, for example: 1 is 1 second, and 0.001 is 1 millisecond.

.. image:: images/scheduled-loop.png
   :width: 150
   :align: center


Every Loop
----------

This block runs the blocks nested inside in a repeated loop.  

The loop will run forever unless externally stopped by exiting the script, or resetting the Kookaberry or removing power from the Kookaberry.  

Another name for this block is the Repeat Forever loop.

.. image:: images/every-loop.png
   :width: 150
   :align: center


Exit Program
------------

This block directs the running program to exit.

.. image:: images/exit-program.png
   :width: 150
   :align: center

Sleep
-----
 
This block causes the program to wait / pause for the specified time before continuing to the next block.  

The number in the box specifies the duration of sleep in decimal seconds.

.. image:: images/sleep.png
   :width: 200
   :align: center


Time (s)
--------

This block returns a value in whole seconds since the Kookaberry’s epoch time ( 00:00:00 on 1st 
January 2000).  

By subtracting successive values given by this block, the elapsed interval in 
seconds between the samples may be calculated which is useful for timing functions.

.. image:: images/time-secs.png
   :width: 150
   :align: center


Time (ms)
---------

This block returns a value in milliseconds since the Kookaberry’s epoch time (00:00:00 on 1st 
January 2000).  

By subtracting successive values given by this block, the elapsed interval in 
milliseconds between the samples may be calculated which is useful for high-resolution timing functions.

.. image:: images/time-msecs.png
   :width: 150
   :align: center
