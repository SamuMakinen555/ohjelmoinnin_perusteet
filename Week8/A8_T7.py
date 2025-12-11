from drawLib import drawCircle, drawSquare, drawHexagon, saveSvg, Drawing

def main() -> None:
    # Initialize the drawing object
    Dwg = Drawing()
    print("Program starting.")
    while True:
        showOptions()
        choice = askChoice()
        match choice:
            case 1:
                print('Insert square')
                # TODO: Prompt for square parameters and call drawSquare
                # Example: left = askValue1("Left edge position")
                left = askValue1("Left edge position")
                top = askValue1("Top edge position")
                sideLength = askValue1("Side length")
                color = askValue1("Fill color")
                strokeColor = askValue1("Stroke color")
                drawSquare(Dwg, left, top, sideLength, color, strokeColor)
            case 2:
                print('Insert circle')
                # TODO: Prompt for circle parameters and call drawCircle
                centerX = askValue1("Center X coord")
                centerY = askValue1("Center Y coord")
                radius = askValue1("Radius")
                color = askValue1("Fill color")
                stroke = askValue1("Stroke color")
                drawCircle(Dwg, centerX, centerY, radius, color, stroke)
            case 3:
                print("Insert hexagon details:")
                centerX = int(askValue1("Middle point X"))
                centerY = int(askValue1("Middle point Y"))
                apothem = int(askValue1("Apothem length"))
                color = askValue1("Insert fill")
                strokeColor = askValue1("Insert stroke")
                drawHexagon(Dwg, centerX, centerY, apothem, color, strokeColor)
            case 4:
                # TODO: Prompt for filename and confirm before saving
                file = askValue2("Insert filename")
                print(f"Saving file to \"{file}\"")
                confirmation = input("Proceed (y/n)?: ")
                if confirmation == "y":
                    saveSvg(Dwg, file)
                    print("Vector saved successfully!")

            case 0:
                print("Exiting program.\n")
                break
        print()
    print("Program ending.")

def showOptions() -> None:
    print("Options:")
    print("1 - Draw square")
    print("2 - Draw circle")
    print("3 - Draw hexagon")
    print("4 - Save svg")
    print("0 - Exit")

def askChoice() -> int:
    return int(input("Your choice: "))

def askValue1(PPrompt: str) -> str:
    return input(f"- {PPrompt}: ")

def askValue2(PPrompt: str) -> str:
    return input(f"{PPrompt}: ")

if __name__ == "__main__":
    main()