LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def shiftCharacter(Character: str, Alphabet: str):
    for i in range(len(Alphabet)):
        if Character == Alphabet[i]:
            Shift = i + 13
            if Shift >= len(Alphabet):
                Shift -= len(Alphabet)
    NewCharacter = Alphabet[Shift]            

    return NewCharacter

def collectRows():
    collectedRows = ""
    while True:    
        Row = input(f"Insert row(empty stops): ")
        if Row != "":
            collectedRows += Row + "\n"
        else:
            return collectedRows

def rot13(message):
    cipheredMessage = ""
    for Character in message:
        if Character in LOWER_ALPHABETS:
            cipheredMessage += shiftCharacter(Character, LOWER_ALPHABETS)
        elif Character in UPPER_ALPHABETS:
            cipheredMessage += shiftCharacter(Character, UPPER_ALPHABETS)
        else:
            cipheredMessage += Character
    return cipheredMessage

def writeFile(filename, content):
    with open(filename, 'w', encoding="UTF-8") as file:
        file.write(content)
    return None

def main():
    print(f"Program starting.\n")
    print(f"Collecting plain text rows for ciphering.")
    collectedRows = collectRows()
    print("")
    
    print(f"#### Ciphered text ####")
    cipheredMessage = rot13(collectedRows)
    print(cipheredMessage)
    print(f"#### Ciphered text ####")
    
    filename = input(f"Insert filename to save: ")
    if filename == "":
        print(f"File name not defined.")
        print(f"Aborting save operation.")
    else:
        writeFile(filename, cipheredMessage)
        print(f"Ciphered text saved!")
    print(f"Program ending.")


if __name__ == "__main__":
    main()