# The “New Student Information Database” Python Script
*ASimpson, 03/06/2020*

## Introduction:
In this module and assignment, I learned about creating Python scripts that use files to store and access information.  
I also learned how to use “pickle” as a python way to store obscured data in a .dat binary file.  Finally, I learned 
all about how to handle errors that my code might generate.  

Specifically, I learned about: 
 - How to Read data from text files
 - How to Write Data from text files
 - How to Read/Write more complex data from binary files
 - How to intercept and handle errors during a program’s execution
 I also learned a bit more about GitHub web pages, how to use create a blog article to demonstrate python 
programming concepts.  

## Working with Text Files:
I learned on page 190 of Chapter 7, that with Python, it’s easy to read strings from plain text files-files that are 
made up of only ASCII characters.  Text files are a good choice for permanently storing simple information, for a 
number of reasons.  First they are cross-platform.  A text file on a windows machine is the same as a text file on a 
Mac.  Second, text files are easy to use.  Most operating systems come with basic tools to view and edit them.

### Reading text files:
Python makes working with files easy, but there may be some confusion because of the different ways you can work with files. For instance, there are several ways to read the data from a file. Here’s a look at some common examples.
The readline() function:
Each time you call the readline() method, gets one line of data and advances to the next line. Advancing one line at a time is commonly referred to in programming as a cursor. Note that since I closed the file, any additional calls to my read_data() function read the same first row of data! 

### Using a “while” Loop:
If you want to get data from additional lines you must call the readline() method repeatedly. One way to call the readline() method repeatedly is to use a "while" loop.

### The readlines() function:
Python's readlines() function, reads all the lines in a file, and returns a list. The readlines() function is different than the read() function, which reads all the lines in a file and returns a string.

### Using a “for” Loop:
Yet another option to read multiple rows of data using a "for" loop. One small advantage of using the “for” loop is that it automatically closes the file when it reaches the end of the file's data.
