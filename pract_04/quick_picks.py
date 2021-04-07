"""
CP1404 Practical
Quick pick program
"""

import random

numbers_each_line = 6
minimum = 1
maximum = 45


def main():
    quick_pick_numbers = int(input("How many quick picks? "))
    while quick_pick_numbers < 0:
        print("Number Invalid")
        quick_pick_numbers = int(input("How many quick picks? "))

    for i in range(quick_pick_numbers):
        quick_pick = []
        for _ in range(numbers_each_line):
            number = random.randint(minimum, maximum)
            while number in quick_pick:
                number = random.randint(minimum, maximum)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick))


main()