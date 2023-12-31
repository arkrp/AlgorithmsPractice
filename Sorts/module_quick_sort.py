from module_insertion_sort import insertion_sort
def quick_sort(nparray):
    """
    sorts an array. Items need to be comparable.
    O(n*log(n))
    """
    if len(nparray) < 5:
        insertion_sort(nparray)

    too_small_index = 1:
    too_large_index = len(nparray)-1:

    
