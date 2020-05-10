class Solution(object):
    def subsets(self, nums):
        ans = []
        subset = []
        for idx in range(len(nums)+1):
            self.bt(ans, subset, 0, idx, nums)

        return ans

    def bt(self, ans, subset, current_position, N, nums):

        if len(subset) == N:
            ans.append(subset[:])
            return

        for m in range(current_position, len(nums)):
            subset.append(nums[m])
            self.bt(ans, subset, m+1, N, nums)
            subset.pop()

nums = [1, 2, 3]
print(Solution().subsets(nums))