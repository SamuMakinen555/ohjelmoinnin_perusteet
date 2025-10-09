print("Program starting.\n")
print("Check multiplicative persistence.")

Luku = int(input("Insert an integer: "))
Kirj = str(Luku)
Step = 0
Loppu = len(Kirj)

while True:
    if Luku < 10:
        print("No more steps.")
        break
    else:
        for i in range(0, Loppu):
            if i == 0:
                print(f"{Kirj[0:1]}", end="")
                Luku = int(Kirj[0:1])
            else:
                print(f" * {Kirj[i:i+1]}", end="")
                Luku = Luku * int(Kirj[i:i+1])
        print(f" = {Luku}")
        Step += 1
        Kirj = str(Luku)
        Loppu = len(Kirj)

print(f"\nThis program took {Step} step(s)")
print("\nProgram ending.")