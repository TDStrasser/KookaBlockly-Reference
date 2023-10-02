Lists
=====

A list is an array of zero or more items which can be variables, numbers, characters or text.
The usual usage is to create a variable and set its value to that returned by the list blocks.















Create Empty List
-----------------





This value block gives back a new, empty list.  The gear icon in the block allows the user custom
 tailor the block.



Create List With
----------------










This value block creates a new list with the socketed items.  The block can be configured with the 
gear icon to add or remove sockets.

Here is an example of setting the value of a variable called “letters” to a list of the names of
 Greek letters: [“alpha”, “beta”, “gamma” and “delta”]

 

Create List With Item Repeated No. of Times
-------------------------------------------

 

This action block creates a new list with the left-hand socketed item repeated several times as 
specified by the number inserted into the right-hand socket.

In this example, a variable called ”listofnumbers” is set to a list of the number “123” repeated 5 
time, that is: [123, 123, 123, 123, 123]

 






Length Of List
--------------

 

This value block represents the number of items in the socketed list.

In this example a variable “L” is set to the number of items in the list [“alpha”, “beta”, “gamma” 
and “delta”] in the variable “letters” which is 4

 

Is Empty
--------

 

This value block represents whether the socketed list is empty (i.e. has no items in it) and is True 
if the list is empty or False if the list has members.





In List Find First / Last Occurrence of Item
--------------------------------------------

 

This value block gives back the index in the list at which the item was found, if it was found.  If it 
was not found it gives a -1 instead.  The first item in a list has an index of 0.  The first socketed 
item allows for a user to name a variable which is a list, and the second socketed item specifies 
the value that is being searched for.

In this example we search for the first occurrence of “gamma” in the variable “letters” 
comprising the list [“alpha”, “beta”, “gamma” and “delta”] and set the variable “place” to the 
index of “gamma” which has a value of 2 being the third item with the index count beginning at 
0.

 







In List Get / Remove Item
-------------------------

 

This value block operates on a list to retrieve, retrieve and remove, or just remove an item at a 
particular position in the list.  The value of the list item is returned as the result of the block.
The graphic shows the choices available in each element of the block.  















In this example, the variable item is set to the result of getting the item with index 2 from the list 
in the variable “letters”.  The result passed to “item” will be “gamma”

 


In List Set / Insert Item
-------------------------

 

This action block either changes the value of an item at a specified location to the socketed value 
or inserts a new item with the socketed value at the specified location in a chosen list.











By way of example, we may wish to add “epsilon” to the end of the list in “letters”:

 

In List Get Sub-List From Index to Index
----------------------------------------

 

This value block allows a user to get a portion of a chosen list as another list.  The portion starts 
from the first chosen location and ends at the second chosen location













In this example a smaller list is assigned to variable “subletters” comprising the “letters” list from 
index number 1 to 3 inclusive.  The results is [“beta”, ”gamma”, delta”]


 













Make List With Delimiter
------------------------

 

This value block either parses a text string into items separated by the delimiter text and 
arranges the items into a list; or it takes the items in a list and concatenates them into a text 
string separated by the delimiter text.









An example is to parse a text string into a list.  The text string contains the first four Greek letters 
separated by commas.  The results is a list of the Greek letters as the variable “letters”.

 

The complementary operation is to generate the original text from the list “letters” and to print 
it on the Kookaberry’s display.

 














Sort List
---------

 

This value block allows a list to be sorted by numeric or alphabetic order in an ascending or 
descending format. The options for each element in the block are shown below.











The example prints the items in the list “letters” on successive rows of the Kookaberry display in 
alphabetical order:

 






 
