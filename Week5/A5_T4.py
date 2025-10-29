def askDimension(PPrompt: str) -> float:
   Feed = input(f"Insert {PPrompt}: ")
   return float(Feed)

def calcRectangleArea(PWidth: float, PHeight: float) -> float:
   RecArea = PWidth * PHeight
   return RecArea

def main():
    print("Program starting.")
    Width = askDimension("width")
    Height = askDimension("height")
    Area = calcRectangleArea(Width, Height)
    print("")
    print(f"Area is {Area}²")
    print("Program ending.")

main()