from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        self.ans = defaultdict(list)

        self.helper(root, 0, 0)

        result = []
        for i in sorted(self.ans.keys()):
            temp = []
            for j in sorted(self.ans[i]):
                temp.append(j[1])
            result.append(temp)
        return result


    def helper(self, root, row, col):

        if not root:
            return

        self.ans[col].append((row, root.val))

        self.helper(root.left, row+1, col-1)
        self.helper(root.right, row+1, col+1)