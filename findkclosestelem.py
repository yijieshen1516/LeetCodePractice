def closestelem(array, target):

    left = 0
    right = len(array) -1

    while (left < right -1):
        mid = (left + right) //2
        if (array[mid] < target):
            left = mid
        elif (array[mid] > target):
            right = mid
        else:
            return mid
    return left if abs(array[left] - target) < abs(array[right] - target) else right




