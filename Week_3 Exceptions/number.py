
while True:
    try:
        x = int(input("what's x? "))        
    except ValueError:
        print("x is not an integer")
    else:
        break # break can also be under input

print(f"x is {x}") 


"""
try:
    x = int(input("what's x? "))        
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")
"""





















