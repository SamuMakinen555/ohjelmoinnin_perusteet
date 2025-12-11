########################################################
# Task A9_T3
# Developer Samu Mäkinen
# Date 09.12.2025
########################################################

import sys

def main() -> None:
    print("Program starting.")
    file = input("Insert filename: ")

    try:
        with open(file, 'r', encoding="UTF-8") as f:
            print(f"## {file} ##")
            print(f.read())
            print(f"## {file} ##")
    except FileNotFoundError:
        print(f"Couldn't read file \"{file}\".")
        sys.exit(1)
    
    print("Program ending.")

if __name__ == "__main__":
    main()