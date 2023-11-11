from Heap import Heap
myheap = Heap(values=[110,3,4,2,4,4,6])
for i in [1,4,6,2,3,5]:
    myheap.push(i)
for i in myheap:
    print(i)
