"""
CP1404 Practical -
Client code to use the Car class.
"""

from pract_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("Toyota",180)
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))

    limo = Car("Limo", 100)
    limo.add_fuel(20)
    print("Limo fuel = {}".format(limo.fuel))
    limo.drive(115)
    print("After driving 115km, Limo odometer = {}".format(limo.odometer))
    print(limo)

main()