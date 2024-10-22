# Define main function
def main():
    text = input("convert: ")
    # Call convert function
    print(convert(text))

# Define convert function
def convert(newtext):
    return newtext.replace(":)","🙂").replace(":(","🙁")

main()