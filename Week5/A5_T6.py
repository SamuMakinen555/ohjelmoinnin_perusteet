def showOptions() -> None:
    print("Options:")
    print("1 - Show count")
    print("2 - Increase count")
    print("3 - Reset count")
    print("0 - Exit")
    return None

def askChoice() -> int:
    while True:
        userinput = input("Your choice: ")
        testnumeric = userinput.isnumeric()
        if testnumeric == False:
            print("Unknown option!\n")
            showOptions()
        else:
            return int(userinput)
            
def main():
    print("Program starting.")
    count = 0
    while True:
        showOptions()
        choice = askChoice()
        if choice == 1:
            print(f"Current count - {count}\n")
        elif choice == 2:
            count += 1
            print("Count increased!\n")
        elif choice == 3:
            count = 0
            print("Cleared count!\n")
        elif choice == 0:
            print("Exiting program.\n")
            break
        else:
            print ("Unknown option!\n")
    print("Program ending.")

    

if __name__ == "__main__" or "unittest" in __import__("sys").modules:
    main()