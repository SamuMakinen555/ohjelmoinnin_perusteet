import hashlib

# Constants
CREDENTIALS_FILE = "credentials.txt"
DELIMITER = ";"


def hash_password(password: str) -> str:
    """
    Hash the password using MD5 and return the hex digest.
    """
    # TODO: Implement password hashing
    s = password
    res = hashlib.md5(s.encode())
    md5hash = res.hexdigest()
    return md5hash
    


def register(PUsername: str, PPassword: str) -> None:
    """
    Register a new user by appending their credentials to the file.
    """
    # TODO: Count existing users to assign a new ID
    # TODO: Hash the password
    # TODO: Write the new user to the file
    with open(CREDENTIALS_FILE, 'r', encoding="UTF-8") as file:
        lines = [line.strip() for line in file if line.strip()]
        idnumber = len(lines)
       
        # counter = 0
        # for line in file:
        #     if line.strip():
        #         counter += 1
    
    hashedpass = hash_password(PPassword)

    with open(CREDENTIALS_FILE, 'a', encoding="UTF-8") as file:
        file.write(f'{idnumber}{DELIMITER}{PUsername}{DELIMITER}{hashedpass}')

    return None



def login(PUsername: str, PPassword: str) -> bool:
    """
    Check if the username and password match an entry in the credentials file.
    """
    # TODO: Hash the input password
    # TODO: Read the file and compare credentials
    hashedpass = hash_password(PPassword)

    with open(CREDENTIALS_FILE, 'r', encoding="UTF-8") as file:
        lines = [line.strip() for line in file if line.strip()]
        for i in lines:
            if PUsername in i and hashedpass in i:
                return True
            else:
                return False
    


def viewProfile(PUsername: str) -> list[str]:
    """
    Return the user ID and username for the given username.
    """
    # TODO: Read the file and return the matching profile
    with open(CREDENTIALS_FILE, 'r', encoding="UTF-8") as file:
       lines = [line.strip() for line in file if line.strip()]
       idcounter = -1
       for i in lines:
           idcounter += 1
           if PUsername in i:
               print(f'Profile ID {idcounter} - {PUsername}')
               profile = [str(idcounter), PUsername]
               
    return profile


def change_password(PUsername: str, PNewPassword: str) -> None:
    """
    Change the password for the given username.
    """
    # TODO: Read all lines, update the password for the matching user
    # TODO: Write the updated lines back to the file
    
    with open(CREDENTIALS_FILE, 'r', encoding="UTF-8") as file:
       lines = [line.strip() for line in file if line.strip()]
       idcounter = -1
       for i in lines:
           idcounter +=1
           if PUsername in i:
               idnumber = idcounter
       
       newhashedpass = hash_password(PNewPassword)
       lines[idnumber] = (f'{idnumber}{DELIMITER}{PUsername}{DELIMITER}{newhashedpass}')

    with open(CREDENTIALS_FILE, 'w', encoding="UTF-8") as file:
       for i in lines:
           file.write(i)

    return None

