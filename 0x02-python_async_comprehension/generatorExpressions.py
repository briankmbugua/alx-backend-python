"""Genrators are a powerful feature in python, that allows you to create iterators in a concise and memory efficient way.They are similar to list comprehesions, but the do not construct list object. Instead, they return a special object called generator object to supply the next value in a sequence."""

# Syntax
"""Generator expressions use parentheses '() and have a similar syntax as list comprehensions. Instead of creating a list and keeping the whole sequence in memory, they create an iterable generator object, that generates one item at a time."""

squares_gen = (x*x for x in range(10))

# Lazy Evaluation
"""Lazy evaluation is an evaluation strategy which delays the evaluation of an expression until its value is needed. In this way, we can avoid unnecessary computations and improve the performance of our program. Lazy evaluation is used in the context of normal order and call-by-need evaluation of programming languages. Generator expressions implement lazy evaluation. This is useful when the input data are large, or even infinite."""
# Elements are generated one at a time as you iterate over the generator.

for square in squares_gen:
    print(square) # Generates one element at a time

# conversion to other data structures
# squares_list = List(squares_gen)

# Generator Functions
"""You can create generator functions using the yield keyword.They are more flexible and allow for custom logic for generating values"""

def custom_generator():
    for i in range(5):
        yield i

print(custom_generator)