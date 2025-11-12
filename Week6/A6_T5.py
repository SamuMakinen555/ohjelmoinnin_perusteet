def readValues(filename):
    with open(filename, 'r') as File:
       values = []
       for n in File:
           values.append(int(n.strip()))
    return values

def analyseValues(values):
    Sum = sum(values)
    Count = len(values)
    Greatest = max(values)
    Average = sum(values) / len(values)

    Results = (f"Count;Sum;Greatest;Average\n")
    Results += (f"{Count};{Sum};{Greatest};{Average:.2f}\n")
    return Results

def displayResults(Filename, Results):
    print(f"#### Number analysis - START ####")
    print(f'File "{Filename}" results:')
    print(Results)
    print(f"#### Number analysis - END ####")

def main():
    print(f"Program starting.")   
    filename = input(f"Insert filename: ")
    values = readValues(filename)
    analysis = analyseValues(values)
    displayResults(filename, analysis)    
    print(f"Program ending.")

if __name__ == "__main__" or "unittest" in __import__("sys").modules:
    main()