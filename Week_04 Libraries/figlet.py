import sys, random
from pyfiglet import Figlet


figlet = Figlet()

fonts = figlet.getFonts() # Get a list of available fonts

if len(sys.argv) == 1:
    figlet.setFont(font=random.choice(fonts))
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in fonts:
    figlet.setFont(font=sys.argv[2]) # Set the font from user input @ index 2
else:
    sys.exit("Invalid usage")

s = input("Input: ")
print(figlet.renderText(s))











