import unittest
import insertion.insertionSort as Algorithm


class TestInsertionSort(unittest.TestCase):
    def setUp(self):
        print '\n\n======================== START ========================'

    def test_avg_case(self):
        source = [6, 8, 12, 11, 15, 13, 20, 3, 10]
        result = Algorithm.insertion_sort(source)
        self.assertEqual(result, [3, 6, 8, 10, 11, 12, 13, 15, 20])

    def test_worst_case(self):
        source = [20, 15, 13, 12, 11, 10, 8, 6, 3]
        result = Algorithm.insertion_sort(source)
        self.assertEqual(result, [3, 6, 8, 10, 11, 12, 13, 15, 20])

    def test_best_case(self):
        source = [3, 6, 8, 10, 11, 12, 13, 15, 20]
        result = Algorithm.insertion_sort(source)
        self.assertEqual(result, [3, 6, 8, 10, 11, 12, 13, 15, 20])


if __name__ == '__main__':
    unittest.main(verbosity=2)
