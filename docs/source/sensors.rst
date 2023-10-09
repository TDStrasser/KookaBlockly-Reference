-------
Sensors
-------


The Kookaberry contains a variety of on-board sensors being a 3-axis accelerometer and a 
magnetic compass, and it also supports two types of temperature sensor and two types of 
combined temperature and humidity sensors.
The Sensors category provides blocks that enable the use of these sensors.

-----------------
Internal Sensors
-----------------

Accelerometer (raw)
-------------------

 


The Kookaberry contains an internal 3-axis accelerometer based on the LMS303 integrated 
circuit.  

The accelerometer block provides the acceleration value of one of the X, Y and Z axes in the 
sensor’s frame of reference.  The X, Y and Z axes are selected via the second drop-down list on 
the right of the block.  The values are in metres per second squared. 

The Kookaberry’s internal accelerometer is oriented so that the X axis is along the horizontal 
dimension of the display, the Y axis is aligned with the vertical dimension of the display, and the 
Z axis is perpendicular to the Kookaberry’s circuit board.

This example shows the X, Y and Z acceleration values being retrieved and displayed once per 
second.  The Kookaberry is lying on a horizontal surface.

 

 

A typical value for acceleration in the Z direction is 9.81 m/sec^2.  This will vary as a function of 
Latitude.  To obtain accurate results from the LSM303 in the X, Y or Z axis calibration may be 
necessary


Accelerometer (scaled)
----------------------

 




The scaled accelerometer compound block is a convenient combination applying a multiplier and an offset to the raw accelerometer reading.  The scale and offset factors are also the results of value blocks.

This block is useful to reduce the sensitivity of the accelerometer and to compensate for offsets in tilt along the selected axis.


Compass
-------

 

The magnetic compass is part of the LMS303 integrated circuit, and the magnetic field strength 
value may be obtained from either the Kookaberry’s internal sensor

The value returned is an integer that is the vector sum of the xyz components of the magnetic 
field experienced by the sensor.

(Missing blocks for compass_get_xyz and compass.get_heading()


----------------
External Sensors
----------------

DS18x20 Temp Sensor
-------------------

 

The DS18x20 is an electronic temperature probe and this DS18x20 value block enables 
reading of the probe and returns the temperature in degrees centigrade.  The option on this 
block enables selection of which connector it is attached to.

The DS18x20 sensor is used for measuring temperature in air and in liquid.  The sensor is pre-
calibrated and performs all of the temperature calculations within the sensor.





NTC Temp Sensor
---------------
 

The NTC (Negative Temperature Coefficient) thermocouple sensor works by varying its 
resistance which lowers as temperature rises.  The Kookaberry performs the necessary 
calculations to convert the sensor’s resistance to a temperature reading in degrees centigrade.

The options on the NTC value block are:
•	The connector to which the sensor is attached
•	The parameters A, B and C are the coefficients used in the Stein-Hart equation that is used to convert thermocouple resistance to temperature.  Explaining this in more depth is beyond the scope of this manual.  It is recommended that the default values not be altered.


DHT11-DHT22
-----------



The Kookaberry supports the DHT11 and DHT22 temperature and humidity sensors.  The option 
on the DHT value block permit the selection of the sensor type (DHT11 or DHT22), the connector 
to which the sensor is connected, and whether to read temperature (in degrees centigrade) or 
relative humidity (as a percentage).

The DHT sensors are for measuring air temperature and the difference between the two sensors 
is that the slightly more expensive DHT22 sensor has a higher level of accuracy and precision.
The manufacturers of the DHT11 and DHT22 recommend a sampling period of greater than 2 
seconds




BME280 Temperature, Humidity and Pressure Sensor
------------------------------------------------

 






External LSM303
---------------

 













LUX Sensor VEML7700
-------------------

 


Power Sensor INA219
-------------------

 

Soil Moisture Sensor
--------------------

 





 
