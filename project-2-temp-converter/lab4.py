"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 4
---------------------------------------------------------------------------------
- File Name: lab4.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Use conditional statements to control the flow of execution.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Ask the user for an integer and store it in a variable 'num'
num = int(input("please give me a whole number\n"))
# Use an if statement to check if the number is positive, negative or zero 
if num == 0:
    print("wow really 0?")
elif num > 0:
    print("a postive number? how basic")
else:
    print("are you like the number? negative?")
# Ask the user for their age and store it in a variable 'age' 
age = int(input("\nwhat is your age?\n"))
# Use an if statement to check if the user is an adult (18+) or a minor 
if age >= 18:
    print("unc")
else:
    print("youre too young get out of here!")
# Ask the user for two integers, 'a' and 'b' 
a = int(input("\ngive me a whole number\n"))
b = int(input("\ngive me another whole number\n"))
# Use an if statement to check if both numbers are positive or both are negative 
if a & b < 0:
    print("you really are so negative")
elif a & b > 0:
    print("youre so postive it makes me sick")
# Otherwise print "One number is positive and the other is negative." 
else:
    print("a perfect balance, as all things should be") 