import unittest
from module_insertion_sort import insertion_sort
class TestSort(unittest.TestCase):
    def test_insertion_sort(self):
        self._test_in_place_sorting_algorithm("insertion",insertion_sort)
    def _test_in_place_sorting_algorithm(self, sort_name, sort_function):
        print(f'starting sort test: {sort_name}')
        unsorted_list = [9,1,4,6,2,3,10]
        manually_sorted_list = [1,2,3,4,6,9,10]
        sorted_list = unsorted_list.copy()
        sort_function(sorted_list)
        print('unsorted list:'.rjust(23) + str(unsorted_list))
        print('sorted list:'.rjust(23) + str(sorted_list))
        print('manually sorted list:'.rjust(23) + str(manually_sorted_list))
        self.assertTrue(
                self._array_is_equal(
                    sorted_list,
                    manually_sorted_list
                    )
                )
    @staticmethod
    def _array_is_equal(array1, array2):
        if len(array1) != len(array2):
            return false
        for index in range(len(array1)):
            if array1[index] != array2[index]:
                return False
        return True
if __name__ == '__main__':
    print('hey this code runs?')
    unittest.main()
    


