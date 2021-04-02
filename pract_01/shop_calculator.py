"""
CP1404/CP5632 - Practical
Student: Siyan Tao
Shop_calculator
"""
number_of_items = int(input("Number of items: "))
total = 0
while number_of_items <= 0:
    print("Invalid number of items")
    number_of_items = int(input("Number of items: "))
for i in range(number_of_items):
    price= float(input("Price of item: "))
    total += price
if total >100:
    total= total * (1-0.1)
print("Total price for", number_of_items, "items is ${:.2f}".format(total))