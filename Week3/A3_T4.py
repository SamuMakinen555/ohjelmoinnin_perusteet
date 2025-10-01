#A3_T4 More menu options
#
#Extend the previous menu program by adding three more options to the menu.
#
print("Program starting.\n" \
"This is a program with simple menu, " \
"where you can choose which operation the program performs.")
Name = input("Before the menu, please insert your name: ")
print("")
print("Options:")
print("1 - Print welcome message")
print("2 - Print the name backwards")
print("3 - Print the first character")
print("4 - Show the amount of characters in the name")
print("0 - Exit")
Choice = input("Your choice: ")
if Choice == "1":
    print(f"Welcome {Name}!")
elif Choice == "2":
    print(f"{Name[::-1]}")
elif Choice == "3":
    print(f"The first character in name \"{Name}\" is \"{Name[0:1]}\"")
elif Choice == "4":
    print(f"There are {len(Name)} characters in the name \"{Name}\"")
elif Choice == "0":
    print("Exiting...")
else:
    print("Unknown option.")
print("\nProgram ending.")
#Options:
#
#    Print the name backwards
#        Your name backwards is "{NameBackwards}"
#    Print the first character
#        The first character in name "{Name}" is "{FirstChar}"
#    Show the amount of characters in the name
#        There are {NameLength} characters in the name "{Name}"
