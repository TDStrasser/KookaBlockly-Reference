--------
Advanced
--------




The Advanced Category is provided to extend the capability of KookaBlockly by allowing the 
definition of additional blocks using Python programming statements.  This category is available 
to the more advanced user as a way of transitioning from KookaBlockly to Python scripts, and 
also to add extended functionality such as using special sensors and actuators and other 
Kookaberry peripherals, or using Python module libraries.

 


Python Value Block
------------------

 


This value block allows the result of any Python statement to be passed to KookaBlockly sockets.  
The Python statement is typed into the text box in the block.  In the default block, the statement 
results in the value 2.






Python Action Block
-------------------

 

This action block permits any Python statement to be inserted into a KookaBlockly program.  The 
statement is typed into the text box in the block.
Typical usage might be to import a library module “import math”, or “import sensor”, or 
anything else that is permitted in Python syntax.

.. code:: Python

    import machine, kooka 

    # A comment

    while True:
      time.sleep(0.5)
      if kooka.button_a.was_pressed():
        raise SystemExit

      machine.idle()



