Pins
====




Pins are electrical connectors on the Kookaberry.  The Kookaberry circuit board has five plugs on 
the rear numbered P1 to P5.  P3 has four pins and the rest have 3 pins.  On each connector two 
of the pins are used for positive and negative power connections.  The remaining pin(s) have 
multiple uses as digital or analogue inputs or outputs.

The Pins category provides the means to control what the pins do.


.. note::
  NOTE:   In each of the Pins blocks the dropdown box may be replaced by a 
  String.   i.e.   Drag the dropdown box out of the Block and replace by a string 
  from the Strings category

		



Pin ON
------


The Pin ON block causes the selected pin to be used as a digital output and to be turned on 
(output voltage is +3.3 volts DC).

Pin OFF
-------

The Pin OFF block causes the selected pin to be used as a digital output and to be turned off 
(output voltage is 0 volts DC).

Toggle Pin
----------


The  Toggle Pin block causes the selected pin to be used as a digital output and toggled on / off. 
(output voltage is either 0 volts (OFF) or 3.3 volts (ON))

Set Pin to Digital (1)
----------------------

 

The Set Pin to Digital (1) block causes the selected pin to be set to a digital output 1 being ON 3.3 
volts dc and 0 being OFF 0 v dc.


Get Pin Digital Value
---------------------
 

This value block designates the selected pin as a digital input and returns the digital value of the 
input as either 0 (if the input voltage is closer to 0 volts) or 1 (if the input voltage is closer to +3.3 
volts DC).

.. note::
  Please note that applying negative voltage or voltages greater than 3.3 volts DC to the Kookaberry’s connectors may irreparably damage the     Kookaberry!



Pin Voltage
-----------

 
This value block designates the selected pin as an analogue input and returns an integer 
corresponding linearly to the value of the input in the range 0 (for 0 volts) to 4095 (for +3.3 volts 
DC).

.. note::
   Please note that applying negative voltage or voltages greater than 3.3 volts DC to the Kookaberry’s connectors may irreparably damage the Kookaberry!


Pin – Voltage Percent
---------------------
 

This value block designates the selected pin as an analogue input and returns an integer 
corresponding linearly to the value of the input in the range 0 (for 0 volts) to 100 (for +3.3 volts 
DC).

.. note::
  Please note that applying negative voltage or voltages greater than 3.3 volts DC to the Kookaberry’s connectors may irreparably damage the  Kookaberry!

Pin – Set Volts Out
-------------------

 

Where available on the Kookaberry the Pin set volts out block causes the selected pin to be used 
as an analogue output and to be set to the voltage which is the result of the attached value 
block.  This feature is not available on Kookaberry using the RP2040 microprocessor


Pin – Scale Volts Out
---------------------
 
 

Where available on the Kookaberry the Pin scale volts out block causes the selected pin to be 
used as an analogue output and to be set to the voltage which is the product of the results of the 
attached value blocks.  The first value block is interpreted as a percentage in the range 0 to 100,
 and the second value block provides the maximum voltage (with 3.3 volts being the maximum 
that can be produced by the Kookaberry).   This feature is not available on Kookaberry using the 
RP2040 microprocessor


Pin – Pulse Width Modulation (PWM)
----------------------------------

 

Pulse Width Modulation (PWM) oscillates the selected Pin as a digital output between 0 (0 volts) 
and 1 (+3.3 volts DC) at a given frequency and duty cycle.  The duty cycle is the proportion of 
each oscillation in which the output state is set to 1.  The example duty cycle of 50% above 
means that the oscillation is 0 for 50% of the time and 1 for the remaining 50%.

Both frequency and duty can be derived from value blocks or specified directly as shown.

PWM is used to apply speed control to DC motors by varying the duty cycle from 0% (motor is 
stopped) to 100% (motor at full speed). Additional circuitry is required to deliver the electrical 
power that a motor requires.

PWM can also be used to play tones through a loudspeaker by varying the frequency according 
to the pitch required.  A frequency of 440Hz corresponds to the musical note of middle A on a 
piano, for example.  Duty cycle is usually set to 50% but other interesting harmonics may be 
produced by varying the duty cycle over a limited range around 50%.  Additional circuitry is also 
required to successfully drive a loudspeaker.

.. note::
  Please note that motors and loudspeakers should not be directly plugged into a Kookaberry 
  connector.  These devices require special electronics to supply more power.  Plugging in 
  motors or loud speakers without the necessary driving electronics may irreparably damage the Kookaberry





