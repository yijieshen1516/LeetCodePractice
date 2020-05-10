class Solution(object):
    def subsets(self, nums):
        ans = []
        subset = []
        self.bt(ans, subset, 0, len(nums), nums)
        return ans

    def bt(self, ans, subset, current_position, N, nums):

        if current_position == N:
            ans.append(subset[:])
            return

        # choose
        subset.append(nums[current_position])
        self.bt(ans, subset, current_position+1, N, nums)
        subset.pop()

        # not to choose
        self.bt(ans, subset, current_position + 1, N, nums)


nums = [1, 2, 3]
print(Solution().subsets(a))