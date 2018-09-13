# Python101

from utils.test_rig import O


# ----- test cases ----------------------------

@O.k
def dummy_fail():
    """..this test should fail.."""
    assert 1 == 2


@O.k
def testing_page5():
    """Whitespace Formatting"""

    test_variable = (1 + 2 + 3 + 4 + 5)
    assert test_variable == 15


@O.k
def testing_page6():
    """Modules"""

    from math import remainder
    test_variable = remainder(10, 4)
    assert test_variable == 2


@O.k
def testing_page7():
    """Arithmetic"""

    test_variable = 10 / 4
    assert test_variable == 2.5


@O.k
def testing_page8():
    """Functions"""

    def abbreviate_phrase(phrase):
        words = phrase.split()
        result = ""
        for word in words:
            if word[0].isupper():
                result += word[0]
        return result

    assert abbreviate_phrase("Foundations of Software Science") == "FSS"
    assert abbreviate_phrase("Test All Upper") == "TAU"
    assert abbreviate_phrase("test all lower") == ""


@O.k
def testing_page9():
    """Strings"""

    single_quoted_test_string = 'Howdy!'
    assert len(single_quoted_test_string) == 6


@O.k
def testing_page10():
    """Exceptions"""

    def throw_something():
        try:
            raise RuntimeError
        except RuntimeError:
            return "Runtime Exception Encountered"

    assert throw_something() == "Runtime Exception Encountered"


@O.k
def testing_page11():
    """Lists"""

    test_list = [1, 2, 3, 4, 5]

    assert sum(test_list) == 15
    assert test_list[-2] == 4
    assert test_list[2:4] == [3, 4]


@O.k
def testing_page12():
    """Lists"""

    _, x, _, _ = [1, 2, 3, 4]
    assert x == 2


@O.k
def testing_page13():
    """Tuples"""

    def return_multiple_values():
        return 1, 5

    test_tuple = return_multiple_values()
    assert test_tuple[1] == 5


@O.k
def testing_page14():
    """Dictionaries"""

    capitals = {
        "India": "New Delhi",
        "China": "Beijing",
        "USA": "Washington, D.C.",
        "France": "Paris",
        "South Africa": ["Capetown", "Bloemfontein", "Pretoria"]
    }

    # This test fails due to chaining comparision operators.
    assert not "India" in capitals == True

    assert "India" in capitals
    assert capitals["South Africa"][2] == "Pretoria"
    assert capitals.get("Japan", "Not Found") == "Not Found"
    assert len(capitals) == 5
    assert str("Brazil" in capitals.keys()) == "False"


@O.k
def testing_page15():
    """Default Dictionaries"""

    from collections import defaultdict

    def is_default(dictionary):
        try:
            dictionary["Num1"] += 1
            return True
        except KeyError:
            return False

    test_dict = {}
    test_default_dict = defaultdict(int)

    assert is_default(test_default_dict) == True
    assert is_default(test_dict) == False


@O.k
def testing_page16():
    """Counters"""

    from collections import Counter

    test_counter = Counter(["Hi", "Hello", "Howdy", "Hola", "Hi"]).most_common(1)
    assert test_counter == [("Hi", 2)]

@O.k
def testing_page17():
    """Sets"""

    some_list = [1, 1, 2, 2, 3, 3, 4, 4]
    test_set = set(some_list)

    assert len(some_list) == 8
    assert len(test_set) == 4
    assert test_set == {1, 2, 3, 4}


@O.k
def testing_page17_again():
    """Membership Test"""

    from time import time_ns as get_time

    some_string = """We’ll use sets for two main reasons. The first is that in is a very fast operation on sets. If
        we have a large collection of items that we want to use for a membership test, a set is more appropriate than a 
        list. We’ll use sets for two main reasons. The first is that in is a very fast operation on sets. If we have a 
        large collection of items that we want to use for a membership test, a set is more appropriate than a list. We’ll 
        use sets for two main reasons. The first is that in is a very fast operation on sets. If we have a large collection 
        of items that we want to use for a membership test, a set is more appropriate than a list. We’ll use sets for two 
        main reasons. The first is that in is a very fast operation on sets. If we have a large collection of items that we 
        want to use for a membership test, a set is more appropriate than a list"""

    test_list = some_string.split()
    test_set = set(test_list)

    start_time_list = get_time()
    "items" in test_list
    time_taken_list = get_time() - start_time_list

    start_time_set = get_time()
    "items" in test_set
    time_taken_set = get_time() - start_time_set

    assert time_taken_set <= time_taken_list


@O.k
def testing_page18():
    """Control Flow"""

    def test_ternary(x):
        return "Zero" if x == 0 else "Non-Zero"

    assert test_ternary(0) == "Zero"
    assert test_ternary(1) == "Non-Zero"


@O.k
def testing_page19():
    """Truthiness"""

    empty_string = ""
    non_empty_string = "A non empty string."
    a_none = None

    def is_true(string):
        if string:
            return "Yes"
        else:
            return "No"

    assert is_true(empty_string) == "No"
    assert non_empty_string and non_empty_string[0] == "A"
    assert a_none or "Some" == "Some"


@O.k
def testing_page20():
    """Truthiness - All & Any"""

    assert not all([False, True, 100])
    assert any([False, True, 100])
    assert all([])
    assert not any([])


@O.k
def testing_page22():
    """Sorting"""

    test_list = [4, 5, 3, 7, 6]
    test_list.sort()
    assert test_list == [3, 4, 5, 6, 7]


@O.k
def testing_page23():
    """List Comprehensions"""

    test_list = [x for x in range(6) if x % 2 != 0]
    test_dict = {x: x + 1 for x in range(4)}
    another_list = [(x, y) for x in range(3) for y in range(3)]
    assert test_list == [1, 3, 5]
    assert test_dict == {0: 1, 1: 2, 2: 3, 3: 4}
    assert another_list[2] == (0, 2)


@O.k
def testing_page24():
    """Generators and Iterators"""

    from types import GeneratorType

    def generate_integers(n):
        for i in range(n):
            yield i

    test_generator = generate_integers(10)
    assert isinstance(test_generator, GeneratorType)
    assert next(test_generator) == 0
    assert next(test_generator) == 1

    generator_from_list_comprehensions = (x for x in range(3))
    assert isinstance(generator_from_list_comprehensions, GeneratorType)


@O.k
def testing_page25():
    """Randomness"""

    from random import randrange, seed, random

    assert randrange(0, 4) in [0, 1, 2, 3]

    seed(1)
    pseudo_random_sequence_1 = [int(random() * 100) for _ in range(10)]

    seed(2)
    pseudo_random_sequence_2 = [int(random() * 100) for _ in range(10)]

    seed(1)
    pseudo_random_sequence_3 = [int(random() * 100) for _ in range(10)]

    assert not pseudo_random_sequence_1 == pseudo_random_sequence_2
    assert pseudo_random_sequence_1 == pseudo_random_sequence_3


@O.k
def testing_page26():
    """Regular Expression"""

    from re import search

    assert search("S", "FSS")


@O.k
def testing_page27():
    """Object Orientation"""

    class Car:
        def __init__(self, make="Some", model="Car"):
            self.make = make
            self.model = model

        def name(self):
            return self.make + " " + self.model

    a_car = Car("Honda", "Accord")
    another_car = Car()

    assert a_car.name() == "Honda Accord"
    assert another_car.name() == "Some Car"


@O.k
def testing_page28():
    """Functional Tools - Partial"""

    from functools import partial

    def exponent(base, power):
        return base ** power

    cube_of = partial(exponent, power=3)
    assert cube_of(3) == 27


@O.k
def testing_page29():
    """Functional Tools - Map, Reduce, Filter"""

    from functools import reduce

    a_list = [1, 2, 3, 4, 5]
    doubles = map(lambda x: x * 2, a_list)
    even_doubles = filter(lambda x: x % 2 == 0, doubles)
    sum_of_even_doubles = reduce(lambda x, y: x + y, even_doubles)

    assert sum_of_even_doubles == 30


@O.k
def testing_page30():
    """Enumerate"""

    numbers = ["Zero", "One", "Two", "Three", "Four", "Five"]

    for i, number_string in enumerate(numbers):
        if i == 2:
            assert number_string == "Two"


@O.k
def testing_page31():
    """Zip & Arguement Unpacking"""

    first_list = [0, 1, 2]
    second_list = [3, 4, 5]
    zipped = list(zip(first_list, second_list))
    assert zipped == [(0, 3), (1, 4), (2, 5)]
    assert list(zip(*zipped)) == [(0, 1, 2), (3, 4, 5)]
    assert list(zip((0, 3), (1, 4), (2, 5))) == [(0, 1, 2), (3, 4, 5)]


@O.k
def testing_page32():
    """*Args"""

    def sum_of_two(x, y):
        return x + y

    def sum_of_three(x, y, z):
        return x + y + z

    def square(func):
        def do_it(*args):
            return func(*args) ** 2

        return do_it

    test_two_args = square(sum_of_two)
    test_three_args = square(sum_of_three)

    assert test_two_args(2, 3) == 25
    assert test_three_args(2, 3, 4) == 81


@O.k
def testing_page33():
    """*KwArgs"""

    branch_codes = {}

    def add_items(**kwargs):
        branch_codes.update(kwargs)

    assert not branch_codes

    add_items(csc="Computer Science", ece="Electrical & Computer Engineering")
    assert branch_codes["csc"] == "Computer Science"

    misc = {"abc": "Some Course", "xyz": "Another Course"}
    add_items(**misc)
    assert branch_codes["xyz"] == "Another Course"


if __name__ == "__main__":
    O.report()
