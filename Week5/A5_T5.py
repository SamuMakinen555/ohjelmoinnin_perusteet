def menu():
    print("Options:")
    print("1 - Insert word")
    print("2 - Show current word")
    print("3 - Show current word in reverse")
    print("0 - Exit")
    return input("Your choice: ")

def main():
    print("Program starting.")
    Word = ""
    while True:
        choice = menu()
        if choice == "1":
            Word = input("Insert word: ")
            print("")
        elif choice == "2":
            print(f"Current word - \"{Word}\"\n")
        elif choice == "3":
            print(f"Word reversed - \"{Word[::-1]}\"\n")
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Unknown option! try again.\n")

    print("\nProgram ending.")

main()


    