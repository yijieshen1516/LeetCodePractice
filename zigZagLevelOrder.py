# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):

        if not root:
            return []

        queue = [(root, 0)]
        ans = []


        while queue:
            curr = []

            for i in range(len(queue)):
                node, level = queue.pop(0)

                curr.append(node.val)

                if node.left:
                    queue.append((node.left, level+1))
                if node.right:
                    queue.append((node.right, level+1))

            if level % 2 == 0:
                ans.append(curr)
            else:
                ans.append(curr[::-1])

        return ans

    #
    #     if not root:
    #         return None
    #
    #     self.ans = []
    #     self.helper(root, 0)
    #
    #     return self.ans
    #
    #
    # def helper(self, root, level):
    #
    #
    #     if not root:
    #         return
    #
    #
    #     if len(self.ans) <= level:
    #         self.ans.append([])
    #
    #
    #     if level % 2 == 1:
    #         self.ans[level].insert(0, root.val)
    #
    #     else:
    #         self.ans[level].append(root.val)
    #
    #
    #     self.helper(root.left, level+1)
    #     self.helper(root.right, level+1)