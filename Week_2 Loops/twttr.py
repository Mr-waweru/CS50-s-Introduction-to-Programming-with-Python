# ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
user_input = input("Input: ")
vowels = "aeiouAEIOU"
for vowel in vowels:
    user_input = user_input.replace(vowel, "")
print(f"Output: {user_input}")



"""
user_input = input("Input: ")
vowels = "aeiouAEIOU"
output = ''.join([char for char in user_input if char not in vowels])
print(f"Output: {output}")
"""