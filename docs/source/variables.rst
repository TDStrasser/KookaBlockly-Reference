---------
Variables
---------

Variables are a way of creating and manipulating a named value, in the same way that algebra uses names to refer to a value.  
A **Variable** is useful as a named container to store a value for later use in one or more places in a KookaBlockly script.

Examples of typical variable names are **X**, **Y** and **Z** when referring to cartesian coordinates; **H**, **W** and **D** as dimensions of an object; 
and **i** or **j** as an index into a list.  Variable names can of course be longer, for example **height**, or **temperature**

When KookaBlockly is first started, or when a new script is started, the **Variables** palette looks like this:


.. figure:: images/variables-create.png
   :width: 300
   :align: center
   
   The initial Variables palette


Create Variable
---------------

Clicking on “Create variable”  brings up a dialogue box where the user can define the variable's name.  
Type in a name and then click on **OK**.  The figure shows an example name ``"my_variable"``.


.. image:: images/variables-create-dialog.png
   :height: 200
   :align: center



Once a new variable has been created, the new variable will be available in the **Variables** palette.


.. image:: images/variables-create-post.png
   :height: 300
   :align: center

It is possible to right-click while hovering over the variable block in the palette to reveal a number of actions 
which can be selected by then clicking on them:

1. **Delete the variable** - removes the variable, and its associated blocks if it was the only variable.
2. **Rename the variable** - brings up a dialogue box, as for creating a variable, in which the new name can be typed.  
   The new name must contain at least one visible character and not be the same as any other variable.
3. **Help** - this option does not yet work. It is intended eventually to display Help text.

.. image:: images/variables-right-click.png
   :height: 300
   :align: center


Set Variable
------------

Using this block, a value can be assigned to a variable by attaching a value block to its input.  
The value can be a number, a boolean, or a character string.

The variable to be assigned the value can be selected from the drop-down-list.

.. image:: images/variables-set.png
   :height: 80
   :align: center

The drop-down list also has some other choices:

1. **Rename variable** - brings up a dialogue box in which the new name can be typed.  
   The new name must comprise at least one visible character and must not be a duplicate name.
2. **Delete the variable** - removes the variable and its associated blocks from the script.

.. image:: images/variables-set-dropdown.png
   :height: 120
   :align: center



Change Variable
---------------

This action block allows the user to change the selected variable by a number specified by the input numerical value.

This block will only work for numerical variables and will only accept numerical values.  
Character strings and boolean values will not be accepted.

.. image:: images/variables-change.png
   :height: 80
   :align: center

This examples illustrates how this block may be used as a counter.
Three variables are set up: ``count_b``, ``count_c`` and ``count_d`` to count the number of times buttons B, C and D are pressed.
The running totals are printed on the Kookaberry's display.

.. image:: images/variables-change-example.png
   :height: 500
   :align: center

 

.. image:: images/variables-change-example-display.png
   :height: 200
   :align: center


Variable Value
--------------

This value block allows a user to attach a variable’s value to the input of another block.


.. image:: images/variables-value.png
   :height: 80
   :align: center

This example reads a temperature from a sensor once per 5 seconds, storing it in a variable named ``"temperature"``, then using the stored value to perform a conversion calculation 
and display the original and converted values on the Kookaberry display:


.. image:: images/variables-example.png
   :height: 400
   :align: center

