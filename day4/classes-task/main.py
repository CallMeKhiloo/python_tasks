from Car import Car
from Person import Person
from Employee import Employee
from Office import Office


def simulate_fuel_consumption(car, distance_km):
    consumed = (distance_km / 10) * 10
    car.fuelRate = max(0, car.fuelRate - consumed)
    return car.fuelRate


def main():
    iti = Office("ITI Smart Village", [])

    fiat_128 = Car(name="Fiat 128", fuelRate=100, velocity=40)

    samy = Employee(
        name="Samy",
        money=2000,
        mood="Happy",
        healthRate=90,
        car=fiat_128,
        email="samy@iti.gov",
        salary=5000,
        distanceToWork=20
    )

    samy.id = 1

    iti.hire(samy)

    print(f"Office: {iti.name}")
    print(f"Employees count (all offices): {Office.employeesNum}")
    print(f"Samy distance to work: {samy.distanceToWork} km")

    travel_time = samy.distanceToWork / samy.car.velocity
    print(f"Travel time at {samy.car.velocity} km/h: {travel_time:.2f} hour(s)")

    # Case 1: move at 8:30 -> arrives at 9:00 (not late)
    move_hour = 8.5
    checker = iti.check_lateness if hasattr(iti, "check_lateness") else iti.check_latenes
    was_late = checker(empId=1, moveHour=move_hour)
    print(f"Move at {move_hour}: late? {was_late}, salary={samy.salary}")

    # Case 2: slower speed, move at 8:30 -> late
    samy.car._Car__velocity = 20
    was_late = checker(empId=1, moveHour=8.5)
    print(f"Move at 8.5 with 20 km/h: late? {was_late}, salary={samy.salary}")

    remaining_fuel = simulate_fuel_consumption(samy.car, samy.distanceToWork)
    print(f"Fuel after 20 km trip: {remaining_fuel}% (expected 80% from 100%)")


if __name__ == "__main__":
    main()