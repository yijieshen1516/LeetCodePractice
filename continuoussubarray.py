class Solution(object):

    def checkSubarraySum(self, nums, k):

        res = 0
        prefix_sum = {}

        prefix_sum[0] = -1

        for i in range(len(nums)):
            res += nums[i]

            if k != 0 :
                res %= k

            if res in prefix_sum:
                if (i - prefix_sum[res]) >= 2:
                    return True

            else:
                prefix_sum[res] = i

        return False


nums = [23, 2, 4, 6, 7]
k = 6
print(Solution().checkSubarraySum(nums, k))