def main():
    word = input("Input: ")
    new_word = (shorten(word))
    print(f"Output: {new_word}")


def shorten(word):
    vowels = "aeiouAEIOU"
    for vowel in vowels:
        word = word.replace(vowel, "")
    return(word)


if __name__ == "__main__":
    main()


# user_input = input("Input: ")
# vowels = "aeiouAEIOU"
# for vowel in vowels:
#     user_input = user_input.replace(vowel, "")
# print(f"Output: {user_input}")