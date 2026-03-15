name = input("What is your name? ")
age = input("Enter your age: ")

print(f"{name} is {age} years old.")
print("{0} is {1} years old.".format(name, age))
print("{name} is {age} years old.".format(name=name, age=age))
