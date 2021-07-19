
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        remainsum = sum
        self.ans = []

        self.helper(root, res, remainsum)

        return self.ans

    def helper(self, root, res, remainsum):

        if not root:
            return None

        res.append(root.val)

        if not root.left and not root.right and remainsum == root.val:
            self.ans.append(res[:])


        self.helper(root.left, res, remainsum - root.val)
        self.helper(root.right, res, remainsum - root.val)
        res.pop()

