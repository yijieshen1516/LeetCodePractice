
class newNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def levelOrderBottom1(self, root):

    #     res = []
    #     self.dfs(root, 0, res)
    #     return res
    #
    # def dfs(self, root, level, res):
    #     if root:
    #         if len(res) < level + 1:
    #             res.insert(0, [])
    #
    #         res[-(level+1)].append(root.val)
    #         self.dfs(root.left, level+1, res)
    #         self.dfs(root.right, level+1, res)

        # queue = [root]
        # res = []
        # tmp = []
        # line = []
        # while queue:
        #     node = queue.pop(0)
        #     if node.left:
        #         line.append(node.left)
        #     if node.right:
        #         line.append(node.right)
        #     tmp.append(node.val)
        #
        #     if not queue:
        #         res.append(tmp)
        #         if line:
        #             queue = line
        #             line = []
        #             tmp = []

        # queue = [(root, 0)]
        # res = []
        # while queue:
        #
        #     node, level = queue.pop(0)
        #     if len(res) < level+1:
        #         res.append([])
        #
        #     if level %2 == 1:
        #         res[level].insert(0, node.val)
        #     else:
        #         res[level].append(node.val)
        #
        #     if node.left:
        #         queue.append((node.left, level+1))
        #     if node.right:
        #         queue.append((node.right, level+1))
        #
        # return res

    #     from collections import defaultdict
    #
    #     res = []
    #     self.nodeMap = defaultdict(list)
    #
    #     self.dfs(root, 0)
    #
    #     for value in self.nodeMap.values():
    #         res.extend(value)
    #
    #     return res
    #
    # def dfs(self, node, level):
    #
    #     if not node:
    #         self.nodeMap[level].append(None)
    #         return
    #
    #     self.nodeMap[level].append(node.val)
    #
    #     self.dfs(node.left, level+1)
    #     self.dfs(node.right, level+1)

        pos = 0
        queue = [(root, 0)]
        res = []

        while queue:

            curr = []

            for _ in range(len(queue)):
                node, pos = queue.pop(0)
                curr.append((node.val, pos))

                if node.left:
                    queue.append((node.left, pos*2))
                if node.right:
                    queue.append((node.right, pos*2+1))

            res.append(curr)

        return res

root = None
root = newNode(4)
root.left = newNode(2)
root.right = newNode(9)
root.left.left = newNode(3)
root.left.right = newNode(8)
root.right.right = newNode(7)

print(Solution().levelOrderBottom1(root))




