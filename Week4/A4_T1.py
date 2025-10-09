# Program starting.

# Insert starting value: 11
# Insert stopping value: 13

# Starting for-loop:
# 11
# 12
# 13

# Program ending.
print("Program starting.\n")

Start = int(input("Insert starting value: "))
Stop = int(input("Insert stopping value: ")) + 1

print("\nStarting for-loop:")
for shoe in range(Start, Stop):
    print(shoe)
print("\nProgram ending.")