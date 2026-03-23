class Human:
    country = "Egypt"
    def __init__(self, name):
        self.name = name

h1 = Human("mohamed")
h1.country = "USA"
h2 = Human("ahmed")
print(h1.__dict__)
print(h2.__dict__)