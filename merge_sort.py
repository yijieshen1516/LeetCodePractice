
def merge(left, right, array):

    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if (left[i] < right[j]):
            array[k] = left[i]
            i = i+1
        else:
            array[k] = right[j]
            j = j+1
        k = k+1


    while (i < len(left)):
        array[k] = left[i]
        i = i+1
        k = k+1
    
    while (j < len(right)):
        array[k] = right[j]
        j = j+1
        k = k+1

def mergesort(array):

    if(len(array)<2):
        return
    
    mid = len(array)//2
    left=[]
    right=[]

    for i in range(mid):
        left.append(array[i])

    for j in range(mid, len(array)):
        right.append(array[j])

    mergesort(left)
    mergesort(right)

    print(left, right)

    merge(left, right, array)

    print(array)

array = [99, 21, 19, 22, 28, 11, 14, 18]

mergesort(array)
print(array)


