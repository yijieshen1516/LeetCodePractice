class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """

        N = len(nums)

        if not N:
            return 0

        memo = {}

        def helper(index, k):

            if index == N:
                if S == k:
                    return 1
                else:
                    return 0

            key = (index, k)

            if key in memo:
                return memo[key]

            memo[key] = 0

            for candidate in [nums[index], -nums[index]]:
                memo[key] += helper(index+1, k+candidate)

            return memo[key]

        return helper(0, 0)

nums = [1, 1, 1, 1, 1]
S = 3
print(Solution().findTargetSumWays(nums, S))


#
# class Solution:
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
#
#         '''
#         problem:
#
#         - have to add either +  or -
#         - need to use all the array elements
#         - return all combination evaluate to the target result
#
#
#         Algo:
#
#         - Need to start from the first element and go all the way to the last element.
#         - each element can get + or - in front of it
#         - if everything evaluated to the target sum, output += 1
#
#         - brute force - backTracking problem
#         - optimized solution - memoization.
#
#         decision tree:
#
#         [1,2,3,4,5], target = 15
#                              ''
#                               |
#                           +/     \-
#                           1       1
#                         +/ \-   +/ \-
#                       2    2    2    2
#                     +/ \-+/ \-+/ \-+/ \-
#
#         Time : O(2^n) without memo, O(n) with memo
#         memoization: O(n)
#
#         '''
#
#         N = len(nums)
#
#         if not N:
#             return 0
#
#         memo = {}
#
#         def helper(index, k):
#
#             if index == N:
#                 if target == k:
#                     return 1
#                 else:
#                     return 0
#
#             key = (index, k)
#
#             if key in memo:
#                 return memo[key]
#
#             memo[key] = 0
#
#             for candidate in [nums[index], -nums[index]]:
#                 memo[key] += helper(index+1, k+candidate)
#
#             return memo[key]
#
#         return helper(0, 0)