---------
Actuators
---------




The Actuators  category focuses on the internally supported 90 deg, 180 deg and 360 deg Servos 
Motors – typically called Hobby Servos.  These Servos typically have a built in motor, a feedback 
circuit and a motor driver. 

The supported servo motors have a three pin connector being (a) ground, (b) power and (c) 
servo signal.   Whilst different servos can have different operating voltages a typical Hobby Servo 
operates around 4.5 to 6 volts.  It may be possible to drive some small servos directly from the 
Kookaberry however it is usual to operate the servo from a separate power supply due to 
required servo voltage being higher than Kookaberry internal operating voltage of 3.3 volts.  Also 
when under power the servo current requirements can be larger than what can be supplied by 
the Kookaberry

Motors operate differently from servos and are typically controlled by a PWM (pulse width 
modulation) signal. See the Pins category where other forms of output such as PWM (pulse 
width modulation) are described.


 










Servo – Set to Angle
--------------------

 

A servo is a motor that rotates over a fixed angular range.  Servos are used in remote-controlled 
vehicles and robots for example.
The servo block sets the angle to which a servo motor should move specified in degrees.  The 
angle can be calculated by other value blocks or be specified as a fixed value.  The option for this 
block is which connector the servo is attached.

.. note:
  Please note that all but the smallest 9g servos should not be directly plugged into a 
  Kookaberry connector.  These devices require special electronics to supply them with more power.  
  Plugging in large servos without the necessary driving electronics may irreparably damage the Kookaberry!

Servo – Set to Angle over Time
------------------------------

 




Servo - Speed
-------------








Servo – Speed over Time
-----------------------


 






 
