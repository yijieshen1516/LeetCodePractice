# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """

        if not preorder:
            return

        return self.helper(0, len(preorder), preorder)

    def helper(self, l, r, preorder):

        if l >= r:
            return

        node = TreeNode(preorder[l])
        i = l+1

        while (i < r and preorder[i] < node.val):
            i += 1

        node.left = self.helper(l+1, i, preorder)
        node.right = self.helper(i, r, preorder)

        return node

preorder = [8, 5, 1, 7, 10, 12]
print(Solution().bstFromPreorder(preorder))