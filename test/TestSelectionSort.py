import unittest
import time
from random import randint
import selection.selection_sort as algorithm

from common.validations import validate_sorted_array


class TestSelectionSort(unittest.TestCase):
    def setUp(self):
        print('\n\n======================== START ========================')

    def test_avg(self):
        input_array = [randint(0, 10000) for _ in range(10000)]

        print('Testing average case')
        start = time.time()
        algorithm.selection_sort(input_array)
        end = time.time()
        print('Time: ', end - start)

        self.assertTrue(validate_sorted_array(input_array))

    def test_worst(self):
        input_array = [x for x in range(10000, 0, -1)]

        print('Testing worst case')
        start = time.time()
        algorithm.selection_sort(input_array)
        end = time.time()
        print('Time: ', end - start)

        self.assertTrue(validate_sorted_array(input_array))

    def test_best(self):
        input_array = [x for x in range(10000)]

        print('Testing best case')
        start = time.time()
        algorithm.selection_sort(input_array)
        end = time.time()
        print('Time: ', end - start)

        self.assertTrue(validate_sorted_array(input_array))


if __name__ == '__main__':
    unittest.main(verbosity=2)
