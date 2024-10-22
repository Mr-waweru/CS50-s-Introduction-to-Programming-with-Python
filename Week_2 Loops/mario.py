def main():
    print_square(3)


def print_square(size):
    # For each row in square
    for i in range(size):
        # For each block in row
        for j in range(size):
            # Print brick
            print("#", end="")


        print() # Prints a new line at the end of the row and not at the end of every brick 


main()