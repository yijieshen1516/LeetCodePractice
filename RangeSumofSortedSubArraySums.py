def count_less_or_equal(nums, target):
  left = 0
  window_sum = 0
  count = 0
  total_sum = 0 # sum of all the subarray <= target
  for right in range(len(nums)):
    rval = nums[right]
    window_sum += rval

    while window_sum > target:
      lval = nums[left]
      window_sum -= lval
      left += 1

    count += right - left + 1
    total_sum += sum([ nums[j] * (j-left+1) for j in range(left, right+1)])

  print(count, total_sum)
  return count, total_sum

def binary_search(k, nums):
  if k == 0:
    return 0, 0

  left = min(nums)
  right = sum(nums)
  while left < right-1:
    mid = (left + right) // 2
    if count_less_or_equal(nums, mid)[0] >= k:
      right = mid
    else:
      left = mid

  if count_less_or_equal(nums, left) == k:
    result = left
  else:
    result = right

  cnt, val = count_less_or_equal(nums, result)
  return left, val

def sum_of_first_k(index, nums):
  _, total = binary_search(index, nums)
  return total

class Solution:
  def rangeSum(self, nums, n, left, right):
    a = sum_of_first_k(right, nums)
    b = sum_of_first_k(left - 1, nums)
    return (a - b) % (10**9 + 7)

nums = [1, 2, 3, 4]
n = len(nums)
print(Solution().rangeSum(nums, n, 1, 5))