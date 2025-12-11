########################################################
# Task A9_T2
# Developer Samu Mäkinen
# Date 09.12.2025
########################################################

import sys

def main() -> None:

    print("Program starting.")
    while True:
        try:
            Feed = input("Insert exit code (0-255): ")
            ExitCode = int(Feed)
            if (ExitCode < 0) or (ExitCode > 255):
                raise Exception
         
        except:
            print("Error! The number must be between 0-255.")
            continue
        
        if ExitCode == 0:
            print("Clean exit.")
        else:
            print("Error code")
        sys.exit(ExitCode)
    

    print("Program ending.")
    return None

if __name__ == "__main__":
    main()