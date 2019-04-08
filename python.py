
class Solution(object):

    def __init__(self,nums, target):
        self.nums = nums
        self.target = target

    def searchRange(self):
        n = len(self.nums)
        left, right = -1, -1
        l, r = 0, n-1
        while l < r:
            m = (l+r)//2
            if self.nums[m] < self.target: 
                l = m+1
            else: 
                r = m
        if self.nums[l] != self.target: 
            return -1, -1
        left = l
        l, r = left, n-1
        while l < r:
            m = (l+r)//2 + 1
            if self.nums[m] == self.target: 
                l = m
            else: 
                r = m-1
        right = l
        return left, right

if __name__ == "__main__":
 
    arr = [1, 2, 2, 2, 2, 3, 4, 7 ,8 ,8 ]
    x = 2
    c = Solution(arr, x)
    left, right = c.searchRange()
    print(left, right)





