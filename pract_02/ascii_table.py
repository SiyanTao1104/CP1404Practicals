"""
CP1404/CP5632 - Practical
ASCII table and converter
"""
character = str(input("Enter a character: "))
print("The ASCII code for {} is {}".format(character, ord(character)))
number = int(input("Enter a number between 33 and 127: "))
while number < 33 or number > 127:
    number = int(input("Enter a number between 33 and 127: "))
print("The character for {} is {}".format(number, chr(number)))