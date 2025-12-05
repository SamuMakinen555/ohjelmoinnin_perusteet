from dataclasses import dataclass

@dataclass
class TIMESTAMP:
    consumption: float
    price: float


DELIMITER = ";"
WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday")

def readTimestamps(Filename: str, Rows: list[str]) -> None:
    print(f'Reading file "{Filename}".')
    Rows.clear()
    with open(Filename, 'r', encoding="UTF-8") as file:
        next(file)
        for line in file:
            if line == "\n":
                continue
            else:
                Rows.append(line.strip())
    
    return None

def analyseTimestamps(Rows, Results):
    print("Analysing timestamps.")
    Results.clear()
    DayUsage: list[float] = [0] * len(WEEKDAYS)
    DayCost: list[float] = [0] * len(WEEKDAYS)
    for line in Rows:
        Row = line.strip()
        Columns = Row.split(DELIMITER)
        Timestamp = TIMESTAMP
        Timestamp.consumption = float(Columns[2])
        Timestamp.price = float(Columns[3])
        Total = Timestamp.consumption * Timestamp.price
        for i, day in enumerate(WEEKDAYS):
            if Row.startswith(day):
                DayUsage[i] += Timestamp.consumption
                DayCost[i] += Total
                
    Results.append("### Electricity consumption summary ###")
    for i in range(len(WEEKDAYS)):
        Results.append(f" - {WEEKDAYS[i]} usage {DayUsage[i]:.2f} kWh, cost {DayCost[i]:.2f} €")
    Results.append("### Electricity consumption summary ###")
    return None    

def displayResults(Results):
    print("Displaying results.")
    for i in Results:
        print(i)
    return None

def main():
    print("Program starting.")
    Rows = []
    Results = []
    Filename = input("Insert filename: ")
    readTimestamps(Filename, Rows)
    analyseTimestamps(Rows, Results)
    displayResults(Results)
    print("Program ending.")

if __name__ == "__main__" or "unittest" in __import__("sys").modules:
    main()