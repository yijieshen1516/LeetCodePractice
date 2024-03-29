# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution(object):

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """

        self.order = []
        self.prev = None
        self.inorder(root)
        if len(self.order) == 2:
            self.swap(self.order[0][0], self.order[1][1])
        elif len(self.order) == 1:
            self.swap(self.order[0][0], self.order[0][1])
        return

    def inorder(self, root):

        if root == None:
            return
        self.inorder(root.left)
        if self.prev and self.prev.val > root.val:
            self.order.append((self.prev, root))
        self.prev = root
        self.inorder(root.right)
        return

    def swap(self, r1, r2):
        r1.val, r2.val = r2.val, r1.val
        return


root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(2)

print(Solution().recoverTree(root))

"""
morris traveral o(1) space
cur, node, cands = root, TreeNode(-float("inf")), []
while cur:
    if cur.left:
        pre = cur.left
        while pre.right and pre.right != cur:
            pre = pre.right
        if not pre.right:
            pre.right = cur
            cur = cur.left
        else:
            pre.right = None
            if cur.val < node.val:
                cands += [node, cur]
            node = cur
            cur = cur.right
    else:
        if cur.val < node.val:
            cands += [node, cur]
        node = cur
        cur = cur.right

cands[0].val, cands[-1].val = cands[-1].val, cands[0].val

return root
"""