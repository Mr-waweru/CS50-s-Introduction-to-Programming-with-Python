# Create a password checker, if the passsword has an invalid character, print the invalid character
"""
password = input("Enter password: ")
invalid = "!@#$%^&*()?<>"
for letter in password:
    if letter in invalid:
        print(f"{letter} character is not allowed")
"""

# Create a program that counts and prints vowels in an input for a single word
"""
msg = input("Enter your word(s): ")
vowels = "aeiou" 
const = "b, c, d, f, g, h, j, k, l, m, n, p, q, r, s, t, v, w, x, y, z"
vowel_num = 0
for letter in msg:
    if letter in vowels:
        vowel_num += 1
    elif letter in const:
        vowel_num += 0
print(f"{vowels}")
print(f"There are {vowel_num} vowels in the word(s)") 
"""

# Create a program that checks for a valid phone number
# If the program contains anything besides a number print off "Invalid phone number" & break out of the loop
"""
phone = input("Enter phone number: ")
valid = "0123456789+"
for i in phone:
    if i in valid:
        print("Valid Phone Number")
    else:
        print("Invalid Phone Number")
"""

# Create a program that takes a number of guests. For each guest ask their name and age
# If the guest is 18 or older, welcome the guest. Otherwise tell them they must be 18 to drink
 
guests = int(input("Enter number of guests: "))
for i in range(guests):
    name = input("What's your name? ")
    age = int(input("What's your age? "))
    if age < 18:
        print(f"Welcome {name}. You must be 18 to drink!")
    elif age >= 18:
        print(f"Welcome {name}")

