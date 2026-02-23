"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    MAD LIBS
---------------------------------------------------------------------------------
- File Name: mad-libs.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Complete a functional Mad Libs game in Python.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
userName = input("what is youre full name?")
userNameStrip = userName.strip().title().split()

print(f"\nHello {userNameStrip[0]}! we will make alittle story :>")
name1 = input("\nour character needs a name, what should it be?\n")
name1Fix = name1.strip().title()
if name1Fix == "Chara":
    print("\nthe true name :]")
name2 = input("now we need a 2nd for their friend\n")
name2Fix = name2.strip().title()
if name2Fix == "Frisk":
    print("\nthe vessel\n")
verb2 =  input("what are they doing?\n")
verb2fix = verb2.strip()
loction = input("where is our hero and their friend live?\n")
loctionFix = loction.strip().title()
if loctionFix == "Underground":
    print("\nyou do realise we are trying to make heros right?\n")
villian = input("what is the villians name?\n")
villianFix = villian.strip().title()
if villianFix == "Asgore":
    print("\nyou are the villian not him >:[\n")
villianLocation = input("and where do our heros find the villian?\n")
villianLocationFix = villianLocation.strip().title()
verb1 = input("what is the villian doing when they find him?\n")
verb1Fix = verb1.strip()
react = input("how will " + name1Fix + " and " + name2Fix + " reacted to this?\n")
reactFix = react.strip()
stop = input("quick how will they stop the villian!\n")
stopFix = stop.strip().upper()


question = input("should we have a talking animal? y/n\n")
questionFix = question.strip().title()
if questionFix == "Y" and villianFix == "Asgore" or questionFix == "Yes" and villianFix == "Asgore":
    print("\ni know you are just making undertale, no need for me to write anything")

elif questionFix == "Y" or questionFix == "Yes":
    animal = input("oooooooh, what type of animal!\n")
    animalFix = animal.strip().title()
    print(f"\n{name1Fix} was {verb2fix} with their best friend {name2Fix} and their pet talking {animalFix} at {loctionFix}. \nthey deside to go check out {villianLocationFix} and find the evil {villianFix}! and he was {verb1Fix}! {name1Fix}, {name2Fix} and {animalFix} are all {reactFix} at this. they choose to stop the villain by {stopFix}! \
            by {userNameStrip[1]}")

else:
    print(f"\n{name1Fix} was {verb2fix} with their best friend {name2Fix} at {loctionFix}. they deside to go check out {villianLocationFix} and find the evil {villianFix}!\n and he was {verb1Fix}! {name1Fix}, and {name2Fix} are {reactFix} at this. they choose to stop the villain by {stopFix}! \
            by {userNameStrip[0]} {userNameStrip[1]}")
    