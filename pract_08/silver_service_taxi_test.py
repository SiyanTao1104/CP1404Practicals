"""
CP1404 Practical
Siyan Tao
Silver service taxi class test
"""

from pract_08.silver_service_taxi import SilverServiceTaxis


def main():
    test_taxi = SilverServiceTaxis("Number one taxi", 100, 2)
    test_taxi.drive(18)
    print(test_taxi)
    print(test_taxi.get_fare())


main()