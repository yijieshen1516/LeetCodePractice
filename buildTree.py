# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

import collections

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # if not preorder and not inorder:
        #     return
        #
        # root = TreeNode(preorder[0])
        # mid = inorder.index(preorder[0])
        #
        # root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        # root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        #
        # return root

        root = self.helper(preorder, inorder)
        self.levelMap = collections.defaultdict(list)
        self.levelorder(root, 0)
        res = []

        for val in self.levelMap.values():
            res.extend(val)

        return res

    def levelorder(self, root, level):

        if not root:
            self.levelMap[level].append(None)
            return

        self.levelMap[level].append(root.val)

        self.levelorder(root.left, level+1)
        self.levelorder(root.right, level+1)


    def helper(self, preorder, inorder):

        if not preorder or not inorder:
            return

        curr = preorder.pop(0)
        node = TreeNode(curr)
        index = inorder.index(curr)

        node.left = self.helper(preorder, inorder[:index])
        node.right = self.helper(preorder, inorder[index+1:])

        return node

preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

print(Solution().buildTree(preorder, inorder))