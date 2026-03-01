"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 2
---------------------------------------------------------------------------------
- File Name: lab2.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Perform basic operations and calculations using numbers.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Ask the user for two numbers and store them in variables 'a' and 'b', converting to floats
a = float(input("please give a number\n"))
b = float(input("please give another number\n"))
# Add 'a' and 'b' and store the result in a variable 'add_result' 
add = a+b
# Subtract 'b' from 'a' and store the result in a variable 'sub_result' 
sub = a-b
# Multiply 'a' and 'b' and store the result in 'mul_result' 
mul = a*b
# Divide 'a' by 'b' and store the result in 'div_result' 
div = a/b
# Raise 'a' to the power of 'b' and store in 'exp_result' 
exp = a**b
# Calculate the modulus of 'a' and 'b' and store in 'mod_result' 
mod = a%b
# Print the results of each calculation, with a description of the operation, e.g. "5 plus 3 is 8" 
print(f"{a}+{b}={add}\n{a}-{b}={sub}\n{a}x{b}={mul}\n{a} over {b}={div}\n{a} to the power of {b}={exp}\nthe modulus of {a} and {b} = {mod}")