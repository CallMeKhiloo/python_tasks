name = input("What is your name ?")

if name.isalpha():
    print(f"Hello, {name}!")
else:
    print("Please enter a valid name containing only letters.")