LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DELIMITER = ';'

# LOCATIONS = ["Home", "Galba's palace", "Otho's palace", "Vitellius' palace", "Vespasian's palace"]
PROGRESS_FILE = "player_progress.txt"

def readFile() -> str:
    with open(PROGRESS_FILE, 'r', encoding="UTF-8") as file:
        content = file.readlines()
    # Content = ''
    # FileHandle = open(Pfilename, 'r')
    # Row = FileHandle.readline()
    # while Row != '':
    #     Content += Row
    #     Row = FileHandle.readline()
    # FileHandle.close()
    return content

def writeFile(next_location_id: int, passphrase_encrypted: str, passphrase: str) -> str:
    encrypted_filename = (f"{next_location_id}_{passphrase_encrypted}.gkg")

    with open(encrypted_filename, 'r', encoding="UTF-8") as file:
        first_line_encrypted = file.readline() 
        encrypted_content = file.read()
        content = rot13(encrypted_content)

    plain_filename = (f"{next_location_id}-{passphrase}.txt")
    with open(plain_filename, 'w', encoding="UTF-8") as file:
        file.write(content)
    
    return first_line_encrypted

def appendToFile(current_id: int, next_id: int, passphrase: str) -> None:
    new_line = (f"{current_id}{DELIMITER}{next_id}{DELIMITER}{passphrase}")

    with open(PROGRESS_FILE, 'a', encoding="UTF-8") as file:
        file.write(f"{new_line}\n")
    print("[Game] Progress autosaved!")
    return None

def shiftCharacter(Character: str, Alphabet: str) -> str:
    for i in range(len(Alphabet)):
        if Character == Alphabet[i]:
            Shift = i + 13
            if Shift >= len(Alphabet):
                Shift -= len(Alphabet)
    NewCharacter = Alphabet[Shift]            

    return NewCharacter

def rot13(cipheredmessage) -> str:
    Message = ""
    for Character in cipheredmessage:
        if Character in LOWER_ALPHABETS:
            Message += shiftCharacter(Character, LOWER_ALPHABETS)
        elif Character in UPPER_ALPHABETS:
            Message += shiftCharacter(Character, UPPER_ALPHABETS)
        else:
            Message += Character
    return Message


def getLocation(locationId):
    Location = "unknown"
    if locationId == 1:
        Location = "Galba's palace"
    elif locationId == 2:
        Location = "Otho's palace"
    elif locationId == 3:
        Location = "Vitellius' palace"
    elif locationId == 4:
        Location = "Vespasian's palace"
    elif locationId == 0:
        Location = "Home"
    return Location 

def main() -> None:
    print("Travel starting.")
    
    Progress = readFile()
    Progress = [line for line in Progress if line.strip()]
    LastProgress = Progress[-1].strip().split(DELIMITER)   #.strip().split('\n')[-1].split(DELIMITER)
    print(LastProgress)
    CurrentLocationId = int(LastProgress[0])
    CurrentLocation = getLocation(CurrentLocationId)
    NextLocationId = int(LastProgress[1])
    NextLocation = getLocation(NextLocationId)
    PassPhrase_encrypted = LastProgress[2]
    PassPhrase = rot13(PassPhrase_encrypted)

    print(f"Currently at {CurrentLocation}.")
    print(f"Travelling to {NextLocation}...")
    print(f"...Arriving to the {NextLocation}")
    print(f"Passing the guard at the entrance.")
    print(f'"{PassPhrase.capitalize()}"!')
    print("Looking for the message in the palace...")
    print("Ah, there it is! Seems cryptic.")

    if CurrentLocationId == NextLocationId:
        print(f"Already at final location: {CurrentLocation}. No more travel.")
        print("Travel ending.")
        return None
    print("Deciphering Emperor's message...")

    next_progress = writeFile(NextLocationId, PassPhrase_encrypted, PassPhrase)
    
    new_currentid, new_nextid, new_passphrase = next_progress.split(DELIMITER)
    appendToFile(int(new_currentid), int(new_nextid), new_passphrase)

    print("Looks like I've got now the plain version copy of the Emperor's message.")
    print("Time to leave...")
    print("Travel ending.")

    return None

if __name__ == "__main__":
    main()
