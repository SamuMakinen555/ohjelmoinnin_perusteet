def askIntByte(PPrompt: str) -> int:
########################################################
# Task A9_T5
# Developer Samu Mäkinen
# Date 08.12.2025
########################################################

    # Ask for input
    Feed = input(PPrompt)

    # TODO: Use try-except to:
    #   - Convert input to float and int
    #   - Raise an exception if input is not numeric
    #   - Raise an exception if input is not an integer
    #   - Raise an exception if input is not in the range 0–255

    # If all checks pass, return the integer value

    try:
        Feed_float = float(Feed)
    except ValueError:
        raise Exception(f'"{Feed}" is non-numeric value.')
    
    if not Feed_float.is_integer():
        raise Exception(f'"{Feed}" is non-numeric value.')

    Feed_int = int(Feed)
    if (Feed_int < 0) or (Feed_int > 255):
        raise Exception(f'Value "{Feed}" is out of the range 0-255.')

    return Feed_int

def createHex(PRed: int, PGreen: int, PBlue: int) -> str:
    # TODO: Return a hex string in the format "#rrggbb"
    # Use string formatting: "{:02x}"
    Hex = "#{:02x}{:02x}{:02x}".format(PRed, PGreen, PBlue)
    return Hex
    

def main():
    print("Program starting.")

    # TODO: Use try-except here to:
    #   - Call askIntByte for red, green, and blue
    #   - Call createHex to get the hex color
    #   - Print RGB values, hex value, and binary (8-bit) values
    #   - If any exception occurs, print the error and a message like:
    #     "Couldn't perform the designed task due to the invalid input values."
    try:
        Red = askIntByte("Insert red: ")
        Green = askIntByte("Insert green: ")
        Blue = askIntByte("Insert blue: ")
        Hex = createHex(Red, Green, Blue)
        print(f"- Red {Red}") 
        print(f"- Green {Green}")
        print(f"- Blue {Blue}")
        print(f"- Hex {Hex}")
        rbyte = format(Red, '08b')
        gbyte = format(Green, '08b')
        bbyte = format(Blue, '08b')
        print(f"- R-byte(base-2): {rbyte}")
        print(f"- G-byte(base-2): {gbyte}")
        print(f"- B-byte(base-2): {bbyte}")
        
    except Exception as err:
        print(err)
        print("Couldn't perform the designed task due to the invalid input values.")

    print("Program ending.")

if __name__ == "__main__":
    main()
