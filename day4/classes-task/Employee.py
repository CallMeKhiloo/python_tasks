from Person import Person
from datetime import datetime

class Employee(Person):
    id = 0

    def __init__(self, name, money, mood, healthRate, car, email, salary, distanceToWork):
        super().__init__(name, money, mood, healthRate)
        self.id = id
        self.car = car
        if "@" not in email:
            raise ValueError("Invalid email address")
        else:
            self.__email = email
        self.salary = salary
        self.distanceToWork = distanceToWork
        Employee.id += 1

    def work(self, hours):
        if hours == 8:
            self.mood = "Happy"
        elif hours > 8:
            self.mood = "Tired"
        else:
            self.mood = "Lazy"

    def drive(self, distance, velocity):
        self.car.run(distance, velocity)

    def refuel(self, gasAmount = 100):
        self.car.fuelRate += gasAmount

    def send_mail(self, to, subject, msg, receiver_name):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file_name = f"email_{timestamp}.txt"
        sender = self.name
        email_content = f"""From: {sender}
    To: {to}

    Hi, {receiver_name}
    {msg}

    {subject}"""
        with open(file_name, "w") as email_file:
            email_file.write(email_content)

        print(f"Success! {file_name} has been generated.")
