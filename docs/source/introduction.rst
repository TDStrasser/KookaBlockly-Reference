Introduction to KookaBlockly
============================

**KookaBlockly**: Graphical Programming Editor for Kookaberry Microprocessor Boards
-------------------------------------------------------------------------------

**KookaBlockly** is a powerful standalone graphical editor designed for creating program scripts for Kookaberry and related microprocessor boards. 
This editor operates on a drag-and-drop interface, making it beginner-friendly and highly intuitive. 
It's built upon the open-source Google Blockly library (Apache 2 license), created by Google to facilitate the development of beginner-friendly programming languages.

A **KookaBlockly** script is assembled from graphical function blocks dragged onto the workspace from the palette of blocks on the left of the display.  
The blocks click together like pieces of a jigsaw puzzle to form a series of steps that the Kookaberry microcomputer will perform.

.. figure:: images/kblockly-welcome-script.png
   :width: 80%
   :align: center


   This is the **KookaBlockly** display with an example **KookaBlockly** script. 

The example shown above shows a loop that writes a welcome message on the Kookaberry display and flashes the Kookaberry's LEDs.  
It then sleeps for 2 seconds and then goes back to the beginning of the loop.  The loop will run until the Kookaberry is reset or power is removed.

**KookaBlockly** was meticulously crafted by Damien George (George Robotics – MicroPython) in collaboration with Kookaberry Pty Ltd. 
It also received support from the AustSTEM Foundation, the Warren Centre, and the Vonwiller Foundation.

Key Features
------------

Intuitive Graphical Interface: 
    Users can create syntactically correct scripts and programs effortlessly, 
    even without prior knowledge of any programming language.

    **KookaBlockly** enables users to assemble graphical blocks into structured MicroPython (Python 3.0) code.

Compatibility: 
   The generated code can be utilized on most microprocessor boards that use MicroPython, 
   but is particularly suited to those with Kookaberry firmware for STM and RP2040 microprocessors.

Platform Compatibility: 
   **KookaBlockly** runs as a standalone program on personal computers with Microsoft Windows 10 or 11, Apple MacOS, or Raspberry Pi Raspbian operating systems.

Easy Access: 
   The latest version of **KookaBlockly** can be conveniently downloaded from the Kookaberry Github repository 
   at https://github.com/kookaberry/kooka-releases/releases.

   Follow the :doc:`installation` guide in the next section to install **KookaBlockly**.

Working with KookaBlockly
-------------------------

Using **KookaBlockly** is straightforward and enjoyable. 

Users can drag and drop graphical code blocks into the workspace, where they can be seamlessly interlocked or snapped together using sockets. 

These sockets represent fundamental code concepts, including program controls (activation, termination, loops, and decisions), actions, and result computations (variables, values, mathematical and logical expressions). 

The intuitive graphical process empowers users to apply programming concepts and principles when designing scripts or programs, eliminating the need to worry about the syntax and semantics of MicroPython. 

With **KookaBlockly**, programming becomes an enjoyable and accessible endeavour.

AustSTEM Learning Hub
---------------------

AustSTEM has assembled a collection of resources on its Learning Hub at https://learn.auststem.com.au.  
These resources complement the material in this manual with examples, lesson plans, descriptions of equipment and of their application.