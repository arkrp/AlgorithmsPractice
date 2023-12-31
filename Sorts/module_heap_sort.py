from ..DataStructures import Heap
def heap_sort(array):
    myheap = Heap()
    for i in array:
        myheap.push(i)
    return(list(myheap))
if __name__ == "__main__":
    from .tests import test_sort
    test_sort(heap_sort)
    
    
