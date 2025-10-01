print("Program starting.")
print("Testing decision structures.")
Value = int(input("Insert an integer: "))

print("Options:")
print("1 - In one multi-branched decision")
print("2 - In multiple independent if-statements")
print("0 - Exit")
Valinta = input("Your choice: ")

if Valinta == "1":
    print("Using one multi-branced decision structure.")
    if Value >= 400:
        Value = Value + 44
    elif Value >= 200:
        Value = Value + 22
    elif Value >= 100:
        Value = Value + 11
    print(f"Result is {Value}")
elif Valinta == "2":
    print("Using multiple independent if-statements structure.")
    if Value >= 400:
        Value = Value + 44
    if Value >= 200:
        Value = Value + 22
    if Value >= 100:
        Value = Value + 11
    print(f"Result is {Value}")
elif Valinta == "0":
    print("Exiting...")
else:
    print("Unknown option.")
print("\nProgram ending.")
        
