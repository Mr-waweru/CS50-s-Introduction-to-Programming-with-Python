def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))


def convert(fraction):
    while True:
        try:
            numerator, denominator = map(int, fraction.split("/"))
            if denominator == 0:
                raise ZeroDivisionError     
            if numerator > denominator:
                raise ValueError
                    
            percentage = (numerator / denominator) * 100
            return round(percentage)
        
        except ValueError:
            raise ValueError
        except ZeroDivisionError:
            raise ZeroDivisionError
            
        # except (ValueError, ZeroDivisionError):
        #     fraction = input("Fraction: ")


def gauge(percentage):
    if percentage <= 1:
        return("E")
    elif percentage >= 99:
        return("F")
    else:
        return(f"{percentage:.0f}%")


if __name__ == "__main__":
    main()




