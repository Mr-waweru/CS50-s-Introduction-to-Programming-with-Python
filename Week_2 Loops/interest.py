# Python Compound Interest Calculator

principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter principle amount: "))
    if principle < 0:
        print("Principle can't be less than zero!")
    else:
        break

while True:
    rate = float(input("Enter interest rate: "))
    if rate < 0:
        print("Interest rate can't be less than zero!")
    else:
        break

while True:
    time = int(input("Enter time in years: "))
    if time < 0:
        print("Time can't be less than zero!")
    else:
        break

total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: Ksh{total:.2f}")