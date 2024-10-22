"""  
i = 0
while i < 3:
    print("meow")
    i += 1 # same thing as i = i + 1
"""

# for _ in range(2): 
#    print("meow")

# \n prints vertically end="" no empty space at the end
#print("meow\n" * 3, end="")

"""
while True:
    n = int(input("what's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")
"""

def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("what's n? "))
        if n > 0:
            break
    return n 


def meow(n):
    for _ in range(n):
        print("meow")


main()