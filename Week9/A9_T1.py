########################################################
# Task A9_T1
# Developer Samu Mäkinen
# Date 09.12.2025
########################################################


def main() -> None:
    Sum = 0
    Value = -1
    print("Program starting.")
    while Value != 0:
        Feed = input("Insert a floating-point value (0 to stop): ")
        try: 
            Value = float(Feed)
            Sum += Value 
        except ValueError:
            print(f"Error! '{Feed}' couldn't be converted to float.")
        # finally:
        #     print(f"Final sum is ")

    print(f"\nFinal sum is: {Sum :.2f}")
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()