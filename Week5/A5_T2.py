def main():
    print("Program starting.")
    Word = input("Insert word: ")
    print("")
    frameWord(Word)
    print("\n")
    print("Program ending.")
    return None

def frameWord(PWord):
    end = len(PWord)
    for i in range(0, end+4):
        print("*", end="")
    print(f"\n* {PWord} *")
    for i in range (0, end+4):
        print("*", end="")
    return None

main()
# helpommin print("*" * (len(Pword)+4))