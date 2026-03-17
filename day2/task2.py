def character_locator(str, character):
    indices = []
    for i in range(len(str)):
        if character.lower() == str[i].lower():
            indices.append(i)
    return indices
val = input("Enter a name plz: ")
ch = input("Enter a character to search for plz: ")
print(f"the indices are {character_locator(val, ch)}")