def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# All vanity plates must start with at least two letters.
# vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
# Numbers cannot be used in the middle of a plate; they must come at the end. 
# No periods, spaces, or punctuation marks are allowed.

def is_valid(s):
    if len(s) >= 2 and len(s) <= 6 and s[0:2].isalpha() and s.isalnum():
        for char in s:
            if char.isdigit():
                index = s.index(char)
                if s[index:].isdigit() and char != "0":
                    return True
                else:
                    return False
        return True
    return False


main()