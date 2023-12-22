#f import stuff
import operator
#d
class Heap: #f
    """ #f
    This data structure allows for the fast insertion of elements and a fast removal of the least/greatest element depending on configuration.
    
    After every call, the top of the heap is the minimum/maximum of the values in the heap. (specified by heaptype)
    """
    #d
    __slots__ = ('_memory','_comparator')
    #f interface methods
    def __init__(self, *,heaptype = 'min', values = []): #f
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
    #d
    #f iterator stuff
    def __next__(self): #f
        """ #f
        necissary for iteration
        """
        #d
        if self.is_empty():
            raise StopIteration
        return self.pop()
    #d
    def __iter__(self): #f
        """ #f
        necissary for iteration
        """
        #d
        return self
    #d
    #d
    def push(self, value): #f
        """ #f
        Adds a value to the heap
        """
        #d
        #f append to end
        self._memory.append(value)
        #d
        #f fix ordering at end
        lastposition = len(self._memory)-1
        self._fix_order_upwards(lastposition)
        #d
    #d
    def pop(self): #f
        """
        Removes a value from the top of the heap
        """
        #f declare variables!
        memory = self._memory
        start = 0
        end = len(memory) - 1
        #d
        #f swap the root with the last node
        temp = memory[start]
        memory[start] = memory[end]
        memory[end] = temp
        #d
        #f remove the former root
        returnvalue = memory.pop()
        #d
        #f fix the root borked heap
        self._fix_order_downwards(0)
        #d
        #f return the former root
        return returnvalue
        #d
    #d
    def peek(self):
        """
        Gets the top value of the heap
        """
        try:
            return self._memory[0]
        except IndexError as e:
            raise IndexError("Peek was called on an empty heap. Peek requires that there be at lease one element in the heap!") from e
    def is_empty(self): #f
        """
        Gets whether the heap is empty
        """
        return len(self._memory) == 0 #d
    def copy(self): #f
        """
        Creates a shallow copy of the heap
        """
        return Heap(values = self._memory.copy()) #d
    #d
    #f helper methods
    #f private methods
    def _fix_order_upwards(self, position): #f
        """ #f
        Fixes a value being too low on the heap
        """
        #d
        memory = self._memory
        #f if we are on top then there is nothing to fix!
        if position == 0:
            return
        #d
        #f if we are out of order, fix the order!
        #f locate the parent node
        parentposition = self.getParentPosition(position)
        #d
        #f deal with being out of order
        if self._comparator(memory[position],memory[parentposition]):
            #f swap upwards
            temp = memory[parentposition]
            memory[parentposition] = memory[position]
            memory[position] = temp
            #d
            #f fix the parent position
            self._fix_order_upwards(parentposition)
            #d
        #d
        #d
        #d
    def _fix_order_downwards(self, position): #f
        """ #f
        fix a node being higher than it should be
        """
        #d
        memory = self._memory
        #f find the children
        left = self.getLeftChildPosition(position)
        right = self.getRightChildPosition(position)
        #d
        #f deal with having no children
        if left >= len(memory):
            return
        #d
        #f deal with having two children
        if right < len(memory):
            #f deal with parent lowest (or equal)
            if (self._comparator(memory[position],memory[right]) and
                self._comparator(memory[position],memory[left])):
                return
            #d
            #f deal with right child lowest
            if self._comparator(memory[right],memory[left]):
                #f swap with right child
                temp = memory[position]
                memory[position] = memory[right]
                memory[right] = temp
                #d
                #f fix right child
                self._fix_order_downwards(right)
                #d
                return
            #d
            #f deal with left child lowest (or equal to right child)
            #f swap with left child
            temp = memory[position]
            memory[position] = memory[left]
            memory[left] = temp
            #d
            #f fix left child
            self._fix_order_downwards(left)
            #d
            return
            #d
        #d
        #f deal with having 1 child
        #f deal with parent lowest (or equal)
        if self._comparator(memory[position],memory[left]):
            return
        #d
        #f deal with left child lowest
        #f swap with left child
        temp = memory[position]
        memory[position] = memory[left]
        memory[left] = temp
        #d
        #f fix left child
        self._fix_order_downwards(left)
        #d
        return
        #d
        #d #d
    #d
    #f static methods
    @staticmethod
    def getParentPosition(position): #f
        return (position - 1)//2 #d
    @staticmethod
    def getLeftChildPosition(position): #f
        return position * 2 + 1 #d
    @staticmethod
    def getRightChildPosition(position): #f
        return position * 2 + 2 #d
    #d
    #d
#d
