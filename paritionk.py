class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        total_sum = sum(nums)

        if total_sum % k != 0:
            return False

        target_sum = total_sum //k

        nums.sort(reverse=True)

        taken = [False] * len(nums)

        def bt(index, count, curr_sum):

            if count == k-1:
                return True

            if curr_sum > target_sum:
                return False

            if curr_sum == target_sum:
                return bt(0, count+1, 0)

            for j in range(index, len(nums)):
                if not taken[nums[j]]:
                    if bt(j+1, count, curr_sum+nums[j]):
                        return True


            return False

        return bt(0, 0, 0)


#nums = [4, 3, 2, 3, 5, 2, 1]
#k = 4
nums = [2, 2, 2, 2, 3, 4, 5]
k = 4
print(Solution().canPartitionKSubsets(nums, k))