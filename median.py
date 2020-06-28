class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        from collections import deque

        deq = deque()
        res = []

        for idx in range(k):

            while len(deq) != 0:
                if nums[idx] > nums[deq[-1]]:
                    deq.pop()
                else:
                    break
            deq.append(idx)

        for idx in range(k, len(nums)):

            res.append(nums[deq[0]])

            if deq[0] < idx - k + 1:
                deq.popleft()

            if nums[idx] > nums[deq[-1]]:
                deq.pop()
            else:
                break

            deq.append(idx)

        return res

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

print(Solution().maxSlidingWindow(nums, k))