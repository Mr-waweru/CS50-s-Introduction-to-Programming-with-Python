def main():
    greeting = input("Greetings: ")
    output = (value(greeting))
    print(f"${output}")


def value(greeting):
    greeting = greeting.lower().strip()
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()


