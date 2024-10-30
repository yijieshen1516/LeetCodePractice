# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        if not root:
            return None

        if root is p or root is q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        elif left:
            return left

        elif right:
            return right

        else:
            return None


root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
p = TreeNode(5)
q = TreeNode(1)

print(Solution().lowestCommonAncestor(root, p, q))


