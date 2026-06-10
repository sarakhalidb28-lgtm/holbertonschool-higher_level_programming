#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Defines structural unit tests for the max_integer function."""

    def test_ordered_list(self):
        """Tests a standard ordered list of increasing integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Tests an unordered list where max is in the middle."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Tests a list where the maximum value is the first element."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty_list(self):
        """Tests passing an explicit empty list."""
        self.assertEqual(max_integer([]), None)

    def test_no_arguments(self):
        """Tests calling the function with no parameters (default list)."""
        self.assertEqual(max_integer(), None)

    def test_one_element_list(self):
        """Tests a list containing only a single element."""
        self.assertEqual(max_integer([7]), 7)

    def test_all_negative_numbers(self):
        """Tests a list filled entirely with negative integers."""
        self.assertEqual(max_integer([-1, -5, -3, -2]), -1)

    def test_mixed_integers(self):
        """Tests a list containing both positive and negative integers."""
        self.assertEqual(max_integer([-10, 5, -3, 0, 4]), 5)

    def test_identical_elements(self):
        """Tests a list where all elements are identical."""
        self.assertEqual(max_integer([9, 9, 9, 9]), 9)

    def test_floats_and_integers(self):
        """Tests a list containing a mix of floats and integers."""
        self.assertEqual(max_integer([1.5, 2.7, 4, 3.9]), 4)


if __name__ == '__main__':
    unittest.main()
