########################################################
# Task A10_T4
# Developer Samu Mäkinen
# Date 11.12.2025
########################################################

import sys
from A10_TLib import readValues, displayValues, merge, mergeSort

def main() -> None:
    # Initialize
    Values: list[int] = []
    Filename = ""

    
    print("Program starting.")

    # TODO: Handle CLI argument or prompt for filename
    # If len(sys.argv) == 2, use sys.argv[1]
    # Otherwise, ask the user to input the filename
    
    if len(sys.argv) == 2:
        Filename = sys.argv[1]
    else:
        Filename = input("Insert filename: ")

    # TODO: Read values from file into Values list using readValues()
    Values = readValues(Filename, Values)
    # TODO: Print raw values using displayValues()
    print(f"Raw '{Filename}' -> {displayValues(Values)}")
    # TODO: Sort values in ascending order using bubbleSort()
    # TODO: Print sorted ascending values
    mergeSort(Values)
    print(f"Ascending '{Filename}' -> {displayValues(Values)}")
    # TODO: Sort values in descending order using bubbleSort(PAsc=False)
    # TODO: Print sorted descending values
    mergeSort(Values, PAsc=False)
    print(f"Descending '{Filename}' -> {displayValues(Values)}")

    # Clear list
    Values.clear()

if __name__ == "__main__":
    main()
