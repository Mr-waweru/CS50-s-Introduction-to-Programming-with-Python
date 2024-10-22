# .strip() remove white space .tittle() capitalize the first name letter
name = input("what's your name? ").strip().title()
first, last = name.split(" ")

print(f"Hello, {first}")

