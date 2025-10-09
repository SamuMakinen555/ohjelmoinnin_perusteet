print("Program starting.\n")

Start = int(input("Insert starting value: "))
Stop = int(input("Insert stopping value: "))

print("\nStarting while-loop:")
i = Start
while i <= Stop - 1:
    print(i, end = " ")
    i += 1
print(i)

print("")
print("Program ending.")