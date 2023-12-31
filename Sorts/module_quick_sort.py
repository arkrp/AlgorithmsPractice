import logging
def quick_sort(array):
    #f docstring
    """
    in place sorting function
    items need to be comparable
    Complexity: Theta(n*log(n))
    Always selects the first item as a pivot
    """
    #d
    def swap_indicies(index1,index2): #f
        temp = array[index1]
        array[index1] = array[index2]
        array[index2] = temp
    #d
    def quick_sort_section(left_side_index,right_side_index): #f
        logging.debug(f'quick_sort_selection {left_side_index=} {right_side_index=}')
        logging.debug(f'{array=}')
        #f docstring
        """
        recursively quick sorts a section
        left_size_index is inclusive
        right_size_index is exclusive
        """
        #d
        def find_too_large_index(): #f
            nonlocal too_large_index
            while( too_large_index<=right_side_index-1 and
                  array[too_large_index]<array[pivot_index] ):
                too_large_index += 1
        #d
        def find_too_small_index(): #f
            nonlocal too_small_index
            while( too_small_index>=left_side_index and
                  array[too_small_index]>array[pivot_index] ):
                too_small_index -= 1
        #d
        #f do nothing if the section is of length one or less
        if right_side_index - left_side_index <= 1:
            logging.debug('base case reached')
            return
        #d
        #f create variables!
        pivot_index = left_side_index
        too_large_index = left_side_index + 1
        too_small_index = right_side_index - 1
        #d
        #f swap things to the correct side!
        while too_large_index < too_small_index:
            #f find the too large and too small
            find_too_small_index()
            find_too_large_index()
            #d
            #f move the large and small to the correct position!
            if too_large_index < too_small_index:
                swap_indicies( too_small_index , too_large_index )   
            #d
        #d
        #f swap pivot to middle
        center_index = too_large_index - 1
        swap_indicies( pivot_index , center_index )
        logging.debug(f'pivot {array[center_index]} placed at {center_index}')
        #d
        #f recurse!
        quick_sort_section( left_side_index, center_index )
        quick_sort_section( center_index+1, right_side_index )
        #d
    #d
    quick_sort_section(0,len(array))
if __name__ == "__main__":
    from .tests import test_in_place_sort
    test_in_place_sort(quick_sort)

    
