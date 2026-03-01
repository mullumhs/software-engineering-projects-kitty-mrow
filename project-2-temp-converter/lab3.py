"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 3
---------------------------------------------------------------------------------
- File Name: lab3.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Learn how to format numbers for display.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Ask the user for a decimal number and store it in a variable 'num1', converting to a float
num1 = float(input("please give a number\n"))
# Round the number to 2 decimal places using the round function 
print(round(num1, 2))
# Define a large integer 
largeNum = 34879672154
# Print the large integer with commas as thousands separators using f-strings 
print(f"{largeNum:,}")
# Define a small floating-point number 
smallNum = 0.000000000054212
# Print the number in scientific notation using f-strings 
print(f"{smallNum:.2e}")
# Define a small integer 
num2 = 1
# Print the number with leading zeros using f-strings 
print(f"{num2:05}")