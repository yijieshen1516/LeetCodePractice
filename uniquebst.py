class newNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def constructTrees(self, start, end):

        list = []

        if start > end:
            list.append(None)
            return list

        for i in range(start, end + 1):

            leftSubtree = self.constructTrees(start, i - 1)
            rightSubtree = self.constructTrees(i + 1, end)

            for j in range(len(leftSubtree)):
                left = leftSubtree[j]
                for k in range(len(rightSubtree)):
                    right = rightSubtree[k]
                    node = newNode(i)  # making value i as root
                    node.left = left  # connect left subtree
                    node.right = right  # connect right subtree
                    list.append(node)  # add this tree to list

        return list


Solution().constructTrees(0, 3)