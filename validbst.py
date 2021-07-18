# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        lower = float('-inf')
        upper = float('inf')

        return self.helper(root, lower, upper)

    def helper(self, root, lower, upper):

        if not root:
            return True

        left = self.helper(root.left, lower, root.val)
        right = self.helper(root.right, root.val, upper)

        return left and right and (lower < root.val < upper)


root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.right = TreeNode(6)
print(Solution().isValidBST(root))