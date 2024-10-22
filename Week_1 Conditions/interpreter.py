x, y, z = input("Expression: ").split(" ")

x = int(x)
z = int(z)

if y == "+":
    print(float(f"{x + z:.1f}"))
elif y == "-":
    print(float(f"{x - z:.1f}"))
elif y == "*":
    print(float(f"{x * z:.1f}"))
elif y == "/":
    print(float(f"{x / z:.1f}"))