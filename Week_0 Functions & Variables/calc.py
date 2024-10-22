"""
x = float(input("what's x: "))
y = float(input("what's y: "))

z = x + y
print(f"{z:,}")
"""

def main():
    x = int(input("what's x? "))
    print(f"{x} squared is {square(x)}")

def square(n):
    return n ** 2

main()