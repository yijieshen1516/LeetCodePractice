# Definition for a binary tree node.
import collections

class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Codec:

    def serialize(self, root):

        self.data = []

        self.levelorder(root)

        return self.data

    def levelorder(self, root):
        if not root:
            return []

        q = collections.deque()
        q.append(root)

        while q:
            size = len(q)

            for _ in range(size):
                node = q.popleft()
                if node is not None:
                    self.data.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                else:
                    self.data.append(None)

        return self.data

    def deserialize(self, data):

        return self.de_levelorder(data)

    def de_levelorder(self, data):

        if not data:
            return None

        root = TreeNode(data[0])
        level = collections.deque([root])
        i = 1
        while i < len(data):
            node = level.popleft()
            if data[i] is not None:
                node.left = TreeNode(data[i])
                level.append(node.left)
            if data[i+1] is not None:
                node.right = TreeNode(data[i+1])
                level.append(node.right)

            i += 2

        return root

    def helper(self, root):

        if not root:
            return

        self.helper(root.left)
        print(root.val)
        self.helper(root.right)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.left.left = TreeNode(4)


codec = Codec()
print(codec.helper(codec.deserialize(codec.serialize(root))))


"""
def serialize(self, root):

self.data = []

self.preorder(root)

return self.data

def preorder(self, root):

if not root:
    self.data.append('null')
    return
else:
    self.data.append(root.val)

self.preorder(root.left)
self.preorder(root.right)


def deserialize(self, data):


return self.des_preorder(data)

def des_preorder(self, data):

if data[0] == 'null':
    return None

root = TreeNode(data[0])

root.left = self.des_preorder(data[1:])
root.right = self.des_preorder(data[2:])

return root
"""