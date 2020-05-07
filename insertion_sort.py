def insertionSort(arr):
    """
    move right through the unsorted portion of a list, ordering to the left in the sorted portion
    arr[0] is alwys the first sorted element
    """
    for i in range(1,len(arr)):
        k = arr[i]
        j = i -1
        while j >=0 and k < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = k

