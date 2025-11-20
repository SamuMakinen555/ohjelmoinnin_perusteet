WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday")

def readFile(PFilename: str, PRows: list[str]) -> None:
    print('Reading file "{}".'.format(PFilename))
    # 0. Clear PRows list just in case
    PRows.clear()
    # 1. Open filehandle
    file = open(PFilename, 'r', encoding="UTF-8")
    # 2. Read filehandle line-by-line
    # file.readline(PFilename)
    next(file)
    for line in file:
        if line == "\n":
            continue
        else:
            PRows.append(line.strip())
    # 2.1. Skip first line (header row)
    # 2.2. Check if line is empty '\n'
    # 2.3. Add non empty datarow without newline at the end.
    # 3. Close filehandle 
    file.close()
    return None

def analyseTimestamps(PRows: list[str], PResults: list[str]) -> None:
    print("Analysing timestamps.")
    PResults.clear()

    # Append results to the PResults list
    # Initialise helper list 
    WeekdayTimestampAmount: list[int] = [0, 0, 0, 0, 0, 0, 0]
    for i in PRows:
        for j, day in enumerate(WEEKDAYS):
            if i.startswith(day):
                WeekdayTimestampAmount[j] += 1
    # Iterate rows with i
    #   Iterate WEEKDAYS with j
    #      Check if the row starts with the weekday name
    #          Count the day in proper place
    PResults.append("### Timestamp analysis ###")
    for i in range(len(WEEKDAYS)):
        PResults.append(f" - {WEEKDAYS[i]} {WeekdayTimestampAmount[i]} stamps")
    PResults.append("### Timestamp analysis ###")
    WeekdayTimestampAmount.clear()
    # Iterate WEEKDAYS with i and append the daily results
    # Clear the helper list
    return None

def displayResults(PResults: list[str]) -> None:
    print("Displaying results.")
    # Iterate results and print for the user
    for i in PResults:
        print(i)
    return None

def main() -> None:
    # 1. Initialise
    # 1.1. Initialise rows list
    Rows: list[str] = [] #List for storing file rows
    # 1.2. Initialise results list
    Results: list[str] = [] # List for storing analysis results
    # 2. Operate
    print("Program starting.")
    # 2.1. Ask user to define filename
    Filename = input("Insert filename: ")
    # 2.2. Read file
    readFile(Filename, Rows) # Jump to readFile function, send reference to the rows list as a function parameter
    # 2.3. Analyse rows
    analyseTimestamps(Rows, Results) # Jump to analyseTimestamps function, send reference to the Rows and Resulsts lists as function parameters
    # 2.3. Display results
    displayResults(Results)
    # 3. Cleanup
    # 3.1. Clear lists
    Rows.clear()
    Results.clear()
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()
