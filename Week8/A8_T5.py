from loginLib import login, register, viewProfile, change_password

def main() -> None:
    print("Program starting.")
    mainMenu()
    print("Program ending.")

def showOptions() -> None:
    print("Options:")
    print("1 - Login")
    print("2 - Register")
    print("0 - Exit")

def showUserMenu() -> None:
    print("User menu:")
    print("1 - View profile")
    print("2 - Change password")
    print("0 - Logout")

def mainMenu() -> None:
    while True:
        showOptions()
        choice = askChoice()

        # TODO: Handle menu choices
        # - If login: ask for username and password, call login()
        # - If register: ask for username and password, call register()
        # - If exit: break the loop
        if choice == 0:
            print("Exiting program.\n")
            break

        elif choice == 1:
            username = input("Insert username: ")
            password = input("Insert password: ")
            if login(username, password) is True:
                print("Authentication successful!")
                print("")
                userMenu(username)
            elif login(username, password) is False:
                print("Authentication failed!")
                continue
        
        elif choice == 2:
            username = input("Insert username: ")
            password = input("Insert password: ")
            register(username, password)
            print("User registration completed!")
            print("")
            continue

        return None


def userMenu(PUsername: str) -> None:
    while True:
        showUserMenu()
        choice = askChoice()

        # TODO: Handle user menu choices
        # - View profile
        # - Change password
        # - Logout
        if choice == 0:
            print("Logging out...")
            break
        
        elif choice == 1:
            viewProfile(PUsername)
            print("")
            continue

        elif choice == 2:
            newpass = input("Insert new password: ")
            change_password(PUsername, newpass)
            print("Password changed!")
            print("")
            continue


def askChoice() -> int:
    return int(input("Your choice: "))

def askValue(PPrompt: str) -> str:
    return input(f"Insert {PPrompt}: ")

if __name__ == "__main__":
    main()
