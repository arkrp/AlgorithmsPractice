import unittest
from module_insertion_sort import insertion_sort
class TestSort(unittest.TestCase):
    def test_sort(self):
        mylist = [15,45,234,12,3,5,234,23,14,5,7,4]
        insertion_sort(mylist)
        self.assertTrue(self.is_sorted(mylist))
    @staticmethod
    def _is_sorted(array):
        for index in range(len(array)-1):
            if array[index] > array[index+1]:
                return False
        return True
if __name__ == '__main__':
    unittest.main()
    


