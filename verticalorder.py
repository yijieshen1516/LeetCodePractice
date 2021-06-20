from collections import defaultdict
class newNode:
    def __init__(self, data):
        self.val = data
        self.left = self.right = None

class Solution(object):
    def verticalorder(self, root):

       queue = [(root, 0)]
       res = defaultdict(list)

       while queue:

           node, column = queue.pop(0)

           if node:

                res[column].append(node.val)

                if node.left:
                    queue.append((node.left, column-1))
                if node.right:
                    queue.append((node.right, column+1))


       return res

root = None
root = newNode(4)
root.left = newNode(2)
root.right = newNode(9)
root.left.left = newNode(3)
root.left.right = newNode(8)
root.right.right = newNode(7)

print(Solution().verticalorder(root))
