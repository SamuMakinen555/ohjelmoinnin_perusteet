#Make a Python program, which prompts user for a car brand and model. After user inputs, do print the car brand and model sentence with two print commands using “sep” and “end” parameters.

#Example program run:

#Program starting.
print("Program starting.")
#Insert car brand: Toyota
#Insert car model: Corolla
Brand = input("Insert car brand: ")
Model = input("Insert car model: ")
#Car brand is "Toyota" and the model is 'Corolla'.
print("Car brand is ", Brand, " ", sep='"', end="")
#yllä kikkailua, että tulee käytetyksi sep-parametriä. Voisi olla:
#print(f"Car brand is \"{Brand}\" ", end="")
print(f"and the model is '{Model}'.")
#Program ending.
print("Program ending.")
