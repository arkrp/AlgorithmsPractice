def insertion_sort(array):
    for index in range(1,len(array-1)):
        initialvalue = array[index]
        while((index!=0) and (array[index-1]>array[index])):
            array[index]=array[index-1]
            index = index-1
        array[index] = initialvalue


