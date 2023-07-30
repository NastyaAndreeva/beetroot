def pig_it(text):
    word_list = text.split(" ")
    new_list = []
    for word in word_list:
        if not word.isalnum():
            new_list.append(word)
        else:
            new_list.append(word[1:] + word[0] + "ay") 
    return " ".join(new_list)


print(pig_it('Pig latin is cool')) # igPay atinlay siay oolcay
print(pig_it('Hello world !'))     # elloHay orldway !