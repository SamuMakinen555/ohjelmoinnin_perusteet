print("Program starting.\n")

i = 0
Char = 0
while True:
    Word = input("Insert word (empty stops): ")
    i += 1
    Char += len(Word)
    if Word == "":
        i -= 1
        break
    else:
        continue

print("\nYou inserted:")
print(f"- {i} words")
print(f"- {Char} characters")

print("\n Program ending.")