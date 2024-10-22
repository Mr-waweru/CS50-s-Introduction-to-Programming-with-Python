#Create a bot that accepts a message the loop only breaks one "done" is entered 
"""
while True:
    msg = input("Message (done to end): ")
    if msg != "done":
        print("We got your message")
    else:
        break

print("Done")
"""

# Create an account login of a user with 2 passwords
"""
password = input("Enter your password: ")

while password != "password001" and password != "password002":
        print("Wrong password")
        password = input("Try again: ")
print("Welcome to your account!")
"""

#First 3 people to book are gifted a 20% off
"""
name1 = input("name? ")
name = 0
while name < 3:
    print(f"Congrats! {name1}")
    name += 1
    name2 = input("name? ")
    print(f"Congrats! {name2}")
    name3 = input("name? ")
    print(f"Congrats! {name3}")
    break
print("All done")
"""

# User must enter a programming language. Only 5 entries
# if user enters "python" print off how many tries it took
"""
user_input = 0
language = ""
while user_input < 5 and language != "python":
    language = input("Enter programming language: ")
    user_input += 1
if language == "python":
    print(f"It took you {user_input} tries")
"""

#Train ticket booking program
train_tickets = input("Enter 1 - book or 2 - end booking: ")
i = 1
while train_tickets != "2":
    if train_tickets == "1":
        print(f"Train ticket: {i}")
        i += 1
    train_tickets = input("Enter 1 - book or 2 - end booking: ")




