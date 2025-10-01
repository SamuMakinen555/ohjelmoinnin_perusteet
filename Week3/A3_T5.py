# Program starting.
print("Program starting.\n")

# Options:
# 1 - Celsius to Fahrenheit
# 2 - Fahrenheit to Celsius
# 0 - Exit
print("Options:")
print("1 - Celsius to Fahrenheit")
print("2 - Fahrenheit to Celsius")
print("0 - Exit")
# Your choice: 1
Valinta = input("Your choice: ")
# Insert the amount of Celsius: 23
# 23.0 °C equals to 73.4 °F
# # Program ending.
if Valinta == "1":
    Cel1 = float(input("Insert the amount of Celsius: "))
    Fah1 = Cel1 * 1.8 + 32
    print(f"{round(Cel1, 1)} °C equals to {round(Fah1, 1)} °F")
elif Valinta == "2":
    Fah2 = float(input("Insert the amount of Fahrenheit: "))
    Cel2 = (Fah2 - 32) / 1.8
    print(F"{round(Fah2, 1)} °F equals to {round(Cel2, 1)} °C")
elif Valinta == "0":
    print("Exiting...")
else:
    print("Unknown option.")
print("\nProgram ending.")