def partition(array, low, up):

    i = low +1
    j = up
    pivot = array[low]

    while (i <= j):
        while (array[i] < pivot) and (i<up):
            i = i +1
        while (array[j] > pivot):
            j = j -1
        if (i< j):
            array[i], array[j] = array[j], array[i]
            i = i+1
            j = j-1
        else:
            i = i+1
    array[low] = array[j]
    array[j] = pivot

    return j

# quick sort implementation details
# 1. the partition function is to find the correct index of pivot value. 
#    pivot value can be the first element of list
#    left array should be smaller than pivot value
#    right array should be larger than pivot value
# 2. recursive call partition function as left half and right half array
# 3. divide and concur to call main sort function

array = [48, 44, 19, 59, 72, 80, 42, 65, 82, 8, 95, 68]
low = 0
up = len(array) -1

def quicksort(array, low, up):
    if (low > up):
        return
    pivt_loc = partition(array, low, up)
    quicksort(array, low, pivt_loc -1)
    quicksort(array, pivt_loc +1, up)

quicksort(array, low, up)
print(array)