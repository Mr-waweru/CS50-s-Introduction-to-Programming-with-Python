import random


def main():
    ...


def get_level():
    while True:
        level = int(input("Level: "))
        if level not in [1, 2, 3]:
            continue
        return level


def generate_integer(level):
    score = 0
    for i in range(10):
        trials = 1
        if level == 1:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
        elif level == 2:
            x = random.randint(10, 99)
            y = random.randint(10, 99)
        else:
            x = random.randint(100, 999)
            y = random.randint(100, 999)

        while True:
            print(f"{x} + {y} = ", end="")
            answer = input("")
            if answer == (x + y):
                score += 1
                break
            elif answer != (x + y) and trials != 3:
                print("EEE")
                trials += 1
                continue
            else:
                print("EEE")
                print(f"{x} + {y} = {x + y}")
                break




if __name__ == "__main__":
    main()













