#!/usr/bin/env python3

"""
Problem 2

Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral

is formed as follows:

                21 22 23 24 25

                20 7 8 9 10

                19 6 1 2 11

                18 5 4 3 12

                17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the

same way?
"""


def get_sum_of_diagonals_number(spiral_upper_limit):
    """Efficient way to calculate the sum of spiral diagonal

           (nxn) - (n-1)     --         nxn

             |               1           |

        (nxn) - 2 *(n-1)     --    (nxn) - 3 *(n-1)

    :param spiral_upper_limit: :class:`int`odd number
    :return: :class:`int` diagonal sum
    """
    assert spiral_upper_limit % 2 > 0 and spiral_upper_limit > 1, "Number must be odd and greater than 1"
    result = 1
    for n in range(spiral_upper_limit, 0, -2):
        if n == 1:
            break
        # More efficient than using result = set() and adding the results
        result += 4 * n * n - 6 * (n - 1)
    return result


if __name__ == '__main__':
    import sys

    spiral_upper_limit = int(sys.argv[1]) if len(sys.argv) > 1 else 1001
    result = get_sum_of_diagonals_number(spiral_upper_limit)
    print(result)
