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

ASSIGNMENT 3

TASK 1: 

How to solve the problem:
1. Taking the integer input like previous tasks.
2. Define the function: factorial(entered number).
3. Start the if and else condition to solve factorial and give return statement.
4. Give print command to print the result with desired statement.

TASK 2: 

How to Solve the problem:
1. Like before take the integer input from user.
2. import all from maths (*) - so that you dont have to import every single function.
3. Now print the desired function for the number. to avoid giving print statement again and again use '\n' after every function, this will give the result in new line.


ASSIGNMENT 4

TASK 1:  Read a File and Handle Errors 

How to solve the problem:
1. Create a text file named sample.txt.
2. Start with the 'try' command and open the file with the read command as 'open(sample.txt', 'r'), --> r = read.
3. Now, to read lines one by one start as - ' reading_file1 = file.readline(-1)' to print the first line entirely. Remember to put -1 and not 1 as it will read first character only i.e H.
4. Similarly, repeat the command for line 2 'reading_file2 = file.readline(-2)' to print the second line. Remember to mention the command with reading files 1 and 2 so that you can print it separately as per question.
5. Now give the print command mentioning your desired command before the line which will be printed.
6. Next mention except command for error: file not found.
7. then give final command as 'finally: print()'.
8. lastly close the file as file.close().


TASK 2: Write and Append Data to a File

How to Solve the Problem:
1. Here, first you have to take the user input where user can write the text which they want in file.
2. Use 'with open' (The with open() statement in Python provides a way to automatically manage the opening and closing of files, ensuring that files are properly closed even if errors occur) to first write the text ('w').
3. Print 'data is successfully added to the file'.
4. Remember, here its not necessary for the close command as you have used 'with open'.
5. Directly start with appending the file like above. Take additional input or user input2 (to differentiate from user input).
6. Print 'data is successfully appended to the file'.
7. Now , print the final content with read command and it will give all the contents added and ammended in the file.


ASSIGNMENT 5

TASK 1: Create a Dictionary of Student Marks
1.Create a dictionary with key as name of students and value as their marks. students_marks = {key,value}
2. Now take the input for students name from user.
3. Give the if condition for name to be found in dictionary and print the value of that name else print details not found.


TASK 2: Demonstrate List Slicing 
1. Start by creating a list of numbers from 1 to 10. to avoid writing whole series use the range function (remember that end number in range is not included hence range to list numbers from 1 to 10 would be (1,11). [numbers = list(range(1,11)).
2. To slice first five numbers use 'numbers[0:5]' ot simply 'numbers[:5]' as this means it will start with index zero. hence, first five numbers starting from index zero will be [1,2,3,4,5].
3. next mention reversed five as[5::-1] or [::-1] this means it will start from index 5 and go till last. start:stop:step, and -1 means "go backwards." But this is NOT applied on original list but in first five which we calculated just above. do not add '0'in slice as [5:0:-1] as this will not include the number on zero index (end number or stop number is not included).
4. Positive indexes: start from 0 (left to right), Negative indexes: start from -1 (right to left).
4. Now give print statements for all and run the code.

