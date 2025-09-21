#Make Python program, which prompts user to insert two words. Print the length of each word and then compound them together. Put single quotes around the compound word.

#Example program run:

#Program starting.
print("Program starting.")
#Insert first word: fire
#Insert second word: fighter
Word1 = input("Insert first word: ")
Word2 = input("Insert second word: ")
#1st word is 4 characters long.
print(f"1st word is {len(Word1)} characters long.")
#2nd word is 7 characters long.
print(f"2nd word is {len(Word2)} characters long.")
#Words together makes one closed compound 'firefighter'.
print(f"Words together make one closed compound '{Word1+Word2}'.")
#voisi olla vain '{Word1}{Word2}'
#Program ending.
print("Program ending.")
