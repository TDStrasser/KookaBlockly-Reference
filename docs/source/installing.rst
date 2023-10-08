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

1.  Double-click on the downloaded ``KookaSuite-<version>-Win64.msi`` file to launch the Windows Installer.  The following display will then appear.

.. figure:: images/win-install-1.png
   :width: 400
   :align: center

   Click on **Next** to proceed.


2.  KookaSuite does not (as yet) have an application trust certificate, so Windows Defender will alert you with the following dialogue.

.. figure:: images/windows-protect1.png
   :width: 400
   :align: center

   Click on **More info** to proceed to the next dialogue.

.. figure:: images/windows-protect2.png
   :width: 400
   :align: center

   Click on **Run Anyway** to proceed.

3. The installer will then show the **Kookaberry Licence Agreement**.  The agreement contains a liability disclaimer, then a series of open-source licences for the software that is embedded within KookaSuite.

   To obtain a printed copy of the licence, press **Print**.

   Please read the licence conditions and if you accept them, click on the acceptance checkbox to place a tick (as shown) and then click on **Next**.

.. figure:: images/win-install-2.png
   :width: 400
   :align: center

   Click the checkbox to accept the licence, then click on **Next** to proceed.


4. A dialogue will then appear showing where on your computer the KookaSuite programs will be installed.  

   Usually the default location of ``C:\Program Files\Kookaberry\KookaSuite`` is fine, but your or your system administrator may wish to put them elsewhere.  If so, click on **Change** and select the prefered location using the file explorer dialogue which will open.

.. figure:: images/win-install-3.png
   :width: 400
   :align: center

   Installation location dialogue. Click on **Next** to proceed.

5. The next dialogue specifies the folder in which KookaSuite will store files.  

   The default location is ``C:\Users\Public\Kookaberry Scripts\`` which all users share on a Windows PC.  If another location (for example) ``C:\Users\<your account>\Kookaberry Scripts\`` which is unique and private to <your account>) is desired, click on **Change** and select the prefered location using the file explorer dialogue which will open.

.. figure:: images/win-install-4.png
   :width: 400
   :align: center

   Scripts location dialogue.  Click **Next** to proceed.

6. A dialogue that provides the opportunity to select which elements if not all of KookaSuite are to be installed.  It is recommended that all elements be installed for a fully functional KookaSuite.

.. figure:: images/win-install-5.png
   :width: 400
   :align: center

   Press **Install** to proceed with the KookaSuite installation.

7. A dialogue with a progress bar that tracks the installation progress will appear.

   There may be a Windows alert asking for permission to proceed.  Accept the installation by clicking **Yes**.

   The progress bar will then continue and when it reaches completion the Completed dialogue will appear. 

.. figure:: images/win-install-7.png
   :width: 400
   :align: center

   Click on **Finish** to exit the Windows Installer.

Installing KookaSuite on MacOS
------------------------------

1.  Double-click on the downloaded ``KookaSuite-<version>-macOS.dmg`` file to open it.  You will see it contains the three KookaSuite apps.

.. figure:: images/mac-install-1.png
   :width: 400
   :align: center

   The contents of the MacOS KookaSuite download package.


2.  Create a suitably named folder in the Macintosh ``Applications\`` folder and drag the KookaSuite apps into it, as shown below.

    KookaBlockly will then be available to launch (as will KookaIDE and KookTW) from the Applications icon in the Macintosh taskbar and by any other regular methods for starting Macintosh applications.

.. figure:: images/mac-install-2.png
   :width: 400
   :align: center

   KookaSuite apps copied to the Applications folder.




Installing KookaSuite on Raspberry Pi
-------------------------------------

Unzip the downloaded ``KookaSuite-<version>-RPI400.tgz`` file into the home folder.  This will create a folder containing the three executables KookaBlockly, KookaIDE and KookaTW.

Using the terminal program, install the needed Qt5 modules:

.. code-block:: sh
   :caption: Installing QT5

   sudo apt install libqt5webkit5
   sudo apt install libqt5websockets5-dev
   sudo apt install libqt5serialport5

If desired, create Raspberry Pi menu items under `Programming` using the `Preferences/Main Menu Editor`.

Script Folders
--------------

During installation or first running KookaSuite, the ``Kookaberry Scripts\`` folder will be created in the location specified during the installation process.  If the ``Kookaberry Scripts\`` folder already existed it will not be altered.

.. figure:: images/win-install-folders.png
   :width: 500
   :align: center

   The Kookaberry Scripts folder in a fresh KookaSuite installation.


The ``Kookaberry Scripts\`` folder contains two sub-folders:

* ``KookaBlockly\`` where KookaBlockly stores the program scripts created by it.
  
* ``KookaIDE\`` where KookaIDE stores MicroPython scripts. 
 
It is permissible to create sub-folders within the ``KookaBlockly\`` and ``KookaIDE\`` folders for different projects.  

The script selection drop-down boxes in KookaBlockly and KookaIDE will however only scan the first level of sub-folders for scripts.

