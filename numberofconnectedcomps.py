from collections import defaultdict
from collections import deque

class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """

        # graph = defaultdict(list)
        #
        # for edge in edges:
        #     graph[edge[0]].append(edge[1])
        #     graph[edge[1]].append(edge[0])
        #
        # visited = set()
        # queue = deque()
        # count = 0
        #
        # for i in range(n):
        #     if i not in visited:
        #         queue.append(i)
        #         while queue:
        #             s = queue.popleft()
        #             visited.add(s)
        #             for j in graph[s]:
        #                 if j not in visited:
        #                     queue.append(j)
        #
        #         count += 1
        #
        # return count

        graph = defaultdict(list)

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        visited = set()
        count = 0
        for i in range(n):
            if i not in visited:
                self.dfs(graph, visited, i)
                count += 1

        return count

    def dfs(self, graph, visited, node):

        visited.add(node)

        for i in graph[node]:
            if i not in visited:
                self.dfs(graph, visited, i)


n = 5
edges = [[0,1], [1,2], [3, 4]]
print(Solution().countComponents(n, edges))