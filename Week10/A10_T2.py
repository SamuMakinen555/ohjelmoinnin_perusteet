########################################################
# Task A10_T2
# Developer Samu Mäkinen
# Date 12.12.2025
########################################################

import sys

def readValues(Pfilename: str, Pvalues: list[int]) -> None:
    try:
        with open(Pfilename, 'r', encoding="UTF-8") as file:
            for line in file:
                if line.strip():
                    try:
                        Pvalues.append(int(line.strip()))
                    except ValueError:
                        print(f"Skipping a line that is not an integer.")
                        continue
                        
                        
    except FileNotFoundError:
        print(f"File '{Pfilename}' was not found.")
        sys.exit(1)

def sumValues(Pvalues: list[int]) -> int:
    total = sum(Pvalues)
    return total

def productValues(Pvalues: list[list]) -> int:
    product = 1
    for number in Pvalues:
        product *= number
    return product

def displayResults(sum: int, product: int) -> None:
    print("# --- Sum of numbers --- #")
    print(sum)
    print("# --- Sum of numbers --- #")
    print("# --- Product of numbers --- #")
    print(product)
    print("# --- Product of numbers --- #")

def main() -> None:
    values: list[int] = []
    print("Program starting.")
    filename = input("Insert filename: ")
    readValues(filename, values)
    sum = sumValues(values)
    product = productValues(values)
    displayResults(sum, product)
    print("Program ending.")

if __name__ == "__main__":
    main()
