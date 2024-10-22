import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]: # [1:] slicing from index 1 to end
    print("hello, my name is", arg)




