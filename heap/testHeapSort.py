import unittest
import heapSortHerrera


class TestHeapSort(unittest.TestCase):

    def test_it(self):
        source = [6, 8, 12, 11, 15, 13, 20, 3, 10]
        result = heapSortHerrera.heap_sort(source)
        self.assertEqual(result, [3, 6, 8, 10, 11, 12, 13, 15, 20])

if __name__ == '__main__':
    unittest.main()
