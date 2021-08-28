class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        i = 0
        j = 0

        while j < len(nums):

            k -= 1 - nums[j]

            if k < 0:
                k += 1 - nums[i]
                i += 1

            j += 1

        return j - i


nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2

print(Solution().longestOnes(nums, k))