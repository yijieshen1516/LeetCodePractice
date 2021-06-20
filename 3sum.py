class Solution(object):
  # def threeSum(self, nums, target):
  #   results = []
  #   nums.sort()
  #   for i in range(len(nums)-2):
  #     l = i + 1; r = len(nums) - 1
  #     t = target - nums[i]
  #     if i == 0 or nums[i] != nums[i-1]:
  #       while l < r:
  #         s = nums[l] + nums[r]
  #         if s == t:
  #           results.append([nums[i], nums[l], nums[r]])
  #           while l < r and nums[l] == nums[l+1]: l += 1
  #           while l < r and nums[r] == nums[r-1]: r -= 1
  #           l += 1; r -=1
  #         elif s < t:
  #           l += 1
  #         else:
  #           r -= 1
  #
  #   return results
  def threeSum(self, nums, target):
    nums.sort()
    res = []
    for i in range(len(nums)):
      if nums[i] > 0:
        break
      if i == 0 or nums[i-1] != nums[i]:
        self.twoSum(nums, i, res)

    return res

  def twoSum(self, nums, i, res):
    seens = set()
    j = i + 1
    while j < len(nums):
      rest = -nums[i] - nums[j]
      if rest in seens:
        res.append([nums[i], nums[j], rest])
        while j + 1 < len(nums) and nums[j] == nums[j+1]:
          j += 1
      seens.add(nums[j])
      j += 1

nums = [-1, 1, 0, 1, 2, 3]
target = 3
print(Solution().threeSum(nums, target))