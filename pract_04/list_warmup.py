"""
CP1404 practical
List warm up
"""
numbers = [3, 1, 4, 1, 5, 9, 2]
print(numbers[0])
print(numbers[-1])
print(numbers[3])
print(numbers[:-1])
print(numbers[3:4])
print(5 in numbers)
print(7 in numbers)
print("3" in numbers)
print(numbers + [6, 5, 3])

"""Change the first element of numbers to "ten" (the string, not the number 10)"""
numbers[0] = "10"
"""Change the last element of numbers to 1"""
numbers[-1] = 1
"""Get all the elements from numbers except the first two (slice)"""
numbers[2:]
"""Check if 9 is an element of numbers"""
9 in numbers
