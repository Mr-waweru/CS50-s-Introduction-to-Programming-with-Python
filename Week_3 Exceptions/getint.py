def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            x = int(input("what's x? ")) # Alt. return int(input("what's x? "))        
        except ValueError:
            print("x is not an integer")
        else:
            return x # Will break out of the loop and also return a value


main()








