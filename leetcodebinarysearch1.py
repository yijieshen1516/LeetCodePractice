
# class Solution(object):

#     def __init__(self,nums, target):
#         self.nums = nums
#         self.target = target

#     def searchRange(self):
#         n = len(self.nums)
#         left, right = -1, -1
#         l, r = 0, n-1
#         while l < r:
#             m = (l+r)//2
#             if self.nums[m] < self.target: 
#                 l = m+1
#             elif self.nums[m] > self.target:
#                 r = m-1
#             else:
#                 r = m
#         if self.nums[l] != self.target: 
#             return -1, -1
#         left = l
#         l, r = left, n-1
#         while l < r:
#             m = (l+r)//2 + 1
#             if self.nums[m] == self.target: 
#                 l = m
#             else: 
#                 r = m-1
#         right = l
#         return left, right

# if __name__ == "__main__":
 
#     arr = [1, 2, 2, 2, 2, 3, 4, 7 ,8 ,8 ]
#     #arr = [1, 2, 3, 4]
#     x = 2
#     c = Solution(arr, x)
#     left, right = c.searchRange()
#     print(left, right)


def firstlastelem(array, target):
    
    left = 0
    right = len(array) -1
    l = -1
    r = -1

    while (left < right -1):
        mid = (left+right)//2
        if (array[mid] < target):
            left = mid
        else:
            right = mid
    if (array[left] == target):
        l = left
    if (array[right] == target):
        l = right
    left = l
    right = len(array) -1

    while(left < right -1):
        mid = (left+right) //2
        if (array[mid] <= target):
            left = mid
        else:
            right = mid
    if (array[left] == target):
        r = left
    if (array[right] == target):
        r = right
    return l,r

arr = [1, 2, 2, 2, 2, 3, 4, 7 ,8 ,8 ]
x = 2
left,right = firstlastelem(arr,x)
print(left,right)


