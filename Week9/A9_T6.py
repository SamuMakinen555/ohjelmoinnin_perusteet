########################################################
# Task A9_T6
# Developer Samu Mäkinen
# Date 09.12.2025
########################################################

def showOptions() -> None:
    # TODO: Print the menu options
    print("Options:")
    print("1 - Insert line")
    print("2 - Save lines")
    print("0 - Exit")
    return None

def askChoice() -> int:
    # TODO: Ask user for a menu choice and return it as an integer
    # Students should use try-except to handle invalid input
    while True:
        try:
            choice = int(input("Your choice: "))

            if choice in [0, 1, 2, 3]:
                return choice
            else:
                return -1

        except ValueError:
            return -1
          


def saveLines(PLines: list[str]) -> None:
    # TODO: Ask for filename and save lines to the file
    # Students should use try-except to handle file errors
    Filename = input("Insert filename: ")
    while True:
        try:
            with open(Filename, 'w', encoding="UTF-8") as file:
                file.writelines(PLines)
                break
        except:
            print("Invalid filename.")
    return None

def insertLine(PLines: list[str]) -> None:
    # TODO: Ask user to input a line and add it to PLines
    newLine = input("Insert text: ")
    PLines.append(newLine)
    return None

def onInterrupt(PLines: list[str]) -> None:
    # TODO: Handle KeyboardInterrupt when there are unsaved lines
    # Students should use try-except to handle input errors
    if len(PLines) == 0:
        print("Closing suddenly.")
    else:
        print("Keyboard interrupt and unsaved progress!")
        while True:
            try:
                choice = input("Save before quit (y/n)?: ")
                if choice in ["y", "n"]:
                    if choice == "n":
                        break
                    if choice == "y":
                        saveLines(PLines)
                        break
                else:
                    print("Unknown option!")
            except:
                print("Unknown option!")
            


    return None

def main() -> None:
    Lines: list[str] = []
    Choice = -1
    print("Program starting.")
    # Wrap the main loop in a try-except block to catch KeyboardInterrupt
    try:
        while Choice != 0:
            showOptions()
            Choice = askChoice()
            if Choice == 1:
                insertLine(Lines)
            elif Choice == 2:
                saveLines(Lines)
            elif Choice == 0:
                print("Exiting program.")
            else:
                print("Unknown option!")
            print("")
    except KeyboardInterrupt:
        onInterrupt(Lines)
    Lines.clear()
    print("Program ending.")

if __name__ == "__main__":
    main()

