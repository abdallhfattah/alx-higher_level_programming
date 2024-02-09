#!/usr/bin/python3
# 6-max_integer_test.py
"""
Unittest for max_integer([..])
"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class Test_max_int(unittest.TestCase):
    """Unit tests for max_integer([..])."""

    def test_orderedlist(self):
        """testing ordered list"""
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_random(self):
        """testing random numbers"""
        self.assertEqual(max_integer([1, 2, 9999, -99, 124124124]), 124124124)

    def test_negative_numbers(self):
        """testing negative numbers"""
        self.assertEqual(max_integer([-1, -2, -9999, -99, -124124124]), -1)
    
    def test_empty_list(self):
        """testing empty list"""
        self.assertEqual(max_integer([]) , None)
    
    def test_max_begin(self):
        """testing max at begin lists"""
        self.assertEqual(max_integer([5, 1, 4, 2]), 5)

    def test_float(self):
        """testing float lists"""
        self.assertEqual(max_integer([5.5, 1.2, 4.3, 2.1]), 5.5)
    
    def test_str(self):
        """testing str"""
        self.assertEqual(max_integer("ABCDEFGZ") , 'Z')
    
    def test_list_strs(self):
        """testing list of strs"""
        self.assertEqual(max_integer(["abdallah", "roro", "hala" , "zprfix"]), "zprfix")

    def test_empty_str(self):
        """test empty str"""
        self.assertEqual(max_integer("") , None)
