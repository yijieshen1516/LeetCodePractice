# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        dp = [[[] for _ in range(n + 1)] for _ in range(n + 1)]

        return self.helper(0, n, dp)

    def helper(self, start, end, dp):
        if start > end:
            return [None]

        if len(dp[start][end]) > 0:
            return dp[start][end]

        for idx in range(start, end):
            left = self.helper(start, idx - 1, dp)
            right = self.helper(idx + 1, end, dp)
            for l in range(len(left)):
                for r in range(len(right)):
                    node = TreeNode(idx)
                    node.left = left[l]
                    node.right = right[r]
                    dp[start][end].append(node)

        return dp[start][end]

n= 3
print(Solution().generateTrees(n))