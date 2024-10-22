# Adieu, adieu, to Liesl
# Adieu, adieu, to Liesl and Friedrich
# Adieu, adieu, to Liesl, Friedrich, and Louisa
# Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
# Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
# Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
# Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl

import inflect
p = inflect.engine()

"""
text = ["Adieu", "adieu"]

while True:
    try:
        n = input("Name: ")
    except EOFError:
        print()
        break
    text.append(n)
text[2] = "to " + text[2]


if len(text) == 3:
    new_text = p.join(text, conj="")
elif len(text) == 4:
    new_text = p.join(text, final_sep="")
else:
    new_text = p.join(text)

print(new_text)
"""

# Alternatively
names = []

while True:
    try:
        n = input("Name: ")
        names.append(n)
    except EOFError:
        print()
        break

output = p.join(names)
print(f"Adieu, adieu, to " + output)













