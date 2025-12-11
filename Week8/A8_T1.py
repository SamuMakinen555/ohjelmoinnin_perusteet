from A8_T1_lib import activatePause

def askUser() -> str:
    return int(input("Your choice: "))

def showOptions() -> None:
    print("Options:")
    print("1 - Set pause duration")
    print("2 - Activate pause")
    print("0 - Exit")
    return None

def chooseActivity() :
    duration = 0
    while True:
        showOptions()
        choice = (askUser())
        match choice:
            case 1:
                duration = float(input("Insert pause duration (s): "))
            case 2:
                activatePause(duration)
                # print(f"Pausing for {duration} seconds.")
                # sleep(duration)
                # print("Unpaused.")
            case 0:
                print("Exiting program.\n")
                break

def main() -> None:
    print("Program starting.")
    chooseActivity()
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()