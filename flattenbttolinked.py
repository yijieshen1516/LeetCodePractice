# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.


        """
        if not root:
            return None


        self.prev = TreeNode(0)
        self.dummy = self.prev

        self.dfs(root)

        return self.dummy.right


    def dfs(self, root):

        if not root:
            return None

        self.prev.right = root
        self.prev.left = None
        self.prev = root

        self.dfs(root.left)
        self.dfs(root.right)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.right = TreeNode(6)
print(Solution().flatten(root))
