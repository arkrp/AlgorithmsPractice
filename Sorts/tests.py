import random
def test_in_place_sort(sort_function_in_place,*, list_size=10, random_seed=4):
    print('Testing sort!')
    random.seed(random_seed)
    original_list = [i for i in range(list_size)]
    shuffled_list = original_list[:]
    random.shuffle(shuffled_list)
    sorted_list = shuffled_list[:]
    sort_function_in_place(sorted_list)
    if not lists_are_equal(original_list,sorted_list):
        print(f'test failed\noriginal list:\n{original_list}\nshuffled list:\n{shuffled_list}\nsorted list:\n{sorted_list}') 
    else:
        print(f'test sucessful\noriginal list:\n{original_list}\nshuffled list:\n{shuffled_list}\nsorted list:\n{sorted_list}')
def lists_are_equal(list1, list2):
    if len(list1)!=len(list2):
        return false
    for i in zip(list1,list2):
        if i[0] != i[1]:
            return False
    return True
