def closestelem(arr, k, x):

    left = 0
    right = len(arr) - k

    while left < right:
        mid = left + (right - left)//2

        if x <= arr[mid]:
            right = mid
        elif x >= arr[mid + k]:
            left = mid + 1
        elif x - arr[mid] > arr[mid + k] - x:
            left = mid + 1
        else:
            right = mid
    return arr[left : left + k]

#arr = [1, 2, 3, 4, 5]
#x = -1
#k = 4

arr = [12, 16, 22, 30, 35, 39, 42,
       45, 48, 50, 53, 55, 56]
x = 35
k = 4

print(closestelem(arr, k, x))




