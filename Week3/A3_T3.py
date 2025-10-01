#A3_T3 Menu program
#
print("Program starting.\n" \
"This is a program with simple menu, " \
"where you can choose which operation the program performs.")
#Create a program with a plain menu.
#
#    Prompt username first
Name = input("Before the menu, please insert your name: ")
#    Make program menu with following options:
#        Print welcome message
#            Welcome {Name}!
#        Exit
#            Exiting...
#    Prompt user to choose option “Your choice:”
#    Perform actions based on the user input
print("")
print("Options:")
print("1 - Print welcome message")
print("0 - Exit")
Choice = input("Your choice: ")
if Choice == "1":
    print(f"Welcome {Name}!")
elif Choice == "0":
    print("Exiting...")
else:
    print("Unknown option.")

print("\nProgram ending.")
#
#Creating menus like this is a really handy way to make tiny text-based programs and there will be more exercises like this in the future.
#
#The expectation at this point is that the user is able to choose option by inserting corresponding number. No error handling is required, it will be introduced later.
#
#Other possible output variats:
#
#    Unknown option.

