def insertion_sort(array):
    for index in range(1,len(array)):
        initial_value = array[index]
        while((index!=0) and (array[index-1]>initial_value)):
            array[index] = array[index-1]
            index = index - 1
        array[index] = initial_value
if __name__ == "__main__":
    from .tests import test_in_place_sort
    test_in_place_sort(insertion_sort)

