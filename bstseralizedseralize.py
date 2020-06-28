# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        self.data = []

        self.inorder(root)

        return self.data

    def inorder(self, root):

        if not root:
            self.data.append('null')
            return
        else:
            self.data.append(root.val)

        self.inorder(root.left)
        self.inorder(root.right)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        return self.des_inorder(data)

    def des_inorder(self, data):

        if data[0] == 'null':
            return None

        root = TreeNode(data[0])

        root.left = self.des_inorder(data[1:])
        root.right = self.des_inorder(data[2:])

        return root


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

print(Codec().deserialize(Codec().serialize(root)))


