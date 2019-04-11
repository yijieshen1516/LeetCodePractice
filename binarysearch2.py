# def binarysearch(array, target):

#     left = 0
#     right = len(array) -1

#     while(left <= right):
#         mid = (right + left) //2
#         if (array[mid] > target):
#             right = mid -1
#         elif (array[mid] < target):
#             left = mid +1
#         else:
#             return mid
    
#     return -1

# array = [1,2,4,6,8,10]
# target = 2
# index = binarysearch(array, target)
# print(index)

def binarysearch(array, target):

    left = 0
    right = len(array) -1

    while (left < right -1):
        mid = (right +left)//2
        if (array[mid] > target):
            right = mid
        elif (array[mid] < target):
            left = mid
        else:
            return mid
    if (array[left] == target):
        return left
    if (array[right] == target):
        return right

    return -1

array = [1,2,4,6,8,10]
target = 2
index = binarysearch(array, target)
print(index)