Clock
=====

The blocks in the Clock category provid the functions to read and set the electronic real-time-clocks (RTCs).  

The Kookaberry has an internal RTC which defaults to a time of 00:00:00 on 1 January 2015 when the Kookaberry is turned on.  The Kookaberry itself does not retain the time which may have been previously set as it has no internal battery to keep the internal clock running.

When the Kookaberry is connected to KookaBlockly, its internal RTC is updated to the time on the hosting computer.

An external RTC, connected as an accessory to the Kookaberry, usually has a battery and therefore maintains the time that has been previously set on it.  This provides a convenient way for the Kookaberry to obtain the correct time when it is not tethered to KookaBlockly (or KookaIDE or KookaTW).

Clicking on the Clock category in the KookaSuite palette reveals the available blocks, as below.  Click and drag any of the required blocks to the KooaBlockly workspace and connect with other blocks to build a script that can use and/or set the time.

.. figure:: images/clock-palette.png
   :width: 300
   :align: center
   The palette of KookaBlockly Clock blocks

Each of the Clock blocks is described in the following sections.

--------------
Internal Clock
--------------

Get Clock – Simple Time
-----------------------

Reads the Kookaberry’s internal Real Time Clock (RTC) and returns a date or time in the chosen format selected from the drop-down menu on the block.  The value returned is a character string.

.. image:: images/get-clock-simple.png
   :width: 250
   :align: center


Get Clock - Extended Time
-------------------------


Reads the Kookaberry’s internal Real Time Clock (RTC) and returns the date and time in two parts per the selected formats and separated by a string of characters that can be specified by the user (the default separator is the minus character “-“).

.. image:: images/get-clock-extended.png
   :width: 400
   :align: center


Below is a KookaBlockly example script demonstrating a loop which updates the Kookaberry’s display every second with the current time and date

.. figure:: images/get-clock-extended-script.png
   :width: 300
   :align: center
   A KookaBlockly Script that shows the current time and date on the Kookaberry display.

.. figure:: images/get-clock-extended-display.png
   :width: 200
   :align: center
   The Kookaberry display resulting from the example KookaBlockly Script.


 
--------------
External Clock
--------------

Get External Clock  YYYY/MM/DD
------------------------------


Get External Clock YYYY/MM/DD – hh:mm:ss
----------------------------------------


Set Internal Clock from External Clock
--------------------------------------


Set External Clock from Internal Clock YYYY/DD/MM
-------------------------------------------------


Set External Clock from Internal Clock YYYY/MM/DD – hh:mm:ss
------------------------------------------------------------


