class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1

        while left < right -1:
            mid = (left + right)/2

            if nums[mid] > nums[right]:
                if nums[left] <= target and nums[mid] >= target:
                    right = mid
                else:
                    left = mid
            else:
                if nums[mid] <= target and nums[right] >= target:
                    left = mid
                else:
                    right = mid

        if nums[right] == target:
            return right
        if nums[left] == target:
            return left

        return -1


nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
#nums = [1, 3, 5]
#target = 5

print(Solution().search(nums, target))