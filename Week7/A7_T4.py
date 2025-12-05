from dataclasses import dataclass

@dataclass
class TIMESTAMP:
    weekday: str
    hour: str
    consumption: float
    price: float

DELIMITER = ";"

def readTimestamps(Filename: str, Rows: list[TIMESTAMP]) -> None:
    print(f'Reading file "{Filename}".')
    Rows.clear()
    with open(Filename, 'r', encoding="UTF-8") as file:
        next(file)

        for line in file:
            line = line.strip()
            if line:
                Columns = line.split(DELIMITER)
                timestamp = TIMESTAMP(
                    weekday=Columns[0],
                    hour=Columns[1],
                    consumption=float(Columns[2]),
                    price=float(Columns[3])
                )
                Rows.append(timestamp)
    return None

def analyseTimestamps(Rows, Results):
    Results.clear()
    Results.append("Electricity usage:")
    for line in Rows:
        Row = line.strip()
        Columns = Row.split(DELIMITER)

        timestamp = TIMESTAMP(
            weekday=Columns[0],
            hour=Columns[1],
            consumption=float(Columns[2]),
            price=float(Columns[3])
        )

        Total = timestamp.consumption * timestamp.price
        Results.append(f" - {timestamp.weekday} {timestamp.hour}:00, price {timestamp.price:.2f}, consumption {timestamp.consumption:.2f} kWh, total {Total:.2f} €")

    return None    

    
def displayTimestamps(Results: list[TIMESTAMP]):
    print("Electricity usage:")
    for timestamp in Results:
        Total = timestamp.consumption * timestamp.price
        print(f" - {timestamp.weekday} {timestamp.hour}:00, price {timestamp.price:.2f}, consumption {timestamp.consumption:.2f} kWh, total {Total:.2f} €")
    return None


def main():
    print("Program starting.")
    Rows = []
    # Filename = "A7_T4_D1.csv"
    Filename = input("Insert filename: ")
    readTimestamps(Filename, Rows)
    displayTimestamps(Rows)
    print("Program ending.")

if __name__ == "__main__":
    main()