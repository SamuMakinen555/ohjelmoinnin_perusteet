print("Hello World!")
print("Here we are")

print("He said: \"Hello\", and kept walking.")
print("He said hello \n \r \t \b and \\and kept walking")

exampleString = "Text and numb3rs"
exampleInt = 12
exampleFloat = 12.12
exampleBoolean = False

#Firstname = input("What is your first name: ")
#Lastname = input("What is your last name: ")
#print(f"Hello ",  Firstname,  Lastname)

Sentence = "Finding substring"
print(Sentence)
print(Sentence[0]) # Antaa lauseen ensimmäisen merkin
print(Sentence[-2]) # Antaa lauseen toiseksi viimeisen merkin
print(Sentence[2:9]) # Antaa lauseen merkit 3-9
print(Sentence[:9]) # Antaa lauseen merkit alusta 9:ään
print(Sentence[-9:-2])
print(Sentence[2:9:3]) # Antaa lauseen merkit 3-9, mutta hyppää 3 merkkiä kerrallaan
print(Sentence[::3])
print(Sentence[::-1])

#name = "Mira"
#age = 48

#print(name, age)
#print(name + age) # Tämä ei toimi
#print(name + " " + str(age)) # Tämä toimii

num1 = input("Anna luku 1 ") # Vaihtoehtohan olisi käyttää juurikin tuota int input, esim; #Num1 = int(input(Anna luku1 )
num2 = input("Anna luku 2 ")

num3 = int(num1) + int(num2)
print(num3)
