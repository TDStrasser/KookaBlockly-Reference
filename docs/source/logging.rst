Logging
=======




The Kookaberry contains a 4 megabyte non-volatile serial memory store which is used to store 
files.  These files can be written and read by the Kookaberry and via a USB interface by any 
attached computer.

These blocks provide a facility for writing and reading files.

 


Clear File – data.csv
---------------------

 











Text may not be relevant now

The file write action block opens a text file for writing in append mode. That is, if no file exists a 
new file is created, otherwise the text to be written is appended to the end of the existing file.
The name of the file is specified in the “to file” parameter.  This can be any legal filename, 
usually in the form ‘name.typ’  where name is a text string and typ is a short, usually three letter, file type description.  
Common types are: “txt” for text files; “log” for log text files, “csv” for 
comma separated variable file.  File type conventions are determined by the computer operating 
system that will read these files.
The next parameter “log” is prepopulated with a value block giving the Kookaberry’s time, but 
this can be replaced by any other value block.
A second value block will be written to the same line in the file separated by a comma.  The 
value block should return a string of text characters.
Each time this block is run a new line will be appended to the end of the specified file.

.. {NOTE:     We should have a file readline block as well]    Not sure whether this comment is current




Log Timestamped Value
---------------------

 

TEXT TEXT TEXT

Log Two Timestamped Values
---------------------

 


TEXT TEXT TEXT





 
