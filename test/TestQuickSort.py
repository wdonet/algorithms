import unittest
import time
from random import randint
import quick.quick_sort as algorithm

from common.validations import validate_sorted_array


LEN_INPUT = 10000


# Test it with: python3 -m unittest test/TestQuickSort.py
class TestQuickSort(unittest.TestCase):

    def setUp(self):
        print('\n\n======================== START ========================')

    def test_avg(self):
        input_array = [randint(0, LEN_INPUT) for _ in range(LEN_INPUT)]

        print('Testing average case')
        start = time.time()
        algorithm.quick_sort(input_array)
        end = time.time()
        print('Time: ', end - start)

        self.assertTrue(validate_sorted_array(input_array))

    def test_worst(self):
        input_array = [x for x in range(LEN_INPUT, 0, -1)]

        print('Testing worst case')
        start = time.time()
        algorithm.quick_sort(input_array)
        end = time.time()
        print('Time: ', end - start)

        self.assertTrue(validate_sorted_array(input_array))

    def test_best(self):
        input_array = [x for x in range(LEN_INPUT)]

        print('Testing best case')
        start = time.time()
        algorithm.quick_sort(input_array)
        end = time.time()
        print('Time: ', end - start)

        self.assertTrue(validate_sorted_array(input_array))


if __name__ == '__main__':
    unittest.main(verbosity=2)
