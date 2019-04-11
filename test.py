def quickSort(arr, left, right):
    if left < right:
        mid = partition(arr, left, right)
        quickSort(arr, left, mid - 1)
        quickSort(arr, mid + 1, right)
    return arr


def partition(arr, left, right):
    pivot = arr[right]
    slow = left - 1
    for fast in range(left, right):
        if arr[fast] < pivot:
            slow += 1
            arr[slow], arr[fast] = arr[fast], arr[slow]
    arr[slow+1], arr[right] = arr[right], arr[slow+1]
    return slow + 1


if __name__ == "__main__":
    a = [48, 44, 19, 59, 72, 80, 42, 65, 82, 8, 95, 68]
    print(quickSort(a, 0, len(a)-1))