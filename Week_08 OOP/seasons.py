from datetime import date
import sys, inflect

p = inflect.engine()

def main():
    try: 
        year, month, day = input("Date of birth: ").split("-")  #YYYY-MM-DD format
    except ValueError:
        sys.exit("Invalid date")

    print(minutes_lived(year, month, day))


def minutes_lived(year, month, day):
    try: 
        dob = date(int(year), int(month), int(day))
    except ValueError:
        return "Invalid date"
    today_date = date.today()
    date_diff = today_date - dob
    minutes = int(date_diff.total_seconds() / 60)
    msg = p.number_to_words(minutes, andword="")
    return (f"{msg} minutes").capitalize()
    


if __name__ == "__main__":
    main()