def create_dictionary(names):
    new_dict = {}
    for name in names:
        new_dict.setdefault(name[0], []).append(name)
    for key in new_dict.keys():
        new_dict[key].sort()
    return new_dict

names= []

print("Enter the names plz (leave empty then press enter to stop): ")
while True:
    name = input()
    name = name.replace(" ", "_")
    if(name == ""):
        break
    names.append(name)
print(create_dictionary(names))