def main():
    print("Program starting.")
    PName = askname()
    greetuser(PName)
    print("Program ending.")

def askname():
    name = input("Insert name: ")
    return name

def greetuser(PName):
    print(f"Hello {PName}!")
    return None

main()