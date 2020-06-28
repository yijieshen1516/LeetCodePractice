class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """

        dp = {}
        return self.helper(nums, S, dp, 0)


    def helper(self, nums, S, dp, i):

        if i == len(nums):
            if S == 0:
                return 1
            else:
                return 0
        else:
            if S in dp:
                return dp[S]

            left = self.helper(nums, S - nums[i], dp, i + 1)
            right = self.helper(nums, S + nums[i], dp, i + 1)

            dp[S] = left + right
            return dp[S]

nums = [1, 1, 1, 1, 1]
S = 3
print(Solution().findTargetSumWays(nums, S))