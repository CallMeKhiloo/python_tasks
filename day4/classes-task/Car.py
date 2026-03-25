class Car:
    def __init__(self, name, fuelRate, velocity):
        self.name = name
        if fuelRate < 0 or fuelRate > 100:
            raise ValueError("Fuel rate should be between 0 and 100")
        else:
            self.__fuelRate = fuelRate
        if velocity < 0 or velocity > 200:
            raise ValueError("Velocity should be between 0 and 200")
        else:
            self.__velocity = velocity

    def run(self, distance, velocity):
        self.velocity = velocity
        fuel_consumed = distance * 0.1
        if fuel_consumed > self.fuelRate:
            distance_covered = self.fuelRate / 0.1
            self.velocity = 0
            self.fuelRate = 0
            self.stop(distance - distance_covered)
        else:
            self.fuelRate -= fuel_consumed
            self.stop(0)

    def stop(self, distance_remaining = 0):
        if distance_remaining > 0:
            print(f"The car stopped due to running out of fuel and the remaining distance is {distance_remaining}.")
        else:
            print("The car stopped successfully.")

    @property
    def velocity(self):
        return self.__velocity
    
    @property
    def fuelRate(self):
        return self.__fuelRate
    
    @fuelRate.setter
    def fuelRate(self, value):
        if value < 0:
            self.__fuelRate = 0
        elif value > 100:
            self.__fuelRate = 100
        else:
            self.__fuelRate = value