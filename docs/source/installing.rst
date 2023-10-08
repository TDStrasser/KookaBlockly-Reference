Installing KookaBlockly
=======================

KookaBlockly is part of the KookaSuite set of code development and editing tools for the Kookaberry microcomputer and other microcomputer boards that can use the Kooka firmware.

The tools that are in KookaSuite are:

KookaBlockly
  a powerful standalone graphical editor designed for creating program scripts.

KookaIDE
  a text editor for creating and editing MicroPython program scripts and directly interacting with the Kookaberry control console.

  *IDE is short for Integrated Development Environment.*

KookaTW
  A virtual Kookaberry user interface that replicates the physical user interface on a Kookaberry and provides a user interface for compatible microprocessor boards that do not have a physical user interface.

  *TW originated as Teacher's Window, but also stands for TWin.*

Downloading KookaSuite
----------------------

The latest version of KookaBlockly can be conveniently downloaded from the Kookaberry Github repository at https://github.com/kookaberry/kooka-releases/releases.

Choose the latest version compatible with your personal computer.  KookaSuite versions available are for:

* Microsoft Windows V10 and later

* Apple MacOS V10.15 and later

* Raspian for the Raspberry Pi

Click on the hyperlink for the appropriate version of KookaSuite and download it to a folder (default is in the **Downloads** folder) on your personal computer.

Installing KookaSuite on Microsoft Windows
------------------------------------------

Double-click on the downloaded KookaSuite-1_9_0-Win64.msi file to launch the Windows Installer.


Installing KookaSuite on MacOS
------------------------------

Double-click on the downloaded KookaSuite-1.9.0-macOS.dmg file to launch the MacOS Installer.


Installing KookaSuite on Raspberry Pi
-------------------------------------

Unzip the downloaded `KookaSuite-1.9-RPI400.tgz` file into the home folder.  This will create a folder containing the three executables KookaBlockly, KookaIDE and KookaTW.

Using the terminal program, install the needed Qt5 modules:

.. code-block:: sh
   :caption: Installing QT5

   sudo apt install libqt5webkit5
   sudo apt install libqt5websockets5-dev
   sudo apt install libqt5serialport5

If desired, create Raspberry Pi menu items under `Programming` using the `Preferences/Main Menu Editor`.
