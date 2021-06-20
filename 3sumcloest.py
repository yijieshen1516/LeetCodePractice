class Solution(object):
    def threeSumCloest(self, nums, target):

        nums.sort()

        res = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1

            while l < r:
                s = nums[i] + nums[l] + nums[r]

                if abs(target - s) < abs(target - res):
                    res = s

                if target < s:
                    r -= 1
                elif target > s:
                    l += 1

                else:
                    return res

        return res

nums = [-1, 2, 1, -4]
target = 1
print(Solution().threeSumCloest(nums, target))