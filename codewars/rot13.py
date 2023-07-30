def rot13(message):
    string = "abcdefghijklmnopqrstuvwxyz"
    new_string = ""
    for i in range(0, len(message)):
        if message[i].lower() in string:
            idx = string.find(message[i].lower())
            new_letter = string[idx + 13 if idx < 13 else idx - 13]
            new_string += new_letter if message[i].islower() else new_letter.upper()
        else:
            new_string += message[i]
    return new_string

# print(rot13("lkaA1bcw"))
# print(rot13("EBG13 rknzcyr.")) #"ROT13 example."
print(rot13("Guvf vf npghnyyl gur svefg xngn V rire znqr. Gunaxf sbe svavfuvat vg! :)"))

