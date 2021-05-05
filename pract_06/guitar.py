"""CP1404 Siyan Tao
Practical -
Guitar example.
"""
from datetime import date


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return print("{} ({}) : ${}".format(self.name, self.year, self.cost))

    def get_age(self):
        current_date = date.today()
        return current_date.year - self.year

    def is_vintage(self):
        return self.get_age() >= 50

    def __lt__(self, other):
        return self.year < other.year
