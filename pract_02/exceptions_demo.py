"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

"""
When will a ValueError occur?
"""
# Numerator and denominator must be valid numbers
"""
When will a ZeroDivisionError occur?
"""
# Cannot divide by zero
"""
Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

valid_input = False
numerator = 0
denominator = 0
while not valid_input:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        if numerator == 0 or denominator ==0 :
            print("numerator and denominator can not be 0")
            numerator = int(input("Enter the numerator: "))
            denominator = int(input("Enter the denominator: "))
        fraction = numerator / denominator
        numerator = True
        denominator = True
        print(fraction)
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
print("Finished")