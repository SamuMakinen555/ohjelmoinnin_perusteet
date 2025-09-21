#Make a Python program, which prompts the user name and two floating numbers. Multiply the inserted numbers to get product. Round the product in two decimal precision. Complete the program output as shown below.

#Example program run:

#Program starting.
print("Program starting.")
#What is your name: John
Name = input("What is your name: ")
#Enter a floating point number: 3.1
#Enter second floating point number: 5.3
Floatnumber1 = float(input("Enter a floating point number: "))
Floatnumber2 = float(input("Enter a second floating point number: "))
#Voisi olla myös:
#Floatnumber1 = input("Enter...")
#Floatnumber1 = float(Floatnumber1)
#jne.
#John you gave numbers 3.1 and 5.3
print(f"{Name} you gave numbers {Floatnumber1} and {Floatnumber2}")
#Multiplying first and second number will result in product 16.43
Product = Floatnumber1 * Floatnumber2
print(f"Multiplying first and second number will result in product {round(Product, 2)}")
#Program ending.
print("Program ending.")






