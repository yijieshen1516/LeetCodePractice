class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        ans = []
        temp_list = []
        self.bt(ans, temp_list, candidates, target, 0)

        return ans


    def bt(self, ans, temp_list, nums, target, i):
        if target < 0:
            return

        if target == 0:
            ans.append(temp_list[:])
            return

        for j in range(i, len(nums)):
            temp_list.append(nums[j])
            self.bt(ans, temp_list,nums, target-nums[j], j)
            temp_list.pop()
