import requests
import sys, json

# if len(sys.argv) != 2:
#     sys.exit("Missing command line argument")
if len(sys.argv) > 2:
    sys.exit("Too many command line argument")
elif len(sys.argv) < 2:
    sys.exit("Too few command line argument")
else:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    
    try:
        float(sys.argv[1])
    except ValueError:
        sys.exit("Command line arument is not a number")

data = response.json()
price = data["bpi"]["USD"]["rate"]
price = price.replace(",", "")
price = float(price) * float(sys.argv[1])
print(f"${price:,.4f}")

