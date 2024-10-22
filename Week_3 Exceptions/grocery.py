shopping_list = {}

while True:
    try:
        item = input("").upper()
        if item not in shopping_list:
            shopping_list[item] = 1
        else:
            shopping_list[item] += 1
    except EOFError:
        break

for item in sorted(shopping_list):
    print(f"{shopping_list[item]} {item}")
        







