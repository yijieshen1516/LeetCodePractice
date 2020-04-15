
class Solution(object):
    def averageOfLevels(self, root):
        info = []
        def dfs(node, depth = 0):
            if node:
                if len(info) <= depth:
                    info.append([0, 0])
                info[depth][0] += node.val
                info[depth][1] += 1
                dfs(node.left, depth + 1)
                dfs(node.right, depth + 1)
        dfs(root)

        return [s/float(c) for s, c in info]

class newNode:
    def __init__(self, data):
        self.val = data
        self.left = self.right = None

root = None
root = newNode(4)  
root.left = newNode(2)  
root.right = newNode(9)  
root.left.left = newNode(3)  
root.left.right = newNode(8)  
root.right.right = newNode(7)  

Solution().averageOfLevels(root)