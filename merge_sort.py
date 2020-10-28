import random as rd

def merge(arr):
    if len(arr) > 1:
        # copy data into temp arrays
        mid = len(arr) //2
        left = arr[:mid]
        right = arr[mid:]
        #
        merge(left)
        merge(right)
        #
        i = j = k = 0
        # copy data from temp arrays
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j +=1
            k +=1
        # checking if elements are left
        while i < len(left):
            arr[k] = left[i]
            i+= 1
            k += 1
        #
        while j < len(right):
            arr[k] = right[j]
            j+=1
            k+=1
    return arr


if __name__ == '__main__':
    myarr = [rd.randint(1,4096) for x in range(1000)]
    print('before')
    print(myarr)
    merge(myarr)
    print('after')
    print(myarr)


