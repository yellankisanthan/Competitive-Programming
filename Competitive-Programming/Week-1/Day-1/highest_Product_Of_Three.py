import sys
import unittest
maxi = sys.maxsize
mini = -sys.maxsize-1

def highest_product_of_3(arr):
    if len(arr) < 3:
        raise ValueError("...........")

    first_highest = mini
    second_highest = mini
    third_highest = mini
    first_lowest = maxi
    second_lowest = maxi

    for i in range(0,len(arr)):
        if arr[i] > first_highest:
            third_highest = second_highest
            second_highest = first_highest
            first_highest = arr[i]

        elif arr[i] > second_highest:
            third_highest = second_highest
            second_highest = arr[i]

        elif arr[i] > third_highest:
            third_highest = arr[i]

        if arr[i] < first_lowest:
            second_lowest = first_lowest
            first_lowest = arr[i]

        elif arr[i] < second_lowest:
            second_lowest = arr[i]

    return max((first_lowest*second_lowest*first_highest),(first_highest*second_highest*third_highest))

# Tests

class Test(unittest.TestCase):

    def test_short_list(self):
        actual = highest_product_of_3([1, 2, 3, 4])
        expected = 24
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = highest_product_of_3([6, 1, 3, 5, 7, 8, 2])
        expected = 336
        self.assertEqual(actual, expected)

    def test_list_has_one_negative(self):
        actual = highest_product_of_3([-5, 4, 8, 2, 3])
        expected = 96
        self.assertEqual(actual, expected)

    def test_list_has_two_negatives(self):
        actual = highest_product_of_3([-10, 1, 3, 2, -10])
        expected = 300
        self.assertEqual(actual, expected)

    def test_list_is_all_negatives(self):
        actual = highest_product_of_3([-5, -1, -3, -2])
        expected = -6
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            highest_product_of_3([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1])

    def test_error_with_two_numbers(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1, 1])


unittest.main(verbosity=2)