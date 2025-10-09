print("Program starting.\n")

Start = int(input("Insert starting value: "))
Stop = int(input("Insert stopping value: "))

print("\nStarting for-loop:")
for shoe in range(Start, Stop):
    print(shoe, end=" ")
print(Stop)
print("\nProgram ending.")