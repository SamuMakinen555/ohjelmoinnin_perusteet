########################################################
# Task A10_T6
# Developer Samu Mäkinen
# Date 11.12.2025
########################################################

import sys
from A10_TLib import readValues, displayValues, bubbleSort, quickSort
import copy
import time
from typing import Callable

def measureSortingTime(PSortingAlgorithm: Callable, PArr: list[int]) -> int:
    StartTime = time.perf_counter_ns()
    PSortingAlgorithm(PArr)
    EndTime = time.perf_counter_ns()
    ElapsedTime = EndTime - StartTime
    return ElapsedTime

def showOptions():
    print("Options:")
    print("1 - Read dataset values")
    print("2 - Measure speeds")
    print("3 - Save results")
    print("0 - Exit")
    return None

def handleChoice(Values):
    
    while True:
        showOptions()
        choice = input("Your choice: ")

        if choice == "0":
            print("Exiting program.\n")
            break
        elif choice == "1":
           Filename = input("Insert dataset filename: ")
           Values = readValues(Filename, Values)
        elif choice == "2":
            BuiltinSortedTimeNs = measureSortingTime(sorted, copy.deepcopy(Values))
            BubbleSortTimeNs = measureSortingTime(bubbleSort, copy.deepcopy(Values))
            QuickSortTimeNs = measureSortingTime(quickSort, copy.deepcopy(Values))
            print(f"Measured speeds for dataset '{Filename}':")
            print(f" - Built-in sorted {BuiltinSortedTimeNs} ns")
            print(f" - Bubble sort {BubbleSortTimeNs} ns")
            print(f" - Quick sort {QuickSortTimeNs} ns")

           
        elif choice == "3":
            continue
            
    return None

def main() -> None:
   
    Values: list[int] = []
        
    print("Program starting.")
    handleChoice(Values)
    Values.clear()
    print("Program ending.")
 

if __name__ == "__main__":
    main()