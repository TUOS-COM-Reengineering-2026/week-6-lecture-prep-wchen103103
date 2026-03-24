#import unittest
#from prep import strange_function

#class MyTestCase(unittest.TestCase):
#    def test_strange_function1(self):
#        self.assertEqual(
#            first=strange_function(1, 2, 3, 4),
#            second='behaviour 3'
#        )

    # TODO: Can you write more test cases below to increase the test coverage of `strange_function`?

import unittest
from prep import strange_function

class MyTestCase(unittest.TestCase):

    def test_strange_function1(self):
        self.assertEqual(
            strange_function(1, 2, 3, 4),
            'behaviour 3'
        )

    def test_behaviour_1(self):
        self.assertEqual(
            strange_function(5, 5, 1, 10),
            'behaviour 1'
        )

    def test_behaviour_2(self):
        self.assertEqual(
            strange_function(5, 5, 10, 1),
            'behaviour 2'
        )

    def test_behaviour_4(self):
        self.assertEqual(
            strange_function(10, 5, 1, 2),
            'behaviour 4'
        )

    def test_behaviour_5(self):
        self.assertEqual(
            strange_function(10, 5, 2, 10),
            'behaviour 5'
        )

    def test_behaviour_6(self):
        self.assertEqual(
            strange_function(10, 5, 20, 10),
            'behaviour 6'
        )
