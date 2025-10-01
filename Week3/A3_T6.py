# Program starting.
# Welcome to the unit converter program!
# Follow the menu instructions below.
print("Program starting.")
print("Welcome to the unit converter program!")
print("Follow the menu instructions below.\n")

# Options:
# 1 - Length
# 2 - Weight
# 0 - Exit
# Your choice: 1
print("Options:")
print("1 - Length")
print("2 - Weight")
print("0 - Exit")
Pick = input("Your Choice: ")
print("")
# Length options:
# 1 - Meters to kilometers
# 2 - Kilometers to meters
# 0 - Exit
# Your choice: 1
# Insert meters: 1000
# 1000.0 m is 1.0 km
if Pick == "1":
    print("Length options:")
    print("1 - Meters to kilometers")
    print("2 - Kilometers to meters")
    print("0 - Exit")
    Pick2 = input("Your choice: ")
    if Pick2 == "1":
        Metr = float(input("Insert meters: "))
        Kilom = Metr / 1000
        print(f"{round(Metr,1)} m is {round(Kilom, 1)} km")
    elif Pick2 == "2":
        Kilom = float(input("Insert kilometers: "))
        Metr = Kilom * 1000
        print(f"{round(Kilom, 1)} km is {round(Metr, 1)} m")
    elif Pick2 == "0":
        print("Exiting...")
    else:
        print("Unknown option.")
elif Pick == "2":
    print("Weight options:")
    print("1 - Grams to pounds")
    print("2 - Pounds to grams")
    print("0 - Exit")
    Pick2 = input("Your choice: ")
    if Pick2 == "1":
        Gram1 = float(input("Insert grams: "))
        Pound1 = Gram1 / 453.6
        print(f"{round(Gram1, 1)} g is {round(Pound1, 1)} lb")
    elif Pick2 == "2":
        Pound2 = float(input("Insert pounds: "))
        Gram2 = Pound2 * 453.6
        print((f"{round(Pound2, 1)} lb is {round(Gram2, 1)} g"))
    elif Pick2 == "0":
        print("Exiting...")
    else:
        print("Unknown option.")
elif Pick == "0":
    print("Exiting...")
else:
     print("Unknown option.")
# Program ending.
print("\nProgram ending.")