# python-codes

**My Python Code** is a collection of code that I have taken my time to write as I continue to learn Python programming language.

The First Python code is a Python Function that checks whether a number belongs to a Fibonacci Sequence or Not when you input any number on the function. Secondly, I did a Python Function that checks if a number is a Prime Number or Not when you input any number on the function.In Addition to those two, I also did another Python Function that checks whether a number is Positive, Negative and/or Zero when you input any desired number to the function.

# FIBONACCI SEQUENCE

## What is Fibonacci Sequence?

**Fibonacci sequence** is a sequence or a series of numbers in which each number is the sum of the two preceeding ones. 

It usually begins with 0 and 1.

Mathematically, it is represented as **Fn = Fn-1 + Fn-2** for n>1 where **Fo = 0** and **F1 =11**.

In this Python code I have used if...elif...else which has four main conditions or expessions.

First, you declare the Python function, using *def Fibonacci(n):*

Secondly, you start with the **If statement** which is your first condition. i.e if **n < 0** the code will print out "Invalid input".

Then **elif statement**, **n == 0** and the code checks if n = 0 then it returns 0 on the interpreter.

Then another **elif statement** **n == 1 or n == 2** and the code checks whether n = 1 or 2 then it returns 1 on the interpreter.

Lastly, **else statement** which will return the *Fibonacci sequence* of numbers greater than 2.

# PRIME NUMBERS

## What is a Prime Number?

**Prime Number** is a whole number and not a fraction or a number with a decimal point, greater than 1 and whose factors are 1 and itself only.

Similarly, In this case, I have used if...elif.else with four conditions.

To begin with, you declare the Python function, using *num = int(input("Enter any number: "))*

Then you start with the **If statement** the first condition. i.e if **num <= 1** then the program will ask you to "Enter a number" and prints out is not a Prime Number depending on what number you choose.

Then **elif statement**, **num> 1** and as you prime numbers are always greater than one so you choice of number there again will either print Is a Prime Number or Is Not a Prime Number.

Then  you have the for statement condition where the range starts from 2  and goes on to numbers greater than 2, **if statement** **(num % x) == 0** and the code returns "Is Not a Prime Number" on the compiler.

Finally, **else statement** which will return Is a Prime Number.

# POSITIVE AND NEGATIVE NUMBERS.

**Integers** are really sets of whole numbers consisting of positive numbers, negative numbers and zero.

**Positive numbers** are real numbers greater than zero and are found on the right side of the number line while **Negative numbers**
are real numbers less than zero and are found in the left side of the number line.

In the Third Python function, I implemented if...elif...else whereby you declare the function that enables the user to enter any number of choice.

Then you use **If statement**, number == 0 that makes the compiler to print out zero, Consequently the **elif statement** number < 0 will produce negative numbers, then again another *elif statement* that returns positive numbers this time around and eventually the "else statement" that prints out incorrect input, this is not a number.  
