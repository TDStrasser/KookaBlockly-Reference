Buttons
=======

The Kookaberry has four buttons beneath the display labelled A, B, C and D.  

These buttons are coloured ``A`` red, ``B`` green, ``C`` blue, and ``D`` yellow.  

.. figure:: images/kberry-front-photo.png
   :width: 300
   :align: center
   
   Kookaberry - front view


Button functions are also available on the virtual Kookaberry which is shown when KookaBlockly's **Show display** button is clicked.

.. figure:: images/kberry-virtual-blank.png
   :width: 300
   :align: center
   
   Virtual Kookaberry


Button blocks are used to specify the actions to be taken when a specific button is pressed.

.. figure:: images/buttons-palette.png
   :width: 300
   :align: center
   
   The palette of KookaBlockly Buttons blocks


Each block is described in turn below.

When Button Was Pressed
-----------------------

This is a control loop that performs the actions contained within it whenever the selected 
button *was pressed*. 

The button options are ``A``, ``B``, ``C``, or ``D``.  

*was pressed* means that the actions within the loop will be performed only once after the selected button press.

.. image:: images/buttons-when-was-pressed.png
   :width: 250
   :align: center


When Button Is Pressed
----------------------

This is a control loop that performs the actions contained within it as long as the selected 
button *is pressed*. 

The button options are ``A``, ``B``, ``C``, or ``D``.  

*is pressed* means that the actions will be performed repeatedly as long as the selected button is being pressed.

.. image:: images/buttons-when-is-pressed.png
   :width: 250
   :align: center


Button was pressed
------------------

This is a value block whose result is ``True`` (= ``1``) whenever the selected button was pressed.  

The button options are ``A``, ``B``, ``C``, or ``D``.

After this value block is used its output reverts to ``False`` (= ``0``) until the next time the button was pressed.

.. image:: images/buttons-was-pressed.png
   :width: 250
   :align: center


Button is pressed
-----------------	
This is a value block whose result is ``True`` (= ``1``) as long as the selected button is being pressed.  

The button options are ``A``, ``B``, ``C``, or ``D``.

Th output of this value block reverts to ``False`` (= ``0``) when the button is not being pressed.

.. image:: images/buttons-is-pressed.png
   :width: 250
   :align: center


Exit Program
------------

This is a combination of two blocks: the **button was pressed** control loop, as described above, and the **exit program** action.

The result of using this combination is whenever the button selected was pressed the currently running program will finish.

.. image:: images/buttons-when-was-pressed-exit.png
   :width: 250
   :align: center

