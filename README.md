CIS 2110
Homework Assignment #7

Learning Objectives: 
 To demonstrate the student's ability to process loops in Python 
Assignment:
 For this homework, you will write several programs.  Each should be a separate program, 
and each should run independently of the other programs.
Program 1
Write a program that asks the user to input an integer value less than 500 (this is variable 
n). The program should then ask the user for a second integer value (which we refer to as x).  
Using a WHILE loop, print all of the numbers that divide x into n and have no remainder.  DO 
NOT use variables x and n in your program- make up your own variable names!!!  I suggest you 
use the “mod” function, which is discussed in section 2.2 of “Python for everyone”.   
For example, you interaction with the program might look something like this:
Please enter an integer that is less than 500:   20
Please enter a second number you want to divide by: 6
6
12
18
Thank you- you are now done!
Program 2a
Write a program that asks the user to input two integer values between 0 and 100 (we’ll 
call these numbers the upper and lower limits).  Using a WHILE loop, print the numbers 
BETWEEN the upper and lower limits.  Next, print the sum of all the numbers between the 
upper and lower limits. Once the program has processed the numbers, output the count of the 
numbers you processed, and the sum of the numbers you processed. For this program use a 
WHILE loop.
Program 2b
Write a program that asks the user to input two integer values between 0 and 100, and print the 
number BETWEEN the numbers that we entered AND the sum of all the numbers between the 
numbers the user input. Once the program has processed the numbers, output the count of the 
numbers you processed, and the sum of the numbers you processed. For this program, 
however, use a FOR loop instead of a WHILE loop.
For loops are covered in section 4.6 of “Python for Everyone”.  
In addition to the book, I suggest watching BOTH of the following videos:
https://youtu.be/6iF8Xb7Z3wQ  
https://youtu.be/94UHCEmprCY   (especially the first 5 minutes)  
And websites:
https://wiki.python.org/moin/ForLoop   (I suggest running the code they show you in the first 
examples!!!)  
https://www.w3schools.com/python/python_for_loops.asp
Program 3
For this assignment, keep in mind that ALL STRINGS are LISTS!  I strongly suggest you review 
section 4.6 of “Python for everyone” and Hasley’s PowerPoint notes about lists and for loops 
that are posted on Canvas.  
The assignment:
Write a program that asks the user for input.  Use a FOR loop to parse the string you get from 
the user, from start to finish.  For each character in the string report out:
If the character is a letter, output the UPPERCASE and LOWERCASE version of the letter.
IF the character is a number, output the letter and the SQUARED value of the number. For 
example, if the character is 3, the program should output “The original is 3” and “The square of 3 
is 9”
If the character is a space, output the string “SPACE”  (all uppercase).
If the character is not a letter, number, or space, output “<character> is a special character!”  
Where <character> is the character you are examining.
So- if I input    Joe3.3 2A
The output should be 
J
j
O
O
E
e
The original is 3
The square of 3 is 9
. is a special character!
The original is 3
The square of 3 is 9
SPACE
The original is 2
The square of 2 is 4
! is a special character!
Program 4
Write a program that asks the user for any number of floating point numbers.  When the 
user is done entering numbers, they should enter “done”.  The program should then print to the 
screen the count of the numbers entered, the sum of the numbers entered, and the average of the 
numbers entered.  
Guidelines:
 For each program, create a header that prints when you run the rile.  The header should 
state your name, the assignment number, the program number, and a brief description of 
what the program does. 
 ALL of your code must always be within this file- you will lose points if you attempt to 
import libraries or code that is external to the file (I’m happy if you can do this, but for 
now let’s keep it simple, k?)
 Give priority to writing CODE THAT WORKS.  If you can’t get part of the code to run, 
comment out that part and tell me (in the comment) what you were trying to do so I can 
give you partial credit.  I will take off points for code that doesn’t run- I shouldn’t have to 
debug your code just to get it to run.      
 I suggest you use comments liberally
