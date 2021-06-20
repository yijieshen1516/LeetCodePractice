class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        nums.sort()
        res = []

        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):

                l = j + 1
                r = len(nums) -1

                while l < r:
                    sums = nums[i] + nums[j] + nums[l] + nums[r]

                    if sums == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                    elif sums < target:
                        l += 1
                    elif sums > target:
                        r -= 1

        return res

nums = [2, 2, 2, 2]
target = 8
print(Solution().fourSum(nums, target))