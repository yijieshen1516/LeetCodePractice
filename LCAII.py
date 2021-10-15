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
        self.countp = 0
        self.countq = 0

        ans = self.helper(root, p, q)

        if not self.countp or not self.countq:
            return None

        return ans

    def helper(self, root, p, q):

        if not root:
            return None

        left = self.helper(root.left, p, q)
        right = self.helper(root.right, p, q)

        if  root.val == p.val:
            self.countp += 1
            return root

        if root.val == q.val:
            self.countq += 1
            return root

        if left and right:
            return root

        if not left and not right:
            return None

        if left:
            return left

        if right:
            return right

root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
p = TreeNode(5)
q = TreeNode(9)
print(Solution().lowestCommonAncestor(root, p, q))
