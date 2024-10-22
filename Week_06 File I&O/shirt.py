import sys, os

from PIL import Image, ImageOps

if len(sys.argv) == 3:
    extensions = [".jpg", ".jpeg", ".png"]
    ext_1 = os.path.splitext(sys.argv[1])
    ext_2 = os.path.splitext(sys.argv[2])

    if ext_1[1].lower() == ext_2[1].lower() and ext_1[1] in extensions:
        try:
            user_image = Image.open(sys.argv[1], "r")
        except FileNotFoundError:
            sys.exit("Input odoes not exist")

        shirt = Image.open("shirt.png")
        size = shirt.size
        user_image = ImageOps.fit(user_image, size)
        user_image.paste(shirt, shirt)
        user_image.save(sys.argv[2])

    elif ext_2[1].lower() != ext_1[1].lower() and ext_1[1] in extensions:
        sys.exit("Input and output have different extensions")
    elif ext_2[1] not in extensions:
        sys.exit("Invalid input")

elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")