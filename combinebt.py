class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1 and not t2: return None
        if t1:
            v1, L1, R1 = t1.val, t1.left, t1.right
        else:
            v1, L1, R1 = 0, None, None
        if t2:
            v2, L2, R2 = t2.val, t2.left, t2.right
        else:
            v2, L2, R2 = 0, None, None
        node = TreeNode(v1+v2)
        node.left = self.mergeTrees(L1, L2)
        node.right = self.mergeTrees(R1, R2)

        return node


t1 = TreeNode(1)
t1.left = TreeNode(2)
t1.right = TreeNode(3)
t1.left.right = TreeNode(5)
t1.left.left = TreeNode(4)
t1.right.right = TreeNode(6)


t2 = TreeNode(10)
t2.left = TreeNode(20)
t2.right = TreeNode(30)
t2.left.right = TreeNode(50)
t2.left.left = TreeNode(40)
t2.right.right = TreeNode(60)

print(Solution().mergeTrees(t1, t2).val)