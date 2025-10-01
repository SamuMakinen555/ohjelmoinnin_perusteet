#Program starting.
print("Program starting.")
#Insert two integers.
#Insert first integer: 5
#Insert second integer: 5
print("Insert two integers.")
Int1 = int(input("Insert first integer: "))
Int2 = int(input("Insert second integer: "))
#Comparing inserted integers.
print("Comparing inserted integers.")
#Integers are the same
if Int1 == Int2:
    print("Integers are the same")
if Int1 > Int2:
    print("First integer is greater")
if Int1 < Int2:
    print("Second integer is greater")
#
#Adding integers together
#5 + 5 = 10
Sum1 = Int1 + Int2
print("\nAdding integers together")
print(f"{Int1} + {Int2} = {Sum1}")
#
#Checking the parity of the sum...
#Sum is even.
print("\nChecking the parity of the sum...")
Par1 = Sum1 % 2
if Par1 == 0:
    print("Sum is even.")
else:
    print("Sum is odd.")
#Program ending.
print("Program ending.")