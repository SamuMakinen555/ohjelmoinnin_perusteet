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
        print(f"Result is {Value + 44}")
    elif Value >= 200:
        print(f"Result is {Value + 22}")
    elif Value >= 100:
        print(f"Result is {Value + 11}")
    else:
        print(f"Result is {Value}")
elif Valinta == "2":
    print("Using multiple independent if-statements structure.")
    if Value >= 400:
        Value2 = Value + 44
    else: 
        Value2 = Value
    if Value2 >= 200:
        Value3 = Value2 + 22
    else:
        Value3 = Value2
    if Value3 >= 100:
        Value4 = Value3 + 11
    else:
        Value4 = Value3
    print(f"Result is {Value4}")
elif Valinta == "0":
    print("Exiting...")
else:
    print("Unknown option.")
print("\nProgram ending.")
        
