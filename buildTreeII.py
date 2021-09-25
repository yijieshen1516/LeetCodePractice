class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        root = self.helper(inorder, postorder)

        return root

    def helper(self, inorder, postorder):

        if not inorder or not postorder:
            return

        curr = postorder.pop()
        node = TreeNode(curr)
        idx = inorder.index(curr)

        node.right = self.helper(inorder[idx+1:], postorder)
        node.left = self.helper(inorder[:idx], postorder)


        return node

inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]
print(Solution().buildTree(inorder, postorder))