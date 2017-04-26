import unittest
import merge.mergeSort as Algorithm


class TestHeapSort(unittest.TestCase):

    def test_sort(self):
        array = [2, 4, 1, 6, 8, 5, 3, 7]
        Algorithm.merge_sort(array)
        print 'Final Array: %s' % array
        self.assertEqual(array, [1,2,3,4,5,6,7,8])

if __name__ == '__main__':
    unittest.main()