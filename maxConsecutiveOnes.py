class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i = 0
        j = 0
        k = 1
        ans = 0

        while j < len(nums):

            k -= 1 - nums[j]

            while k < 0:
                k += 1 - nums[i]
                i += 1

            j += 1

            ans = max(ans, j - i)

        return ans


nums = [1, 0, 1, 1, 0]
print(Solution().findMaxConsecutiveOnes(nums))