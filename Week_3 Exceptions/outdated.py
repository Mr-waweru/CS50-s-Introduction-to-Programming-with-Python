# month-day-year order, formatted like 9/8/1636 or,
# September 8, 1636
# output that same date in YYYY-MM-DD format

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ")
    if "/" in date:
        month, day, year = date.split("/")
    elif "," in date:
        date = date.replace(",", "")
        month, day, year = date.split(" ")
        if month in months:
            month = months.index(month) + 1
    try:
        if int(month) > 12 or int(day) > 31:
            continue
        else:
            break
    except ValueError:
        continue
    
print(f"{year}-{int(month):02}-{int(day):02}")






















