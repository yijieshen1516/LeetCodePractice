class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = {}
        return self.helper(nums, target, dp)

    def helper(self, nums, target, dp):

        count = 0

        if target < 0:
            return 0

        if target == 0:
            return 1

        if target in dp:
            return dp[target]

        for num in nums:
            count += self.helper(nums, target - num, dp)

        dp[target] = count
        return dp[target]

nums = [1, 2, 3]
target = 4
print(Solution().combinationSum4(nums, target))