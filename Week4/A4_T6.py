print("Program starting.")

Luku = int(input("Insert a positive integer: "))
Step = 0
if Luku > 0:
    while True:
        print(Luku, end="")
        if Luku == 1:
            break
        elif Luku % 2 == 0:
            Luku = Luku // 2
            Step += 1
            print(" -> ", end="")
        else:
            Luku = Luku * 3 + 1
            Step += 1
            print(" -> ", end="")
print(f"\nSequence had {Step} total steps.")
print("\nProgram ending.")