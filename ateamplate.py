import unittest
import re
from utils import read_input

values = read_input("day.txt")
sample = []


def get_foo():
    return 1


class Test(unittest.TestCase):
    def test_case(self):
        v = get_foo()
        self.assertEqual(1, 1)


if __name__ == "__main__":
    unittest.main()
