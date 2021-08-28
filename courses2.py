from collections import defaultdict

class Solution():

    def findOrder(self, n, prerequisities):

        G = [set() for _ in range(n)]
        for d, s in prerequisities:
            G[s].add(d)
        visited, orders = [0] * n, []

        def dfs_circle(x):
            visited[x] = -1
            for y in G[x]:
                if visited[y] < 0 or (not visited[y] and dfs_circle(y)):
                    return True
            visited[x] = 1
            orders.append(x)
            return False

        for x in range(n):
            if visited[x] == 0 and dfs_circle(x):
                return []
        return orders[::-1]

n = 4
prerequisities = [[1,0],[2,0],[3,1],[3,2]]
#n = 2
#prerequisities = [[0, 1], [1, 0]]
print(Solution().findOrder(n, prerequisities))


# topological sort with dfs (three status, 0 not visited, 1 visiting, 2 finished with visit)
# self.graph = defaultdict(list)
#
# self.buildGraph(prerequisites)
#
# self.visited = [0] * numCourses
# self.FoundCycle = 0
# self.ans = []
#
# for idx in range(numCourses):
#     if self.FoundCycle == 1:
#         break
#     if self.visited[idx] == 0:
#         self.helper(idx)
#
#
# return [] if self.FoundCycle == 1 else self.ans
#
#
# def helper(self, idx):
#
#     self.visited[idx] = 1
#
#     for nei in self.graph[idx]:
#         if self.visited[nei] == 0:
#             self.helper(nei)
#         if self.visited[nei] == 1:
#             self.FoundCycle = 1
#
#     self.visited[idx] = 2
#     self.ans.append(idx)
#
#
# def buildGraph(self, prerequisites):
#
#     for pair in prerequisites:
#
#         self.graph[pair[0]].append(pair[1])
#
