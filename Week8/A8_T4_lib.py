from datetime import datetime

MONTHS = (
    "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"
    )

WEEKDAYS =(
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
)

def readTimestamps(filename):
    timestamps  = []
    with open(filename, 'r', encoding="UTF-8") as file:
        for line in file:
            line = line.strip()
            ts = datetime.fromisoformat(line)
            timestamps.append(ts)
    return timestamps

def calculateYears(timestamps, year):
    return sum(1 for ts in timestamps if ts.year == year)

def calculateMonths(timestamps, month):
    return sum(1 for ts in timestamps if MONTHS[ts.month -1] == month.capitalize())

def calculateWeekdays(timestamps, weekday):
    return sum(1 for ts in timestamps if WEEKDAYS[ts.weekday()] == weekday.capitalize())

