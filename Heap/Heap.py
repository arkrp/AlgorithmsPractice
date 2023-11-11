class Heap:
    #f docstring
    """
    Generic Minimum Heap.
    Place items on it in log(n) time
    pop the minimum item out in log(n) time
    please only insert items which are comparable
    very useful data structure
    """
    #d
    #f define attributes
    __slots__ = ('_memory')
    _memory: list
    #d
    #f define interface
    def __init__(self, *, values = []): #f
        self._memory = []
        for value in values:
            self.push(value) #d
    def __next__(self): #f
        if self.empty():
            raise StopIteration
        return self.pop() #d
    def __iter__(self):
        return self
    def push(self, value): #f
        #f docstring
        """
        inserts an elements into the heap
        """
        #d
        #f append to end
        self._memory.append(value)
        #d
        #f fix ordering at end
        lastposition = len(self._memory)-1
        self._fixOrderUpwards(lastposition)
        #d
    #d
    def pop(self): #f
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
        self._fixOrderDownwards(0)
        #d
        #f return the former root
        return returnvalue
        #d
    #d
    def empty(self): #f
        return len(self._memory) == 0 #d
    def copy(self): #f
        return Heap(values = self._memory.copy()) #d
    #d
    #f define private methods
    def _fixOrderUpwards(self, position): #f
        #f docstring
        """
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
        if memory[position] < memory[parentposition]:
            #f swap upwards
            temp = memory[parentposition]
            memory[parentposition] = memory[position]
            memory[position] = temp
            #d
            #f fix the parent position
            self._fixOrderUpwards(parentposition)
            #d
        #d
        #d
        #d
    def _fixOrderDownwards(self, position): #f
        """
        fix a node being higher than it should be
        """
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
            if memory[position] <= memory[right] and memory[position] <= memory[left]:
                return
            #d
            #f deal with right child lowest
            if memory[right] < memory[left]:
                #f swap with right child
                temp = memory[position]
                memory[position] = memory[right]
                memory[right] = temp
                #d
                #f fix right child
                self._fixOrderDownwards(right)
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
            self._fixOrderDownwards(left)
            #d
            return
            #d
        #d
        #f deal with having 1 child
        #f deal with parent lowest (or equal)
        if memory[position] <= memory[left]:
            return
        #d
        #f deal with left child lowest
        #f swap with left child
        temp = memory[position]
        memory[position] = memory[left]
        memory[left] = temp
        #d
        #f fix left child
        self._fixOrderDownwards(left)
        #d
        return
        #d
        #d #d
    #d
    #f define static methods
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
