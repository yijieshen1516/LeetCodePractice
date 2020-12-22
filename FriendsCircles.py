class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        n = len(M)
        ans = 0
        visited = [0] * n
        for i in range(n):
            if visited[i]:
                continue
            self.dfs(M, i, n, visited)
            ans += 1

        return ans

    def dfs(self, M, i, n, visited):

        if visited[i]:
            return

        visited[i] = 1
        for j in range(n):
            if M[i][j] and not visited[j]:
                self.dfs(M, j, n, visited)


M = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(Solution().findCircleNum(M))