class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        curr = []
        self.length = len(nums)

        self.bt(ans, curr, nums)

        return ans

    def bt(self, ans, curr, nums):
        if len(curr) == self.length:
            ans.append(curr[:])
            return

        for idx in range(len(nums)):
            if nums[idx] not in curr:
                curr.append(nums[idx])
                self.bt(ans, curr, nums[:idx] + nums[idx + 1:])
                curr.pop()

nums = [1,2,3]
print(Solution().permute(nums))