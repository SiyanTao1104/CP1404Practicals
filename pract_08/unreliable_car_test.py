"""
CP1404 Practical
Siyan Tao
Unreliable Car class text
"""
from pract_08.unreliable_car import UnreliableCar

n = 1
m = 10


def main():
    """ Text Unreliable Car class"""
    first_car = UnreliableCar("BMW", 100, 80)
    second_car = UnreliableCar("Bentley", 100, 8)

    for i in range(n, m):
        print("When cars start to drive {}km:".format(i))
        print("{} drove {}km".format(first_car.name, first_car.drive(i)))
        print("{} drove {}km".format(second_car.name, second_car.drive(i)))

    print(first_car)
    print(second_car)


main()