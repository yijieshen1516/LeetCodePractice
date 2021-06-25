class Solution(object):

    def longestIncreasingPath(self, matrix):

        if not matrix:
            return 0

        mem = [[0] * len(matrix[0]) for y in range(len(matrix))]
        path = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                path = max(path, self.dfs(matrix, mem, i, j))

        return path

    def dfs(self, matrix, mem, i, j):

        if mem[i][i] != 0:
            return mem[i][j]

        longest_path = 0

        for (m, n) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_i = i + m
            new_j = j + n
            if new_i >= 0 and new_i < len(matrix) and new_j >= 0 and new_j < len(matrix[0]) and matrix[new_i][new_j] > matrix[i][j]:
                longest_path = max(longest_path, self.dfs(matrix, mem, new_i, new_j))

        mem[i][j] = longest_path + 1

        return mem[i][j]


matrix = [[1, 2]]
print(Solution().longestIncreasingPath(matrix))
