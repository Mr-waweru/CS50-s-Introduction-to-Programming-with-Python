while True:
    try:
        fuel_fraction = input("Fraction: ")
        numerator, denominator = map(int, fuel_fraction.split("/"))
        percentage = (numerator / denominator) * 100
        if percentage <= 1 or percentage >= 99:
            break
    except (ValueError, ZeroDivisionError):
        continue
    else:
        break

if percentage <= 1:
    print("E")
elif percentage >= 99:
    print("F")
else:
    print(f"{percentage:.0f}%")



"""
def main():
    fraction_input = input("Fraction: ")
    result = fraction_to_percentage(fraction_input)
    print(f"{result}%")


def fraction_to_percentage(fraction):
    try:
        numerator, denominator = map(int, fraction.split('/'))
        percentage = (numerator / denominator) * 100
        return round(percentage)
    except (ValueError, ZeroDivisionError):
        return 

          
main()
"""