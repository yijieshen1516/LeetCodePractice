def firstoccur(array, target):

    left = 0
    right = len(array) -1

    while(left < right-1):
        mid = (left + right) //2
        if (array[mid] < target):
            left = mid
        elif (array[mid] >= target):
            right = mid
    if (array[left] == target):
        return left
    if (array[right] == target):
        return right
    return -1

array=[1,2,2,3,4,5,5,6,7]
target = 2
index = firstoccur(array, target)
print(index)
        

    