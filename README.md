# Tutedude-Python-Assignments (1 - 5)
  This repository contains Assignments 1-5 of the Python course of tutedude.

ASSIGNMNENT 1

Task 1: Perform Basic Mathematical Operations
  Problem Statement: Write a Python program that does the following:
    1.  Takes two numbers as input from the user.
    2.  Performs the basic mathematical operations on these two numbers:
      o	Addition
      o	Subtraction
      o	Multiplication
      o	Division
  3.  Displays the results of each operation on the screen.

How to solve the Problem:
  1. Take the input of two numbers from the user: Enter number 1, and enter number 2.
  2. As input is always strings, but we need arithmetic operations to be performed, hence we need to convert the input from strings to integers by adding "int (input)".
  3. Now that we have integers, we can give the command for printing the addition, subtraction, multiplication and division of two numbers.
  4. Run the code and it will first ask to enter number 1, once entered it will ask to enter number 2 and then after pressing enter it will display the result of these four arithmeic operations on the screen.

Task 2:  Create a Personalised Greeting
  Problem Statement: Write a Python program that:
  1.  Takes a user's first name and last name as input.
  2.  Concatenates the first name and last name into a full name.
  3.  Prints a personalised greeting message using the full name.

How to solve the problem:
  1. Start by entering the input command for the user to enter the first name and last name, just like we did in task 1.
  2. As input is by default taken as a string and here we have names (strings), hence we do not have to convert and directly add them (Concatenate first and last name) by simply putting '+' between two strings.
  3. But, here's a thing, as we add string, it will be added as the input is; for eg: first name = John last name = doe. then adding both will give Johndoe.( no space in between). Hence, we will give spaces in " " to add this space.
  4. "string 1" + "string 2" will give you the result as - string 1string 2. To add space in between them, we will give space before string 2 as -" string2".
  5. Run the code with your desired greeting.

ASSIGNMNET 2

TASK 1: To Check if a Number is Even or Odd.

Steps to solve the problem:
1. Take the integer input [int(input)] for user to enter the number.
2. State the if condition to check if dividing the entered number by 2 will give a remainder of 0.
3. Give the print command to print the 'number is even' if the condition is true, else to print it is an odd number.

TASK 2: Find Sum of Integers from 1 to 50 Using a Loop

Steps to Solve the problem:
1. Start the for loop command and specify the range from 1 to 51 as in range the last number is excluded and here in problem we want '50' to be included in the sum
2. Give the print command to print the sum of the range(1,51).
3. Now, if you run the code gere it will print the result 50 times but we want it to print only once hence we will add 'break' after giving the print command.
4. 'Break' will stop the loop and give the desired output statement. 
