#   import stuff
import operator
# 
class Heap: #  
    """ #  
    This is a container which allows for quick access to extreme elements.

    This data structure allows for the fast insertion of elements and a fast removal of the least/greatest element depending on configuration.
    
    After every call, the top of the heap is the minimum/maximum of the values in the heap. (specified by heaptype)
    """
    # 
    __slots__ = ('_memory','_comparator')
    #   interface methods
    def __init__(self, *,heaptype = 'min', values = []): #  
        """
        optional parameters:
        heaptype: determine whether this heap should prioritize min or max 
            'min': the minimum value should exit first
            'max': the maximum value should exit first
        values: a list of values you want placed in the heap immediately
        """
        self._memory = []
        if heaptype == 'min':
            self._comparator = operator.lt 
        elif heaptype == 'max':
            self._comparator = operator.gt
        else:
            raise ValueError("You passed an incorrect type parameter to the heap; Heap type must be either \'min\' or \'max\'!")
        for value in values:
            self.push(value)
    # 
    def __next__(self): #  
        """ #  
        necissary for iteration
        """
        # 
        if self.is_empty():
            raise StopIteration
        return self.pop()
    # 
    def __iter__(self): #  
        """ #  
        necissary for iteration
        """
        # 
        return self
    # 
    def push(self, value): #  
        """ #  
        Adds a value to the heap
        """
        # 
        #   append to end
        self._memory.append(value)
        # 
        #   fix ordering at end
        lastposition = len(self._memory)-1
        self._fix_order_upwards(lastposition)
        # 
    # 
    def pop(self): #  
        """
        Removes a value from the top of the heap
        """
        #   declare variables!
        memory = self._memory
        start = 0
        end = len(memory) - 1
        # 
        #   swap the root with the last node
        temp = memory[start]
        memory[start] = memory[end]
        memory[end] = temp
        # 
        #   remove the former root
        returnvalue = memory.pop()
        # 
        #   fix the root borked heap
        self._fix_order_downwards(0)
        # 
        #   return the former root
        return returnvalue
        # 
    # 
    def peek(self): #  
        """
        Gets the top value of the heap
        """
        try:
            return self._memory[0]
        except IndexError as e:
            raise IndexError("Peek was called on an empty heap. Peek requires that there be at lease one element in the heap!") from e
    # 
    def is_empty(self): #  
        """
        Gets whether the heap is empty
        """
        return len(self._memory) == 0 # 
    def copy(self): #  
        """
        Creates a shallow copy of the heap
        """
        return Heap(values = self._memory.copy()) # 
    # 
    #   helper methods
    #   private methods
    def _fix_order_upwards(self, position): #  
        """ #  
        Fixes a value being too low on the heap
        """
        # 
        memory = self._memory
        #   if we are on top then there is nothing to fix!
        if position == 0:
            return
        # 
        #   if we are out of order, fix the order!
        #   locate the parent node
        parentposition = self.getParentPosition(position)
        # 
        #   deal with being out of order
        if self._comparator(memory[position],memory[parentposition]):
            #   swap upwards
            temp = memory[parentposition]
            memory[parentposition] = memory[position]
            memory[position] = temp
            # 
            #   fix the parent position
            self._fix_order_upwards(parentposition)
            # 
        # 
        # 
        # 
    def _fix_order_downwards(self, position): #  
        """ #  
        fix a node being higher than it should be
        """
        # 
        memory = self._memory
        #   find the children
        left = self.getLeftChildPosition(position)
        right = self.getRightChildPosition(position)
        # 
        #   deal with having no children
        if left >= len(memory):
            return
        # 
        #   deal with having two children
        if right < len(memory):
            #   deal with parent lowest (or equal)
            if (self._comparator(memory[position],memory[right]) and
                self._comparator(memory[position],memory[left])):
                return
            # 
            #   deal with right child lowest
            if self._comparator(memory[right],memory[left]):
                #   swap with right child
                temp = memory[position]
                memory[position] = memory[right]
                memory[right] = temp
                # 
                #   fix right child
                self._fix_order_downwards(right)
                # 
                return
            # 
            #   deal with left child lowest (or equal to right child)
            #   swap with left child
            temp = memory[position]
            memory[position] = memory[left]
            memory[left] = temp
            # 
            #   fix left child
            self._fix_order_downwards(left)
            # 
            return
            # 
        # 
        #   deal with having 1 child
        #   deal with parent lowest (or equal)
        if self._comparator(memory[position],memory[left]):
            return
        # 
        #   deal with left child lowest
        #   swap with left child
        temp = memory[position]
        memory[position] = memory[left]
        memory[left] = temp
        # 
        #   fix left child
        self._fix_order_downwards(left)
        # 
        return
        # 
        #  # 
    # 
    #   static methods
    @staticmethod
    def getParentPosition(position): #  
        return (position - 1)//2 # 
    @staticmethod
    def getLeftChildPosition(position): #  
        return position * 2 + 1 # 
    @staticmethod
    def getRightChildPosition(position): #  
        return position * 2 + 2 # 
    # 
    # 
# 
#  test functionality!
if __name__ == '__main__':
    print('testing heap')
    sorted_list = [1,2,3,4,5,6,7,8]
    print('creating heap with values')
    myheap = Heap(heaptype = 'min', values=[7,6,5,4])
    sucessful = True
    print('testing value insertion')
    for i in [3,2,1,8]:
        myheap.push(i)
    print('removing from heap')
    for i in zip(myheap,sorted_list):
        print(f'heap value, specificaion: {i[0]} , {i[1]}')
        if i[0]!=i[1]:
            sucessful = False
    if sucessful:
        print('heap sort sucessful!')
    else:
        print('heap sort failed!')
# 
