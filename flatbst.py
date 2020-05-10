# Definition for a binary tree node.
class newNode(object):
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
        self.curr = newNode(None)
        self.helper(root)

        return self.curr

    def helper(self, root):

        if not root:
            return None

        if self.curr == None:
            self.curr = root
        else:
            self.curr.right = root
            self.curr.left = None
            self.curr = root

        self.helper(root.left)
        self.helper(root.right)


root = newNode(4)
root.left = newNode(2)
root.right = newNode(9)
root.left.left = newNode(3)
root.left.right = newNode(8)
root.right.right = newNode(7)

print(Solution().flatten(root))