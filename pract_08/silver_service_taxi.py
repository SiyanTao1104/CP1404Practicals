"""
CP1404 week8 Practical
Siyan Tao
Silver service taxi class
"""

from pract_08.taxi import Taxi


class SilverServiceTaxis(Taxi):
    flagfall = 4.5

    def __init__(self, name, flue, fanciness):
        super().__init__(name, flue)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        return "{} plus flagfall of ${:.2f}".format(super().__str__(),
                                                    self.flagfall)

    def get_fare(self):
        return self.flagfall + super().get_fare()