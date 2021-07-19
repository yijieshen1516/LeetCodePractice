# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """

        if not root:
            return

        self.diff = float('inf')
        self.dfs(root, target)

        return self.r

    def dfs(self, root, target):

        if not root:
            return None

        if abs(target - root.val) <= self.diff:
            self.diff = abs(target - root.val)
            self.r = root.val

        self.dfs(root.left, target)
        self.dfs(root.right, target)

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
target = 3.714286
print(Solution().closestValue(root, target))