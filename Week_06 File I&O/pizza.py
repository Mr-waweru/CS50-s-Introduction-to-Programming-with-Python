import sys, csv
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    csv_file = sys.argv[1]
    if csv_file.endswith(".csv"):
        try:
            with open(csv_file) as file:
                reader = csv.DictReader(file)
                print(tabulate(reader, headers= "keys", tablefmt="grid"))
        except FileNotFoundError:
            sys.exit("File does not exist")
    else:
        sys.exit("Not a CSV file")
