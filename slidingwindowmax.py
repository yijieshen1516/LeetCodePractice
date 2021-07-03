import heapq

class Solution(object):
    def maxSlidingWindow(self, nums, k):

        queue = []
        res = []

        for i in range(len(nums)):
            num = nums[i]
            while queue and num > queue[-1]:
                queue.pop()

            queue.append(num)

            if i >= k-1:
                res.append(queue[0])

        return res

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(Solution().maxSlidingWindow(nums, k))





