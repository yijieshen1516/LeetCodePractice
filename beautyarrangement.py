class Solution(object):
    def arragement(self, n):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = 0
        nums = [i for i in range(1, n+1)]

        self.bt(nums, 1)

        return self.res

    def bt(self, nums, j):
        if j == len(nums)+1:
            self.res += 1
            return

        for idx in range(len(nums)):
            if not (nums[idx] % j and j % nums[idx]):
                self.bt(nums[:idx] + nums[idx + 1:], j+1)

n = 1
print(Solution().arragement(n))