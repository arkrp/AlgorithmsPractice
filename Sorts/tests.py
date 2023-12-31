import logging
import random

print('test module loaded: Logging level set to DEBUG')
logging.basicConfig(level=logging.DEBUG)

def test_in_place_sort(sort_function_in_place,*, list_size=10, random_seed=4):
    """tests an in place sorting function"""
    logging.debug('Testing in-place sort!')
    random.seed(random_seed)
    original_list = [i for i in range(list_size)]
    shuffled_list = original_list[:]
    random.shuffle(shuffled_list)
    sorted_list = shuffled_list[:]
    sort_function_in_place(sorted_list)
    if not lists_are_equal(original_list,sorted_list):
        logging.debug(f'test failed')
    else:
        logging.debug(f'test sucessful')
    print(f'{original_list=}\n{shuffled_list=}\n{sorted_list=}') 

def test_sort(sort_function,*, list_size=10, random_seed=4):
    """tests an in place sorting function"""
    logging.debug('Testing in-place sort!')
    random.seed(random_seed)
    original_list = [i for i in range(list_size)]
    shuffled_list = original_list[:]
    random.shuffle(shuffled_list)
    sorted_list = sort_function(shuffled_list[:])
    if not lists_are_equal(original_list,sorted_list):
        logging.debug(f'test failed')
    else:
        logging.debug(f'test sucessful')
    print(f'{original_list=}\n{shuffled_list=}\n{sorted_list=}') 

def lists_are_equal(list1, list2): #f
    """returns if two lists have equal elements all the way through"""
    if len(list1)!=len(list2):
        return false
    for i in zip(list1,list2):
        if i[0] != i[1]:
            return False
    return True
#d
