import random


# Genrating random integer between 0 and 10
def create_random_integers(x: int) -> int:
    random_integer = random.randint(0, x)
    return print(random_integer)

def create_random_floats(x: int) -> float:
    random_float = random.random() * x
    return print(random_float)

# for i in range(10):
#     create_random_floats(i+10)

my_list = [i for i in range(1000)]
random_element = random.choice(my_list)

if random_element > 500:
    print("Random element is greater than 500")