# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_value = 0
        self.count = 0
        self.dfs(root)

        return self.count

    def dfs(self, node):

        if not node:
            return

        if node.val >= self.max_value:
            self.count += 1

        self.max_value = max(self.max_value, node.val)

        self.dfs(node.left)
        self.dfs(node.right)