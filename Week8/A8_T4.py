import A8_T4_lib as ts

def showOptions():
    print("Options:")
    print("1 - Calculate amount of timestamps during year")
    print("2 - Calculate amount of timestamps during month")
    print("3 - Calculate amount of timestamps during weekday")
    print("0 - Exit")
    return None

def handleChoice(timestamps):
    while True:
        showOptions()
        choice = input("Your choice: ")

        if choice == "0":
            print("Exiting program.")
            break
        elif choice == "1":
            year = int(input("Insert year: "))
            count = ts.calculateYears(timestamps, year)
            print(f"Amount of timestamps during year '{year}' is {count}\n")
        elif choice == "2":
            month = input("Insert month: ")
            count = ts.calculateMonths(timestamps, month)
            print(f"Amount of timestamps during month '{month}' is {count}\n")
        elif choice == "3":
            weekday = input("Insert weekday: ")
            count = ts.calculateWeekdays(timestamps, weekday)
            print(f"Amount of timestamps during weekday '{weekday}' is {count}\n")
    return None
    
def main():
    print("Program starting.")
    filename = input("Insert filename: ")
    timestamps = ts.readTimestamps(filename)
    handleChoice(timestamps)
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()