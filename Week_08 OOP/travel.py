class Travel:
    def __init__(self, country, month, type) -> None:
        self.country = country
        self.month = self.get_valid_month(month)
        self.type = type
        self.price = 0

    def get_valid_month(self, month):
        # Use a while loop to re-prompt the user until a valid month is entered
        while not (1 <= int(month) <= 12):
            print("Invalid month! Please enter a month between 1 and 12.")
            month = input("Enter a valid month (1-12): ").strip()
        return int(month)
    
    def trip_info(self):
        if 1 <= self.month <= 12:
            if 10 <= self.month or self.month <= 3:
                return f"You are going to {self.country} in the Winter season! This is a {self.type} trip!"
            elif 4 <= self.month <= 9:
                return f"You are going to {self.country} in the Summer season! This is a {self.type} trip!"
        else:
            return "Invalid Input!"
        
    def calc_cost(self, cost_input):
        costs = []
        while True:
            cost_input = int(input("Enter additional costs (0 to stop): "))
            if cost_input == 0:
                break
            self.price += cost_input
            costs.append(cost_input)

        inspect = self.list_inspect(costs)
        return inspect
        
    def list_inspect(self, costs):
        less_than_ten = 0
        for cost in costs:
            if cost >= 10:
                less_than_ten += 1

        if less_than_ten <= 10:
            self.price += 100
            return f"Updated price: {self.price + flight_cost}"
            

location = input("Enter a country: ").capitalize()
month = input("Enter a month (1-12): ").strip()
trip_type = input("Trip type(Leisure or Business): ").capitalize().strip()

test_trip = Travel(location, month, trip_type)
print(test_trip.trip_info())

flight_cost = int(input("Enter flight cost: "))
updated_price = test_trip.calc_cost(flight_cost)
print(updated_price)