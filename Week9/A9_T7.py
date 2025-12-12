########################################################
# Task A10_T5
# Developer Samu Mäkinen
# Date 08.12.2025
########################################################

import sys
import os

def showHelp() -> None:
    #What?
    return

def copyFile(PSrcFile: str, PDstFile: str) -> None:
    try:
        if not os.path.exists(PSrcFile):
            print(f'Source file "{PSrcFile}" does not exist.')
            print("Exiting program.")
            sys.exit(1)

        if os.path.exists(PDstFile):
            print(f'Destination file "{PDstFile}" already exists.')
            overwrite = input("Do you want to overwrite it? (y/n): ")
            if overwrite != "y":
                return
            
        with open(PSrcFile, 'r', encoding="UTF-8") as sourcef:
            content = sourcef.read()

        with open(PDstFile, 'w', encoding="UTF-8") as destf:
            destf.write(content)

        print(f'Copying file "{PSrcFile}" to "{PDstFile}.')

    except Exception as err:
        print(f'Could not copy "{PSrcFile}" to "{PDstFile}". Error: {err}')
        sys.exit(1)

def main() -> None:
    print("Program starting.")
    if len(sys.argv) != 3:
        print("Invalid amount of arguments.")
        sys.exit(0)

    SrcFile = sys.argv[1]
    DstFile = sys.argv[2]

    copyFile(SrcFile, DstFile)

    print("Program ending.")

if __name__ == "__main__":
    main()