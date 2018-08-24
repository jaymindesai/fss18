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
    assert test_list[2:4] == [3,4]


@O.k
def testing_page12():
    """Lists"""

    _, x, _, _ = [1, 2, 3, 4]
    assert x == 2


@O.k
def testing_page13():
    """Tuples"""




if __name__ == "__main__":
    O.report()
