def remove_vowels(str):
    vowels = ['a', 'e', 'i', 'u', 'o']
    new_str = str
    for i in str:
        if i.lower() in vowels:
            new_str = new_str.replace(i, "")
    return new_str

val = input("Enter a name plz: ")
print(f"the old string is {val}\nafter removing the vowels: {remove_vowels(val)}")