# List comprehension
squares_list = [x**2 for x in range(10)]
print(squares_list)
# Dict comprehension
squares_dict = {x: x**2 for x in range(10)}
print(squares_dict)
# Set comprehension
unique_squares = {x**2 for x in range(10)}
print(unique_squares)
# Tuple comprehension
"""Unlike lists, dictionatries, and sets, tuples are immutable,
so they do not support tuple comprehensions.
To create a tuple you use tuple() or parentheses.
"""

a_tuple = tuple(x for x in range(10))
another_tuple = (0,1,2,3,4,5,6,7,8,9)
