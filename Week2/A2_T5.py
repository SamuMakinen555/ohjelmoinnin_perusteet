#Program starting.
print("Program starting.\n")
#Insert a closed compound word: Moonbanana
Word = input("Insert a closed compound word: ")
#The word you inserted is 'Moonbanana' and in reverse it is 'ananabnooM'.
print(f"The word you inserted is '{Word}' and in reverse it is '{(Word[::-1])}'.")
#The inserted word length is 10
print(f"The inserted word length is {len(Word)}")
#Last character is 'a'
print(f"Last character is '{Word[-1]}'\n")

#Take substring from the inserted word by inserting...
#1) Starting point: 0
#2) Ending point: 4
#3) Step size: 1
print(f"Take substring from the inserted word by inserting...")
start1 = int(input("1) Starting point: "))
end1 = int(input("2) Ending point: "))
step1 = int(input("3) Step size: "))

#The word 'Moonbanana' sliced to the defined substring is 'Moon'.
print(f"\nThe word '{Word}' sliced to the defined substring is '{Word[start1:end1:step1]}'.")
#Program ending.
print("Program ending.")
