class Person:
    moods = ("Happy", "Tired", "Lazy")

    def __init__(self, name, money, mood, healthRate):
        self.name = name
        if(money < 1000):
            raise ValueError("Money should be at least 1000")
        else:
            self.__money = money
        self.mood = mood
        if healthRate < 0 or healthRate > 100:
            raise ValueError("Health rate should be between 0 and 100")
        else:
            self.__healthRate = healthRate

    def sleep(self, hours):
        if hours == 7:
            self.mood = "Happy"
        elif hours < 7:
            self.mood = "Tired"
        else:
            self.mood = "Lazy"

    def eat(self, meals):
        if meals == 3:
            self.healthRate = "100%"
        elif meals == 2:
            self.healthRate = "75%"
        elif meals == 1:
            self.healthRate = "50%"

    def buy(self, items):
        self.money -= items * 10