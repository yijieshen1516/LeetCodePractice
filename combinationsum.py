class Solution(object):
    def combinationSum(self, candidates, target):
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, nums, target, index, path, res):
        if target < 0:
            return  # backtracking
        if target == 0:
            res.append(path)
            #res.append(path[:])
            return

        for i in xrange(index, len(nums)):
            #path.append(nums[i])
            self.dfs(nums, target - nums[i], i, path+[nums[i]], res)
            #path.pop()

candidates = [2,3,6,7]
target = 7
print(Solution().combinationSum(candidates, target))


