print("Amount Due: 50")
amount_due = 50
coins = [5, 10, 25]

while amount_due > 0:
	insert_coin = int(input("Insert Coin: "))
	if insert_coin in coins:
		amount_due -= insert_coin
		if amount_due > 0:
			print(f"Amount Due: {amount_due}")
		else:
			print(f"Change Owed: {abs(amount_due)}")
	else:
		print(f"Amount Due: {amount_due}")




