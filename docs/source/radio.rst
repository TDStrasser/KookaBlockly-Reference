Radio
=====



The Kookaberry is equipped with a built-in digital radio transceiver than is able to send and 
receive small amounts of digital data.  The length of the messages that can be sent is 30 bytes or 
less when using KookaBlockly.  Other radio parameters such as the radio channel and speed of 
transmission are also set to default values.  Discussion of altering these parameters (channel, 
speed and message length) is beyond the scope of this manual.

 


Radio Receive
-------------

 


This is a control block which contains actions that will be taken when a message is received by the radio.  If no message is received then no actions within the scope of the block will be taken.



Radio Read
----------

 

This value block will read the first radio message in the queue of radio messages received. Once read the radio message is deleted from the message queue.

Radio Send
----------

 

This action block sends the data within the attached value block as a message via the radio to be received by all other radios on the same channel.  The data can be the result of a value block, or be a fixed message as shown above.  The length of the message must conform to the 30 byte message length limit or else a program error will result.  Typically an alphanumeric text character occupies only one byte but some special characters may occupy two or more bytes.



.. HC-12 Radio to be added
