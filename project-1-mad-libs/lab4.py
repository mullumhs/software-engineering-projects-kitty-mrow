"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 4
---------------------------------------------------------------------------------
- File Name: lab4.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Ask for full name and greet user by their first name only.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
fullName=input("what is youre full name?\n")
name=fullName.strip().title().split()
print("hello",name[0]+"!")