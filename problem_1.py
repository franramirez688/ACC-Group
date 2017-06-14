#!/usr/bin/env python3

"""
Problem 1

A palindromic number reads the same both ways. The largest palindrome made from the

product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers
"""


def get_largest_palindromic_number(num_digits):
    """Calculate the largest palindromic number, given the digits

    :param num_digits: :class:`int` number of digits
    :return: :class:`int` largest number
    """
    assert num_digits > 0, "Enter a number of digits >= 0"

    import itertools

    largest_num = int('9' * num_digits)
    _max = 0
    _max_range = largest_num + 1

    # More or less with similar execution time than using nested for with range()
    for x, y in itertools.product(range(_max_range, -1 , -1), repeat=2):
        r = x * y
        if _is_palindromic(r):
            _max = r if _max < r else _max
    return _max


def _is_palindromic(num):
    """Check if is palindromic the number passed

    :param num: :class:`int`
    :return: :class:`boolean`
    """
    str_num = str(num)
    return str_num == str_num[::-1]


if __name__ == '__main__':
    import sys

    n_digits = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    result = get_largest_palindromic_number(num_digits=n_digits)
    print(result)
