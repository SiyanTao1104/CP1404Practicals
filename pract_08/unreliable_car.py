"""
CP1404 Practical
Siyan Tao
Unreliable Car class
"""
from random import randint
from pract_08.car import Car


class UnreliableCar(Car):
    """Unreliable car class"""

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        random_number = randint(1, 100)
        if random_number >= self.reliability:
            distance = 0
        distance_drive = super().drive(distance)
        return distance_drive
