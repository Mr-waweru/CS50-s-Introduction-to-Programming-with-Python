def main():
    fraction_input = input("Fraction: ")
    result = fraction_to_percentage(fraction_input)
    if result <= 1:
        print("E")
    elif result >= 99:
        print("F")
    else:
        print(f"{result:.0f}%")
    #print(f"{result}%")


def fraction_to_percentage(fraction):
    while True:
        try:
            numerator, denominator = map(int, fraction.split('/'))
            percentage = (numerator / denominator) * 100
            if percentage <= 1 or percentage >= 99:
                break
            return round(percentage)
            
        except (ValueError, ZeroDivisionError):
            continue


if __name__ == "__main__":      
    main()