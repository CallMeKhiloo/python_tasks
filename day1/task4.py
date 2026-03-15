full_name = input("Please enter your full name: ")

if len(full_name.split()) <= 2:
    name_list = full_name.split()
    print(f"Hello, {full_name}! with initials: ")
    for name in name_list:
        print(f"{name[0].upper()} ")
else:
    print("Please enter a valid full name with at most two words.")