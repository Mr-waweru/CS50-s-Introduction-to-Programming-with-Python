cost = int(input("Enter the cost of an item(0 to end): "))
total = 0

while cost != 0:
    total += cost
    cost = int(input("Enter the cost of an item(0 to end): "))
print(f"Grand Total: {total}")
total_dis = total * 0.50
print("Total price with discount: {total_dis}")
