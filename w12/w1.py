# Python101

import re, traceback


class O:
    y = n = 0

    @staticmethod
    def report():
        print("\n# pass= %s fail= %s %%pass = %s%%" % (
            O.y, O.n, int(round(O.y * 100 / (O.y + O.n + 0.001)))))

    @staticmethod
    def k(f):
        try:
            print("\n-----| %s |-----------------------" % f.__name__)
            if f.__doc__:
                print("# " + re.sub(r'\n[ \t]*', "\n# ", f.__doc__))
            f()
            print("# pass")
            O.y += 1
        except:
            O.n += 1
            print(traceback.format_exc())
        return f


# ----- test cases ----------------------------

@O.k
def dummy_fail():
    """this test should fail"""
    assert 1 == 2


@O.k
def testing_page5():
    """Whitespace Formatting"""

    test_variable = (1 + 2 + 3 + 4 + 5)
    assert test_variable == 15


@O.k
def testing_page6():
    """modules"""

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

    assert str("India" in capitals) == "True"
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
            return "True"
        except KeyError:
            return "False"

    test_dict = {}
    test_default_dict = defaultdict(int)

    assert is_default(test_default_dict) == "True"
    assert is_default(test_dict) == "False"


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




if __name__ == "__main__":
    O.report()
