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

print(Solution().findOrder(n, prerequisities))

