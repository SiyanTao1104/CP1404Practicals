"""
CP1404/CP5632 - Practical
Random number
Various examples of using Python string formatting with the str.format() method
Want to read more about it? https://docs.python.org/3/library/string.html#formatstrings
"""
"""
What did you see on line 1? 

What was the smallest number you could have seen, what was the largest?

"""
# there will show the number between 5 to 20, 5 is the smallest number, 20 is the largest.
"""
What did you see on line 2?
What was the smallest number you could have seen, what was the largest?
Could line 2 have produced a 4?
"""
# On line 2, only 3, 5, 7, 9 between 3 to 10. 3 is the smallest number, 9 is the largest number. No
"""
What did you see on line 3?
What was the smallest number you could have seen, what was the largest?
"""
# On line 3, the number which shows has decimal numbers. 2.628101995129376 is the smallest number I have seen,
# 5.2950680921101565 is the largest number I have seen.
"""
Write code, not a comment, to produce a random number between 1 and 100 inclusive.
"""
import random
random_number=random.randint(1,100)
print(random_number)
