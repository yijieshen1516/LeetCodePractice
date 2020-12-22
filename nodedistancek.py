# Definition for a binary tree node.
from collections import defaultdict, deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        from collections import defaultdict
        # vetex: [parent, left, right]
        graph = defaultdict(list)

        # DFS to build graph
        self.buildGraph(root, None, graph)

        # BFS to retrieve the nodes with given distance
        # Starting from the target node
        q = [(target, 0)]

        # keep the records, since the graph is all connected
        visited = set()
        # results
        ans = []
        while q:
            node, distance = q.pop(0)
            if node in visited:
                continue
            visited.add(node)

            # we've reached the desired distance/radius
            if K == distance:
                ans.append(node.val)

            # we haven't reached the desired distance, keep going
            elif distance < K:
                for child in graph[node]:
                    q.append((child, distance + 1))
            # exceed the desired distance
            # No need to go further

        return ans


    def buildGraph(self, node, parent, graph):

        if node is None:
            return

        if parent is not None:
            graph[node].append(parent)

        if node.left is not None:
            graph[node].append(node.left)
            self.buildGraph(node.left, node, graph)

        if node.right is not None:
            graph[node].append(node.right)
            self.buildGraph(node.right, node, graph)


root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
target = TreeNode(5)
K = 2

print(Solution().distanceK(root, target, K))