########################################################
# Task A9_T4
# Developer Samu Mäkinen
# Date 09.12.2025
########################################################

TEMP_MIN = -273.15
TEMP_MAX = 10000

def collectCelsius() -> float:
    Feed = input("Insert celsius: ")
    
    try:            
        Celsius = float(Feed)
        if (Celsius < TEMP_MIN) or (Celsius > TEMP_MAX):
            raise Exception(f"{Celsius} temperature out of range.")
    except ValueError:
        raise Exception(f"Could not convert string to float: '{Feed}'")

    return Celsius

def main() -> None:
    print("Program starting.")
    try:
        Celsius = collectCelsius()
        print(f"You inserted {Celsius} °C")
    except Exception as err:
        print(err)
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()