from A8_T3_lib import readValues, calculateSum, calculateAverage, showOptions

def handleChoice():
    while True:
        showOptions()
        choice = input("Your choice: ")

        if choice == "0":
            print("Exiting program.")
            break
        elif choice == "1":
            filename = input("Insert filename: ")
            values = readValues(filename)
        elif choice ==  "2":
            print(f"Amount of values {len(values)}")
        elif choice == "3":
            print(f"Sum of values {calculateSum(values)}")
        elif choice == "4":
            print(f"Average of values {calculateAverage(values)}")


def main():
    print("Program starting.")
    handleChoice()
    print("\nProgram ending.")
    return None

if __name__ == "__main__":
    main()