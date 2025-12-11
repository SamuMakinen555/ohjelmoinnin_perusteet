def readValues(filename: str):
    values = []

    with open(filename, 'r', encoding="UTF-8") as file:
        for line in file:
            if line == '\n':
                continue
            else:
                values.append(float(line))
    
    return values

def calculateSum(values):
    Sum = round(sum(values), 1)
    return Sum

def calculateAverage(values):
    Average = round(sum(values) / len(values), 1)
    return Average

def showOptions():
    print("\nOptions:")
    print("1 - Read values")
    print("2 - Amount of values")
    print("3 - Calculate sum of values")
    print("4 - Calculate average of values")
    print("0 - Exit")
    return None