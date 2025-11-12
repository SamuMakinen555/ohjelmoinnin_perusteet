def main():
    print(f"Program starting.")
    print(f"This program analyses a list of names from a file.")
    fileName = input(f"Insert filename to read: ")
    print (f'Reading names from "{fileName}".')

    with open(fileName, 'r') as File:
        Namelist = []
        for name in File:
            if name == '\n' or '':
                continue
            else:
                Namelist.append(name.strip())
    
    print(f"Analysing names...")
    print(f"Analysis complete!")

    Count = len(Namelist)
    Shortest = len(min(Namelist, key=len))
    Longest = len(max(Namelist, key=len))
    Average = sum(len(x) for x in Namelist) / Count

    # print(f"count {Count} shortest {Shortest} longest {Longest}")

    print(f"#### REPORT BEGIN ####")
    print(f"Name count - {Count}")
    print(f"Shortest name - {Shortest} chars")
    print(f"Longest name - {Longest} chars")
    print(f"Average name - {Average:.2f} chars")
    print(f"#### REPORT END ####")
    print(f"Program ending.")

if __name__ == "__main__":
    main()