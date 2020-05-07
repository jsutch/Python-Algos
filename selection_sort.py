def selectionSort(arr):
    """
    Find minimum, then swap into left hand sorted arr[n]
    i is the loop pointer, j is the sorting pointer
    and k is the minimum value
    """
    for i in range(len(arr)):
        k = i
        for j in range(i+1, len(arr)):
            if arr[k] > arr[j]:
                k = j

        arr[i], arr[k] = arr[k], arr[i]
