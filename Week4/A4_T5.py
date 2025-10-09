print("Program starting.\n")

Alku = int(input("Insert starting point: "))
Loppu = int(input("Insert stopping point: "))
Tark = int(input("Insert inspection point: "))
print("")
if Alku >= Loppu:
    print("Starting point value must be less than the stopping point value.")
if Tark < Alku or Tark > Loppu:
    print("Inspection value must be within the range of start and stop.")
else:
    print("First loop - inspection with break:")
    for i in range(Alku, Loppu):
        if Tark == Alku:
            print("")
        if i == Tark:
            break
        elif i == Tark - 1:
            print(i)
        else:
            print(i, end=" ")
    print("Second loop - inspection with continue:")
    for i in range(Alku, Loppu):
        if i == Tark:
            continue
        elif i == Loppu - 1:
            print(i)
        else:
            print(i, end=" ")

print("\nProgram ending.")